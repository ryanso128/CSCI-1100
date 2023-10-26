""" 
    This is the skeleton to demonstrate how to put Lab 10 together. 
    It provides an example to show the use of doctest. Note the function,
    addone(x) presented below has an additional 4 lines after 
    the normal function description. The lines beginning with '>>>'
    indicate examples of how the function can be called, and 
    the lines immediately after represent the expected return
    from the call. So, for example, 'addone(1)' should return '2'
    and 'addone(0) should return 1. These lines provide examples
    for a potential user of the lab10 module, but more importantly
    for this lab, they work with the doctest module to allow us to
    do automated testing. 
    
    Look at the file 'test_driver.py' for an example of how to use
    this testing information. Then come back here and change 
    the answer for one or both of the addone examples to 
    an incorrect value and run the testing again to see how a failing
    test is reported.
"""

# def addone(x):
#     '''
#     addone(x) returns 1 more than
#     the value x passed in.

#     >>> addone(1)
#     2
#     >>> addone(0)
#     1
#     '''
#     return x+1

import random
import time

def closest1(L1):    
    '''

    >>> closest1([ ])
    (None, None)
    '''

    if len(L1)<2:
        return (None, None)
    min_distance=max(L1)
    for values1 in L1:
        for values2 in L1:
            distance=abs(values1-values2)
            if distance!=0:
                if distance<min_distance:
                    min_distance=distance
                    least=sorted((values1, values2), reverse=True)
    return tuple(least)

def closest2(L1):
    '''
    L1 : [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
    >>> closest2([ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ])
    (5.4, 4.3)

    '''
    if len(L1)<2:
        return(None, None)
    L1=sorted(L1)
    minn=dict()
    for num in range(len(L1)-1):
        minn[abs(L1[num]-L1[num+1])]=tuple(sorted((L1[num], L1[num+1]), reverse=True))
    return minn[min(minn)]

if __name__ == "__main__":
    num_values=int(input('How many values do you want? '))
    values=[]
    for number in range(num_values):
        values.append(random.uniform(0.0, 1000.0))
    
    s1=time.time()
    (x1, y1)=closest1(values)
    e1=time.time()-s1
    print(x1, y1, e1)
    
    s2=time.time()
    (x2, y2)=closest2(values)
    e2=time.time()-s2
    print(x2, y2, e2)
    
    pass
