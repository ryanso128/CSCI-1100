
points = [ (4,2), (1,-3), (-4, -6), (6,9), (3,8), (-5,2), (6,2) ]
min_x = min(map( lambda y: y[0], list(filter( lambda x: x[0]>0 and x[1]>0, points))))## Solution goes here
print(min_x)
