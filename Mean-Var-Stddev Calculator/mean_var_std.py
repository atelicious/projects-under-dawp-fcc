#This is my solution to the Mean-Variance-Standard Deviation Calculator Problem in FCC's Data Analysis with Python.
#You can view the original question and my repl solution @ https://repl.it/@atelicious/FCC-mean-variance-standard-deviation-calculator

import numpy as np

def calculate(array_list):

  if len(array_list) < 9:

      raise ValueError('List must contain nine numbers.')

  else:

      # This inititates the lists that will serve as the keys of the returned dictionary
      mean_list = []
      variance_list = []
      std_dev_list = []
      max_nums_list = []
      min_nums_list = []
      summation_list = []

      # This is the list that will be converted in a 3x3 numpy array matrix

      reshaped_array_list = np.array(array_list).reshape(3, 3)

      # Because we only need the statistical values for 2 axes, we only need to loop twice
      # to get the values, and append it to its respective list
      for i in range(0, 2):

          axis_mean = list(np.mean(reshaped_array_list, axis = i))
          mean_list.append(axis_mean)

          axis_var = list(np.var(reshaped_array_list, axis = i))
          variance_list.append(axis_var)

          axis_std_dev = list(np.std(reshaped_array_list, axis = i))
          std_dev_list.append(axis_std_dev)

          axis_max_nums = list(np.max(reshaped_array_list, axis = i))
          max_nums_list.append(axis_max_nums)

          axis_min_nums = list(np.min(reshaped_array_list, axis = i))
          min_nums_list.append(axis_min_nums)

          axis_sum = list(np.sum(reshaped_array_list, axis = i))
          summation_list.append(axis_sum)

      #This block will append the statiscial values for the flattened array list

      mean_list.append(np.mean(reshaped_array_list))
      variance_list.append(np.var(reshaped_array_list))
      std_dev_list.append(np.std(reshaped_array_list))
      max_nums_list.append(np.max(reshaped_array_list))
      min_nums_list.append(np.min(reshaped_array_list))
      summation_list.append(np.sum(reshaped_array_list))

      #Building the return value disctionary

      calculations = {'mean':mean_list,
                      'variance':variance_list,
                      'standard deviation':std_dev_list,
                      'max':max_nums_list,
                      'min':min_nums_list,
                      'sum':summation_list
                    }

      return calculations