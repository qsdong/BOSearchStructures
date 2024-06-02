
1. GPyOpt\acquisitions\ 

        Copy LCB.py to LCB_dqs.py

        Add {distance_weight, distance_sigma, distance_lambda, list_size, X, Y} parameters to the __init__ function

        see LCB_dqs.py for details

2. GPyOpt\acquisitions\__init__.py

        from .LCB_dqs import AcquisitionLCB_dqs

        elif name == 'LCB_dqs':
                return AcquisitionLCB_dqs

3. GPyOpt\methods\bayesian_optimization.py

        from ..acquisitions import AcquisitionLCB_dqs

        def _acquisition_chooser(self):
            return self.problem_config.acquisition_creator(self.acquisition_type, self.model, self.space, self.acquisition_optimizer, self.cost.cost_withGradients, X=self.X, Y=self.Y)


4. GPyOpt\util\arguments_manager.py

        from ..acquisitions import AcquisitionLCB_dqs

        def acquisition_creator(self, acquisition_type, model, space, acquisition_optimizer, cost_withGradients,X=None,Y=None):

        distance_weight = self.kwargs.get('distance_weight',1)
        distance_sigma = self.kwargs.get('distance_sigma',0.01)
        distance_lambda = self.kwargs.get('distance_lambda',0.01)
        list_size = self.kwargs.get('list_size',20)


        elif acquisition_type =='LCB_dqs':
            return AcquisitionLCB_dqs(model, space, acquisition_optimizer, None, acquisition_weight, distance_weight, distance_sigma, distance_lambda, list_size, X=X, Y=Y)
