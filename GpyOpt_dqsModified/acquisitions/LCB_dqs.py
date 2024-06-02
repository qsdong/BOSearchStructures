# Copyright (c) 2016, the GPyOpt Authors
# Licensed under the BSD 3-clause license (see LICENSE.txt)

from .base import AcquisitionBase
from ..util.general import get_quantiles

import numpy as np

class AcquisitionLCB_dqs(AcquisitionBase):
    """
    GP-Lower Confidence Bound acquisition function with constant exploration weight.
    See:
    
    Gaussian Process Optimization in the Bandit Setting: No Regret and Experimental Design
    Srinivas et al., Proc. International Conference on Machine Learning (ICML), 2010

    :param model: GPyOpt class of model
    :param space: GPyOpt class of domain
    :param optimizer: optimizer of the acquisition. Should be a GPyOpt optimizer
    :param cost_withGradients: function
    :param jitter: positive value to make the acquisition more explorative

    .. Note:: does not allow to be used with cost

    """

    analytical_gradient_prediction = True

    def __init__(self, model, space, optimizer=None, cost_withGradients=None, exploration_weight=2, distance_weight = 1, distance_sigma=0.01, distance_lambda=0.01, list_size=np.Inf, X = None, Y = None):
        self.optimizer = optimizer
        super(AcquisitionLCB_dqs, self).__init__(model, space, optimizer)
        self.exploration_weight = exploration_weight
        self.distance_weight = distance_weight
        self.distance_sigma = distance_sigma
        self.distance_lambda = distance_lambda
        self.list_size = list_size  # maximum number of points used to compute the distance, i.e., tabu length

        if X.shape[0]<list_size:
            self.X = X
        else:
            self.X = X[-list_size:,:]

        self.bounds = space.get_bounds()
        self.factor = np.array([bound[1] - bound[0] for bound in self.bounds])
        self.paraCount = X.shape[1]

        if cost_withGradients is not None:
            print('The set cost function is ignored! LCB acquisition does not make sense with cost.')  
    
    def _compute_minDistance(self,x):
        """
        Compute the minimum distance between each point in x and X
        X is the set of points that have been evaluated
        x is the set of points under consideration
        """
        min_d = np.zeros((x.shape[0],1))
        for idx,xi in enumerate(x):
            tmp = (xi-self.X)/self.factor
            min_d[idx] = np.min(np.linalg.norm(tmp,axis=1))/np.sqrt(self.paraCount) 
            # min_d is normalized by the number of parameters, thus the range is [0,1]
        return min_d

    def _compute_acq(self, x):
        """
        Computes the GP-Lower Confidence Bound 
        """
        # print("This is the LCB acquisition function. Modified by Qingshu Dong 2023.11.24")
        min_d = self._compute_minDistance(x)

        m, s = self.model.predict(x)   
        f_acqu = -m + self.exploration_weight * s + self.distance_weight * (1- np.tanh((min_d-self.distance_sigma)/self.distance_lambda))/2.0
        
        return f_acqu

    def _compute_acq_withGradients(self, x):
        """
        Computes the GP-Lower Confidence Bound and its derivative
        """
        min_d = self._compute_minDistance(x)

        m, s, dmdx, dsdx = self.model.predict_withGradients(x) 
        f_acqu = -m + self.exploration_weight * s + self.distance_weight * (1- np.tanh((min_d-self.distance_sigma)/self.distance_lambda))/2.0
        df_acqu = -dmdx + self.exploration_weight * dsdx
        return f_acqu, df_acqu

