list_of_nums = list(map(int, input('Enter integers separated by spaces: ').split()))

def max_min_dif(list_of_nums):
    maximum =list_of_nums[0]
    minimum=list_of_nums[0]
    for value in list_of_nums:
        if maximum < value:
            maximum = value
        if minimum > value:
             minimum = value
    return maximum-minimum
    
print(max_min_dif( list_of_nums)) 
