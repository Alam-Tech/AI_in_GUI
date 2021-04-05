from math import sqrt,log
import numpy as np

class Agent():
    
    def __init__(self,limit_val):
        self.no_of_apps = 0
        self.reward_tray = []
        self.no_of_times_displayed = []
        self.reward = 1
        self.no_of_updates = 0
        self.previous_n_choices = []
        self.limit = limit_val
    
    def get_priority_list(self):
        """
        This is fucntion return the priority list on calling.
        """
        if self.no_of_updates < self.limit:
            target_list = list(range(0,self.no_of_apps))
        else:
            if self.limit == 1:
                target = -1
                max_upper_bound = 0
                for i in range(self.no_of_apps):
                    upper_bound = self.__calc_upper_bound(i)        
                    if upper_bound > max_upper_bound:
                        max_upper_bound = upper_bound
                        target = i
                target_list = [target]
            else:
                ub_list = [self.__calc_upper_bound(i) for i in range(self.no_of_apps)]
                ub_list = np.array(ub_list).reshape(-1,1)
                num_list = np.arange(0,self.no_of_apps,1).reshape(-1,1)
                ub_list = np.concatenate((num_list,ub_list),axis=1)
                ub_list = ub_list[ub_list[:,1].argsort()[::-1],:]
                
                target_list = list(map(int,ub_list[:self.limit,0]))
                
        for i in target_list:
            self.no_of_times_displayed[i] += 1
        self.previous_n_choices = target_list
        self.no_of_updates += 1
        return target_list
        
    def add_app(self):
        """
        This function is to add a new record for the newly added app in the tray.
        """
        self.reward_tray.append(0)
        self.no_of_times_displayed.append(0)
        self.no_of_apps += 1
        
    def delete_app(self,target_index):
        """
        This function is to delete all the records of an existing app.
        """
        del self.reward_tray[target_index]
        del self.no_of_times_displayed[target_index]
        self.no_of_apps -= 1
    
    def __calc_upper_bound(self,i):
        if self.no_of_times_displayed[i] == 0:
            return 1e400
        r_i = self.reward_tray[i] / self.no_of_times_displayed[i]
        delta_i =  sqrt( (3*log(self.no_of_updates+1)) / (2*self.no_of_times_displayed[i]) )
        return r_i + delta_i
        
    def update(self,target_index):
        """
        This function recieves the target index of the selected app,
        makes the appropriate updation.
        """
        if target_index in self.previous_n_choices:
            self.reward_tray[target_index] += self.reward