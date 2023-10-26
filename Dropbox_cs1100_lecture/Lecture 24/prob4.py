
f_list = [ 19.4, 45.8, 25.2, -16, 82.19, 63.6, 45.1 ]
c_list = [(c-32)*(5/9) for c in f_list if c>32]## Solution code goes here
line = ''
for c in c_list:
    line += '{:.2f}'.format(c) + ' '
print(line.strip())
