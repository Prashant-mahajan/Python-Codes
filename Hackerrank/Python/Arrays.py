import numpy

def arrays(arr):
    # complete this function
    # use numpy.array 
    b = numpy.array(numpy.flip(arr,0),float)
    return(b)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)