# -*- coding: utf-8 -*-

import GPyOpt
import numpy as np


class BayesOpt_NoWait:  # give next suggestion without waiting for the previous results
    def __init__(self, x_step=None, y_step=np.array([[np.nan]]), args = None, thetaCount=0, levelCount=0, lxyzCount=1, squenceCount=0):
        # AB ， levelCount= 0(fixlevel), 1
        # ABC，levelCount= 0(fixlevel), 2
        # AB ，squenceCount=0
        # ABC，squenceCount=1
        # Cubic，lxyzCount=1
        # Trigonal, Hexagonal, Tetragonal, lxyzCount=1(fixratio),2
        # Orthorhombic, lxyzCount=3

        self.isRand = args.rand # Whether to use random search
        basis=args.basis  # number of basis functions
        self.levelCount = levelCount # 0,1,2
        self.lxyzCount = lxyzCount
        self.squenceCount = squenceCount

        self.acquisition_weight = args.weight

        self.distance_weight = args.distance_weight 
        self.distance_sigma = args.distance_sigma   
        self.distance_lambda = args.distance_lambda 
        self.list_size = args.list_size  # number of points to consider in the distance calculation
        self.lxyzBounds = tuple(args.lxyzBounds) # bounds for lxyz values

        self.xnum = len(x_step[0]) # number of parameters
        self.bounds = []           # parameter bounds
        if self.xnum != basis+thetaCount+levelCount+lxyzCount+squenceCount:
            raise ValueError('parameter number not match')
        for i in range(basis):
            self.bounds.append({'name': 'a'+str(i), 'type': 'continuous', 'domain':(-1.0,1.0)}) # coefficients of basis functions (f_{hkl} in the paper), continuous value

        for i in range(thetaCount):
            self.bounds.append({'name': 'theta'+str(i), 'type': 'continuous', 'domain':(0,np.pi)}) #  theta values, continuous value

        if levelCount > 0:
            domainTuple = tuple(np.linspace(0.1, 0.9, 9)) # level values for A, discrete value (0.1, 0.2, ..., 0.8, 0.9)
            self.bounds.append({'name': 'level0', 'type': 'discrete', 'domain':domainTuple}) 
        if levelCount == 2:
            domainTuple = tuple(np.linspace(-0.9, -0.1, 9)) # level values for C, discrete value (-0.9, -0.8, ..., -0.2, -0.1)
            self.bounds.append({'name': 'level1', 'type': 'discrete', 'domain':domainTuple}) 

        for i in range(lxyzCount):
            self.bounds.append({'name': 'lxyz'+str(i), 'type': 'continuous', 'domain':self.lxyzBounds}) # lxyz values, continuous value

        for i in range(squenceCount): # 0 or 1
            domainTuple = tuple([0,1,2]) # squence value (0, 1, 2)'categorical'
            self.bounds.append({'name': 'squence'+str(i), 'type': 'discrete', 'domain':domainTuple})

        self.x_step = x_step # historical parameter points
        self.y_step = y_step # historical free energy values

        self.status_step = [] # status of each parameter point: nan_delete, nan_ignore, unfinished, normal
        # nan_delete: parameter is nan, need to be deleted
        # nan_ignore: parameter is normal, but free energy is nan, need to be ignored
        # unfinished: parameter is suggested, but free energy is not calculated yet, need to be replaced with a specified value
        # normal: both parameter and free energy are normal, need to be included
        for i in range(len(self.y_step)):
            if np.isnan(self.x_step[i][0]):
                self.status_step.append('nan_delete')  # parameter is nan, need to be deleted
            elif np.isnan(self.y_step[i][0]):
                self.status_step.append('nan_ignore')  # parameter is normal, but free energy is nan, need to be ignored
            elif self.y_step[i][0] > 1e3:  # This point has been suggested, but the free energy has not been calculated yet
                self.status_step.append('unfinished')
                print("error, check y value in the file!")
            else:
                self.status_step.append('normal')  # parameter and free energy are normal, need to be included

        self.eps = 0.05  
        self.sd = 0.1

        self.iter_count  = len(self.y_step) # number of BO iterations
        print('init iter_count: {} (include lines with nan)'.format(self.iter_count))
        self.max_pending = 0
        pass

    def suggest_next(self):
        # find the maximum and minimum values in y_step
        y_tmp = self.y_step.copy()          # deep copy !
        y_tmp[self.y_step>1e3] = np.nan     # replace the value of y_step>1e3 with nan
        y_min = np.nanmin(y_tmp)
        y_max = np.nanmax(y_tmp)
        y_mean = (y_min+y_max)/2            # average value, used to replace the unfinished points 

        y_max_nan = y_max+(y_max-y_min)*0.2 # replace the nan value with a value larger than y_max

        pending_count = np.sum(self.y_step>1e3)
        nan_count = np.isnan(self.y_step).sum() - int(np.isnan(self.x_step).sum()/self.xnum) # number of nan values in y_step
        normal_count = y_tmp.shape[0] - np.isnan(y_tmp).sum() # number of normal values in y_step


        x_step2 = None
        y_step2 = None

        for i in range(len(self.y_step)):
            if self.status_step[i] == 'normal': # when both parameter and free energy are normal
                if x_step2 is None:
                    x_step2 = self.x_step[i].reshape(-1,self.xnum)
                    y_step2 = self.y_step[i].reshape(-1,1)
                else:
                    x_step2 = np.vstack((x_step2, self.x_step[i]))
                    y_step2 = np.vstack((y_step2, self.y_step[i]))
            elif self.status_step[i] == 'nan_ignore': # parameter is normal, but free energy is nan, using a specified value to replace, e.g., y_max_nan
                if x_step2 is None:
                    x_step2 = self.x_step[i].reshape(-1,self.xnum )
                    y_step2 = y_max.reshape(-1,1)
                else:
                    x_step2 = np.vstack((x_step2, self.x_step[i]))
                    y_step2 = np.vstack((y_step2, y_max_nan.reshape(-1,1))) 
            elif self.status_step[i] == 'unfinished':  # parameter is suggested, but free energy is not calculated yet, using a specified value to replace, e.g., y_mean
                if x_step2 is None:
                    x_step2 = self.x_step[i].reshape(-1,self.xnum )
                    y_step2 = y_mean.reshape(-1,1)
                else:
                    x_step2 = np.vstack((x_step2, self.x_step[i]))
                    y_step2 = np.vstack((y_step2, y_mean.reshape(-1,1)))

        if x_step2 is None:  # using nan at the very beginning
            x_step2 = np.ones((1,self.xnum))*np.nan
            y_step2 = np.array([[np.nan]])

        ## using random search
        if self.isRand: 
            rand_x_next = []
            for idict in self.bounds:
                if idict['type'] == 'continuous':
                    rand_x_next.append(np.random.uniform(idict['domain'][0], idict['domain'][1]))
                elif idict['type'] == 'discrete':
                    rand_x_next.append(np.random.choice(idict['domain']))
                elif idict['type'] == 'categorical':
                    rand_x_next.append(np.random.choice(idict['domain']))
                else:
                    raise Exception('type error')
            x_next = np.array([rand_x_next])
            print("random next:",x_next,flush=True)
        else: # using Bayesian optimization
            bo_step = GPyOpt.methods.BayesianOptimization(f = None, domain=self.bounds, model_type = 'GP', 
                acquisition_type='LCB_dqs',X = x_step2, Y = y_step2, eps=self.eps, sd = self.sd, 
                acquisition_weight=self.acquisition_weight,
                distance_weight=self.distance_weight, 
                distance_sigma=self.distance_sigma, 
                distance_lambda=self.distance_lambda,
                list_size=self.list_size)
            x_next = bo_step.suggest_next_locations()
            print("BO next:",x_next,flush=True)

        self.print_step_info('len(x_step)', self.x_step)
        self.print_step_info('len(x_step2)', x_step2)
        print("normal_count: {}, nan_count: {}, pending_count: {}".format(normal_count,nan_count,pending_count),flush=True)

        y_next = np.array([[1e6]])  # using a large value as a placeholder
        self.status_step.append('unfinished') # unfinished status

        self.x_step = np.vstack((self.x_step, x_next))
        self.y_step = np.vstack((self.y_step, y_next))

        self.iter_count += 1

        return x_next, self.iter_count-1 

    def update_step(self, y_value, idx, update_ai, update_Lxyz, statusCode):
        self.y_step[idx][0] = y_value

        if np.isnan(self.y_step[idx][0]):
            self.status_step[idx] = 'nan_ignore' # the parameter is normal, but the free energy is nan, need to be ignored

        elif self.y_step[idx][0] > 1e3: 
            print("idx = {}, error y_value:{}".format(idx, y_value))
        else:
            self.status_step[idx] = 'normal' # both parameter and free energy are normal, need to be included
        pass

    def print_step_info(self,var_name,var_array):
        count = 0
        if var_array is not None:
            print(var_name+":",var_array.shape[0], end = ', ')
            count = var_array.shape[0]
        else:
            print(var_name+': None', end = ', ')
        
        return count


