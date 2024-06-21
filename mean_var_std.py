import numpy as np

def find_stats_flattened(input_arr):
    mean = input_arr.mean()
    variance = input_arr.var()
    std = input_arr.std()
    max = input_arr.max()
    min = input_arr.min()
    sum = input_arr.sum()
    
    return [mean,variance,std,max,min,sum]

def find_stats(input_arr):
    mean_arr = []
    variance_arr = []
    std_arr = []
    max_arr = []
    min_arr = []
    sum_arr = []
    
    for index, elem in enumerate(input_arr):

        mean_arr.append(elem.mean())
        variance_arr.append(elem.var())
        std_arr.append(elem.std())
        max_arr.append(elem.max())
        min_arr.append(elem.min())
        sum_arr.append(elem.sum())
        
    return [mean_arr, variance_arr, std_arr, max_arr, min_arr, sum_arr]


def calculate(list):
    #raise Value Error if list contains less than 9 elements
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    #create numpy array with list
    arr = np.array(list)
    
    #find stats for flattened array
    flattened = find_stats_flattened(arr)
    
    #convert array to 3x3
    arr = arr.reshape(3,3)
    
    #find stats for rows
    axis2 = find_stats(arr)
    
    #transpose array
    arr = np.transpose(arr)
    
    #find stats for columns
    axis1 = find_stats(arr)
        
    mean = [axis1[0], axis2[0], flattened[0]]
    variance = [axis1[1], axis2[1], flattened[1]]
    std = [axis1[2], axis2[2], flattened[2]]
    max = [axis1[3], axis2[3], flattened[3]]
    min = [axis1[4], axis2[4], flattened[4]]
    sum = [axis1[5], axis2[5], flattened[5]]
    
    computations = {'mean' : mean,
                    'variance' : variance,
                    'standard deviation' : std,
                    'max' : max,
                    'min' : min,
                    'sum' : sum}

    return computations


list1 = [2,6,2,8,4,0,1,5,7]
print(calculate(list1))