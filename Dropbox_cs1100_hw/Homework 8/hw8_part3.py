# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:10:17 2022

@author: ryani

Instead of running the simulation for 5 turns, print the simulation every 5
turns and when all bears and tourists have left

"""

#import all necessary files

import json
from Bear import bear
from BerryField import berry
from Tourist import tourist

#start of code

if __name__=='__main__':
    
    #ask user for jsonn file
    
    # jsonn=input('Enter the json file name for the simulation => ').strip()
    # print(jsonn)
    # print()
    
    #open jsonn file
    
    #file = open (jsonn)
    file = open("bears_and_berries_1.json")
    data = json.loads(file.read())   
    
    #for all the data in the data dictionary, put it into a variable for ease 
    #of access
    
    berryfield=data['berry_field']
    active_bears=data['active_bears']
    active_tourist=data['active_tourists']
    reserve_bears=data['reserve_bears']
    reserve_tourists=data['reserve_tourists']
    
    
    #for all the active bears, put it into the bear class and append into bearss
    
    bearss=[]
    for bears in active_bears:
        bearss.append(bear(bears[0], bears[1], bears[2]))
    
    #for all active_tourists, put it into the tourist class and append into touristss
    
    touristss=[]
    for tourists in active_tourist:
        tourists=tourist(tourists[0], tourists[1])
        touristss.append(tourists)
    
    #for all reserve bears, put into bears class and append into reserve_bearss 
    
    reserve_bearss=[]
    for bears in reserve_bears:
        reserve_bearss.append(bear(bears[0], bears[1], bears[2]))
    
    #for all reserve tourists, put into tourist class and append into reserve_tourists
    
    reserve_touristss=[]
    for tourists in reserve_tourists:
        reserve_touristss.append(tourist(tourists[0], tourists[1]))
        
    #start of part 1
    
    print('Starting Configuration')
    
    #put berry field, bearss and touristss into the berry class
    
    berry_field=berry(berryfield, bearss, touristss)
    
    #print out the total berries
    
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
        
    #a second while loop for printing every 5 turns or until no more bears and 
    #tourists exist
    
    l=0
    while (len(bearss)>0 and len(reserve_bearss)>0) or (len(bearss)>0 and berry_field.count()>0):
        #part 2
        i=0
        while i<5 and ((len(bearss)>0 or len(reserve_bearss)>0) and (len(bearss)>0 or berry_field.count()>0)):
            
            #print out the turns
            
            print()
            print('Turn: {}'.format(l+i+1))
            
            #grow the berries
            
            berry_field.growing()
            ded_tourists=[]
            gone_bears=[]
            
            #check if each bear is asleep or awake
            
            for bears in bearss:
                if bears.sleep_turns>0:
                    bears.sleep_turns-=1
                    if bears.sleep_turns==0:
                        pass
                    else:
                        continue
                else:
                    bears.sleep=False
                
                #check if the bears and tourists location are the same. if true,
                #append it to ded_tourists list and put bear to sleep
                
                for tourists in touristss:
                    if bears.x==tourists.x and bears.y==tourists.y:
                        ded_tourists.append(tourists)
                        bears.sleep=True
                        bears.sleep_turns+=2
            
            #moving, eating and checking if location of bears and tourists are 
            #the same
            
            k=0
            while k<len(bearss):
                berry_count=0
                
                #add 1 to the berry count and subtract 1 from the berry field
                #of the bear's location
                
                while berry_count<30 and bearss[k].sleep==False:
                    while berry_field.field[bearss[k].x][bearss[k].y]>0 and berry_count<30:
                        berry_count+=1
                        berry_field.field[bearss[k].x][bearss[k].y]-=1
                    
                    #move the bear
                    
                    if berry_count<30:
                        bearss[k].moving()
                        
                        #check if the tourists and the bears's location are the same
                        #if true, append tourists into ded_tourists and put bear to sleep
                        
                        for tourists in touristss:
                            if bearss[k].x==tourists.x and bearss[k].y==tourists.y and tourists not in ded_tourists:
                                ded_tourists.append(tourists)
                                bears.sleep=True
                                bears.sleep_turns+=2
                                break
                    
                    #if the bear is out of bounds, append bear into gone_bears
                    
                    if 0>bearss[k].x or bearss[k].x>=len(berry_field.field) or 0>bearss[k].y or bearss[k].y>=len(berry_field.field[0]):
                        gone_bears.append(bearss[k])
                        break
                k+=1
            
            
            
            for tourists in touristss:
                tourists.bear_num=0
                
                #count the number of bears for each tourist around them
                
                for bears in bearss:
                    if ((tourists.x-bears.x)**2+(tourists.y-bears.y)**2)**0.5<=4:
                        tourists.bear_num+=1
                        tourists.bears_turns=0
                
                #if the number of bears is 3 or more, append it to ded_tourists
                
                if tourists.bear_num>=3 and tourists not in ded_tourists:
                    ded_tourists.append(tourists)
                
                #if there are no bears around, add 1 to bear_turns
                
                if tourists.bear_num==0:
                    tourists.bear_turns+=1
                    
                #if bear_turns is 3, it gets boring. append tourists into 
                #ded_tourists
                
                if tourists.bear_turns>=3 and tourists not in ded_tourists:
                    ded_tourists.append(tourists)
            
            #for each bear in gone_bears, print it has left and remove it from bearss
            
            if len(gone_bears)>0:
                for missing_bears in gone_bears:
                    print('Bear at ({},{}) moving {} - Left the Field'\
                                  .format(missing_bears.x, missing_bears.y, missing_bears.direction))
                    bearss.remove(missing_bears)
            
            #for each tourists in ded_tourists, remove it from the touristss list
            
            if len(ded_tourists)>0:
                for gone_tourists in ded_tourists:
                    print('Tourist at ({},{}), {} turns without seeing a bear. - Left the Field'\
                        .format(gone_tourists.x, gone_tourists.y, gone_tourists.bear_turns))
                    touristss.remove(gone_tourists)
            
            #if the berry field has 500 berries and there are still reserve_bears, 
            #put the bear into the bearss list
            
            if berry_field.count()>=500 and len(reserve_bearss)!=0:
                print('Bear at ({},{}) moving {} - Entered the Field'\
                      .format(reserve_bearss[0].x, reserve_bearss[0].y, reserve_bearss[0].direction))
                bearss.append(reserve_bearss[0])
                del reserve_bearss[0]
            
            #if there are bearss on the field and there are still reserve tourists,
            #put the reserve tourists into touristss
            
            if len(bearss)>0 and len(reserve_touristss)!=0:
                print('Tourist at ({},{}), {} turns without seeing a bear. - Entered the Field'\
                      .format(reserve_touristss[0].x, reserve_touristss[0].y, reserve_touristss[0].bear_turns))
                touristss.append(reserve_touristss[0])
                del reserve_touristss[0]
            i+=1
        
        #after 5 turns have gone by, print the number of berries, the berry_field
        #and the locations and status of the bears and tourists
        #loop until no mroe bears and tourists
        
        print('Field has {} berries.'.format(berry_field.count()))
        print(berry_field)
        print('Active Bears:')
        for bears in bearss:
            print(bears)
        print()
        print('Active Tourists:')
        for tourists in touristss:
            print(tourists)
        print()    
        l+=5