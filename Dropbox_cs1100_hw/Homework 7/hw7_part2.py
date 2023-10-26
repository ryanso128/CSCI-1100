# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 16:26:02 2022

@author: ryani

given year ranges and 2 weights, output the best and worst movie based on user
inputed category

"""

import json

#guard

if __name__ == "__main__":
    
    #opens the imported file
    
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())
    
    #ask users for year ranges, and the 2 weights
    
    min_year=int(input('Min year => ').strip())
    print(min_year)
    max_year=int(input('Max year => ').strip())
    print(max_year)
    w1=input('Weight for IMDB => ').strip()
    print(w1)
    w1=float(w1)
    w2=input('Weight for Twitter => ').strip()
    print(w2)
    w2=float(w2)
    print('\n', end='')
    
    #find whether each movie falls in the year range, whether the movie has a 
    #a twitter rating, and if that exist, whether that rating is more that 2 ratings
    
    valid_movies=[]
    for movie in movies:
        
        #checks if movie is in the year range
        
        if max_year>=movies[movie]['movie_year']>=min_year:
            
            #checks if a twitter rating exist for movie
            
            in_ratings = movie in ratings
            if in_ratings == True:
                
                #checks if twitter rating, if exists, is more than 2
                
                if len(ratings[movie])>=3:
                    avg_twitter=sum(ratings[movie])/len(ratings[movie])
                    imdb_rating=movies[movie]['rating']
                    weighted_rating=(w1 * imdb_rating + w2 * avg_twitter) / (w1 + w2)
                    
                    #appends weighted average and movie info into valid_movies
                    
                    valid_movies.append((weighted_rating, movies[movie]['genre'], movies[movie]['name'], movies[movie]['movie_year']))
    valid_movies.sort(reverse=True)
    
    #asks user what genre they would like to see
    
    genre=input('What genre do you want to see? ').strip()
    print(genre)
    genre=genre.lower()
    
    #loops through all valid movies and finds movies with the same genre. then
    #appends into another list and finds the max and min of that list
    
    while genre!='stop':
        valid_genre=[]
        for valid in valid_movies:
            for genres in valid[1]:
                genres=genres.lower()
                
                #checks if that movie has the same genre as the user input
                #if true, appends into valid_genre
                
                if genres==genre:
                    valid_genre.append(valid)
        
        #if nothing is in the valid_genre list, print back an error message 
        #and loop again
        
        if len(valid_genre)==0:            
            print('\nNo {} movie found in {} through {}'.format(genre.title(), min_year, max_year))
            print('\n', end='')
            
        #otherwise print out the max(best) and min(worst) of the list    
        
        else:
            print('\nBest:\n{}Released in {}, {} has a rating of {:.2f}'.format(' '*8, valid_genre[0][3], valid_genre[0][2], valid_genre[0][0]))
            print('\n', end='')
            print('Worst:\n{}Released in {}, {} has a rating of {:.2f}'.format(' '*8, valid_genre[-1][3], valid_genre[-1][2], valid_genre[-1][0]))
            print('\n', end='')
            
        #ask the user again until the user types stop
        
        genre=input('What genre do you want to see? ').strip()
        print(genre)
        genre=genre.lower()
            
    
    
    
    
    