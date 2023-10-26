# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:10:17 2022

@author: ryani

Prints the first 5 iterations of the simulation. Berries grow, bears eat 
berries and move, and tourists watch bears and dissapear when they meet a bear.

"""
#import the necessary files
import json
from Bear import bear
from BerryField import berry
from Tourist import tourist

#start of the code
if __name__=='__main__':
    
    #ask user for jsonn file
    
    jsonn=input('Enter the json file name for the simulation => ').strip()
    print(jsonn)
    print()
    
    #open jsonn file
    
    file = open (jsonn)
    # file = open("bears_and_berries_1.json")
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
        
    #the hw part 1
    
    print('Starting Configuration')
    
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
    
    #start of the simulation
    
    i=0
    while i<5:
        
        #print out hte turns
        
        print()
        print('Turn: {}'.format(i+1))
        
        #grow the berries
        
        berry_field.growing()
        ded_tourists=[]
        gone_bears=[]
        
        #check if each bear is sleep or awake.
        
        for bears in bearss:
            if bears.sleep_turns>0:
                bears.sleep_turns-=1
                if bears.sleep_turns==0:
                    pass
                else:
                    continue
            else:
                bears.sleep=False
            
            #check if the location of each bear is the same as each tourists.
            #if that is true, append the tourist into the ded_toursits list
            #and put the bear to sleep
            
            for tourists in touristss:
                if bears.x==tourists.x and bears.y==tourists.y:
                    ded_tourists.append(tourists)
                    bears.sleep=True
                    bears.sleep_turns+=2
        
        #move the bears while eating and checking if the location is the same
        #as a tourist
        
        k=0
        while k<len(bearss):
            berry_count=0
            
            #I add 1 to the berry_count, subtract a berry on the bear's location
            #until the berrys are gone.
            
            while berry_count<30 and bearss[k].sleep==False:
                while berry_field.field[bearss[k].x][bearss[k].y]>0 and berry_count<30:
                    berry_count+=1
                    berry_field.field[bearss[k].x][bearss[k].y]-=1
                
                #then I move the bear.
                
                if berry_count<30:
                    bearss[k].moving()
                    
                    #then i if the locations of the bear and tourist match
                    
                    for tourists in touristss:
                        if bearss[k].x==tourists.x and bearss[k].y==tourists.y and tourists not in ded_tourists:
                            
                            # if true, append tourists into ded_tourists
                            #put bear to sleep
                            
                            ded_tourists.append(tourists)
                            bears.sleep=True
                            bears.sleep_turns+=2
                            break
                
                #if the bear moves out of bounds, break the loop and append
                #the bear into the gone_bears list
                
                if 0>bearss[k].x or bearss[k].x>=len(berry_field.field) or 0>bearss[k].y or bearss[k].y>=len(berry_field.field[0]):
                    gone_bears.append(bearss[k])
                    break
            k+=1
        
        #for each tourists, check if there are any bears around.
        
        for tourists in touristss:
            tourists.bear_num=0
            
            #for each tourist, check the number of bears around in a 4 tile
            #radius
            
            for bears in bearss:
                if ((tourists.x-bears.x)**2+(tourists.y-bears.y)**2)**0.5<=4:
                    tourists.bear_num+=1
                    tourists.bears_turns=0
            
            #if the number of bears is 3 or more and the tourists isn't already
            #dead, append it into the ded_tourists list
            
            if tourists.bear_num>=3 and tourists not in ded_tourists:
                ded_tourists.append(tourists)
            
            #if there are no bears around the tourists, add 1 to the 
            #bear_turns counter
            
            if tourists.bear_num==0:
                tourists.bear_turns+=1
                
            #if there are no bears around the toursits for 3 turns, it gets 
            #bored and goes away, appending it to ded_tourists
            
            if tourists.bear_turns>=3:
                ded_tourists.append(tourists)
        
        #for each bear in the gone_bears, print it has left the field and 
        #delete it form the bearss list of classes.
        
        if len(gone_bears)>0:
            for missing_bears in gone_bears:
                print('Bear at ({},{}) moving {} - Left the Field'\
                              .format(missing_bears.x, missing_bears.y, missing_bears.direction))
                bearss.remove(missing_bears)
        
        #for each tourists in ded_tourists, print it has left the field and 
        #delete it from the touristss list of classes.
        
        if len(ded_tourists)>0:
            for gone_tourists in ded_tourists:
                print('Tourist at ({},{}), {} turns without seeing a bear. - Left the Field'\
                    .format(gone_tourists.x, gone_tourists.y, gone_tourists.bear_turns))
                touristss.remove(gone_tourists)
        
        #after all the bear moving and tourists moving, print the number of
        #berries
        
        print('Field has {} berries.'.format(berry_field.count()))
        
        #print berry field
        
        print(berry_field)
        
        #print the bears that haven't left yet
        
        print('Active Bears:')
        for bears in bearss:
            print(bears)
        print()
        
        #print the tourists that haven't left yet
        
        print('Active Tourists:')
        for tourists in touristss:
            print(tourists)
        print()
        i+=1
                   