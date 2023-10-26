# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:10:17 2022

@author: ryani

Print out the very first iteration of the simtuation.

"""
#import the necessary files
import json
from Bear import bear
from BerryField import berry
from Tourist import tourist

#start of the code
if __name__=='__main__':
    
    #ask user for jsonn file
    
    #jsonn=input('Enter the json file name for the simulation => ').strip()
    #print(jsonn)
    #print()
    
    #open jsonn file
    
    #file = open (jsonn)
    file = open("bears_and_berries_1.json")
    data = json.loads(file.read()) 
    
    #for each key in the data dictonary, set it to a list for ease of use
    
    berryfield=data['berry_field']
    active_bears=data['active_bears']
    active_tourist=data['active_tourists']
    reserve_bears=data['reserve_bears']
    reseve_tourist=data['reserve_tourists']
    
    #for each bear in the active bears, put it into the bears class and 
    #append it into a list
    
    bearss=[]
    for bears in active_bears:
        bearss.append(bear(bears[0], bears[1], bears[2]))
    
    #for each tourists in active tourists, put it into the tourists class 
    #and append it into a list
    
    touristss=[]
    for tourists in active_tourist:
        tourists=tourist(tourists[0], tourists[1])
        touristss.append(tourists)
        
    #put the berry field, the bears in the bear class and the tourist in the
    #tourists class into the berry class
    
    berry_field=berry(berryfield, bearss, touristss)
    
    #print out the total berries in the field
    
    berry_field_sum=berry_field.count()
    print('Field has {} berries.'.format(berry_field_sum))
    print(berry_field)
    print('Active Bears:')
    
    #print out each bear
    
    for bears in bearss:
        print(bears)
    print('\n', end='')
    
    #print out each tourists
    
    print('Active Tourists:')    
    for tourists in touristss:
        print(tourists)
    