class FinishedFlag():
    def __init__(self):
        self.isFinished = [] # list of list, the first element is the index of the parameter (int), the second element is the flag of whether the step is finished (bool)

    def new_para_point(self,iter):
        self.isFinished.append([iter,np.nan]) 
    def update_flag(self,iter):
        for idx in range(len(self.isFinished)):
            if self.isFinished[idx][0] == iter:
                self.isFinished[idx][1] = 1
        return True


class FreeEnergyRecord():
    def __init__(self):
        self.allFreeE = [] # list of list
    def new_para_point(self,iter): 
        self.allFreeE.append([iter,np.nan]) 
    def update_freeE(self,iter,freeE_value): 
        for idx in range(len(self.allFreeE)):
            if self.allFreeE[idx][0] == iter:
                self.allFreeE[idx][1] = freeE_value
        pass
    pass



class AllParaPoint_NoWait():
    def __init__(self, args = None, x_step_init=None, y_step_init=np.array([[np.nan]]), rootDir = '', thetaCount=0,  levelCount=1, lxyzCount=1, squenceCount=0):
        self.xnum = len(x_step_init[0])  # number of parameters
        self.max_iter = args.step # maximum number of iterations
        self.all_finishedFlag = FinishedFlag()
        self.all_freeE = FreeEnergyRecord()
        self.args = args
        self.levelCount = levelCount
        self.lxyzCount = lxyzCount
        self.thetaCount = thetaCount
        self.squenceCount = squenceCount

        self.spacegroup = args.spacegroup # space group number
        self.fixratio = args.fixratio # True or False, cubic space groups will ignore this parameter
        self.cellratio = args.cellratio # Lz = cellratio * Lx , cubic space groups will ignore this parameter
        self.calPlane = args.calPlane # calculate plane for 2d space groups

        self.bo_model = BayesOpt_NoWait(
            x_step=x_step_init, 
            y_step=y_step_init, 
            args=self.args, 
            thetaCount=self.thetaCount, 
            levelCount=self.levelCount, 
            lxyzCount=self.lxyzCount,
            squenceCount=self.squenceCount
            ) 
        self.iter = 0

        self.rootDir = rootDir
        self.stopFlag = False

    def get_next_para(self):
        para_dict = dict()
        if self.stopFlag:
            para_dict['waitTime'] = -1  # tell the worker to stop
            return para_dict
        if self.iter >= self.max_iter:
            para_dict['waitTime'] = -1  # tell the worker to stop
            self.stopFlag = True
            return para_dict
        else:
            self.x_next, self.iter = self.bo_model.suggest_next() # get the next parameter point
            self.all_finishedFlag.new_para_point(self.iter) 
            self.all_freeE.new_para_point(self.iter) 
        

        para_dict['ai'] = self.x_next[0][0:self.args.basis].tolist() # tolist
        if self.thetaCount>0:
            para_dict['theta'] = self.x_next[0][self.args.basis:self.args.basis+self.thetaCount].tolist()
        else:
            para_dict['theta'] = []
        if self.levelCount>0:
            para_dict['level'] = self.x_next[0][self.args.basis+self.thetaCount:self.args.basis+self.thetaCount+self.levelCount].tolist()
        else:
            para_dict['level'] = []
        
        if self.squenceCount==0:
            para_dict['Sequence'] = 0
        elif self.squenceCount==1:
            para_dict['Sequence'] = int(self.x_next[0][-1]) # the last element is the sequence number
        else:
            raise ValueError('squenceCount error')



        if 195<= self.spacegroup <= 230: # Cubic 195-230
            para_dict['lx'] = self.x_next[0][-1-self.squenceCount]
            para_dict['ly'] = self.x_next[0][-1-self.squenceCount]
            para_dict['lz'] = self.x_next[0][-1-self.squenceCount]

        elif 143 <= self.spacegroup <=194: # Trigonal 143-167, Hexagonal 168-194
            if self.fixratio: # if fixratio is True, Lz = cellratio * Lx
                para_dict['lx'] = self.x_next[0][-1-self.squenceCount]
                para_dict['ly'] = para_dict['lx']*np.sqrt(3.0)
                para_dict['lz'] = self.x_next[0][-1-self.squenceCount]*self.cellratio
            else: # if fixratio is False, Lz is also a parameter in the BO model
                para_dict['lx'] = self.x_next[0][-2-self.squenceCount]
                para_dict['ly'] = para_dict['lx']*np.sqrt(3.0)
                para_dict['lz'] = self.x_next[0][-1-self.squenceCount]
        elif 75 <= self.spacegroup <=142: # Tetragonal 75-142
            if self.fixratio: 
                para_dict['lx'] = self.x_next[0][-1-self.squenceCount]
                para_dict['ly'] = para_dict['lx']
                para_dict['lz'] = self.x_next[0][-1-self.squenceCount]*self.cellratio
            else: 
                para_dict['lx'] = self.x_next[0][-2-self.squenceCount]
                para_dict['ly'] = para_dict['lx']
                para_dict['lz'] = self.x_next[0][-1-self.squenceCount]
        elif 310 <= self.spacegroup <= 312: # 2d plane group, p4
            para_dict['lx'] = self.x_next[0][-1-self.squenceCount]
            para_dict['ly'] = para_dict['lx']
            para_dict['lz'] = 1.0
            if self.calPlane == "zy":
                para_dict['lx'], para_dict['lz'] = para_dict['lz'], para_dict['lx']
        elif 313 <= self.spacegroup <= 317: # 2d plane group, p3, p6
            para_dict['lx'] = self.x_next[0][-1-self.squenceCount]
            para_dict['ly'] = para_dict['lx']*np.sqrt(3.0)
            para_dict['lz'] = 1.0
            if self.calPlane == "zy":
                para_dict['lx'], para_dict['lz'] = para_dict['lz'], para_dict['lx']
        else:
            raise ValueError('space group number error!')
        para_dict['iter'] = self.iter
        para_dict['paraDir'] = 'iter{:0>3d}'.format(self.iter)
        para_dict['waitTime'] = 0
        para_dict['rootDir'] = self.rootDir

        return para_dict

    def update_scft_result(self, iter,  freeE_value, update_ai, update_Lxyz, statusCode):
        self.all_freeE.update_freeE(iter,freeE_value) # update the free energy value
        isAllFinished = self.all_finishedFlag.update_flag(iter) 
        if isAllFinished:
            self.bo_model.update_step(freeE_value, iter, update_ai, update_Lxyz,statusCode)
    
    def dump_result(self,filename):
        np.savetxt(filename,np.hstack((self.bo_model.x_step,self.bo_model.y_step)), \
                fmt='%.18e', delimiter=' ', newline='\n', header='header line', \
                footer='', comments='# ', encoding=None)
