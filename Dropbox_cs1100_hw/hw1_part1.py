# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 17:12:57 2022

@author: ryani

Asks user to input names, nouns, verbs, adjectives, etc., and create a
pre-generated Mad Lib.
"""
print('Let\'s play Mad Libs for Homework 1')
print('Type one word responses to the following:')
print(' ', '\n', sep='', end='')
proper_name=input('proper_name ==> ').strip()
print(proper_name)
adjective1=input('adjective ==> ').strip()
print(adjective1)
noun1=input('noun ==> ').strip()
print(noun1)
verb1=input('verb ==> ').strip()
print(verb1)
verb2=input('verb ==> ').strip()
print(verb2)
noun2=input('noun ==> ').strip()
print(noun2)
emotion1=input('emotion ==> ').strip()
print(emotion1)
verb3=input('verb ==> ').strip()
print(verb3)
noun3=input('noun ==> ').strip()
print(noun3)
season=input('season ==> ').strip()
print(season)
adjective2=input('adjective ==> ').strip()
print(adjective2)
emotion2=input('emotion ==> ').strip()
print(emotion2)
team_name=input('team-name ==> ').strip()
print(team_name)
noun4=input('noun ==> ').strip()
print(noun4)
adjective3=input('adjective ==> ').strip()
print(adjective3)

print("\nHere is your Mad Lib...\n\nGood morning {}!\n".format(proper_name))
print('\tThis will be a/an {} {}! Are you {} forward to it?'.format(adjective1, noun1, verb1))
print('\tYou will {} a lot of {} and feel {} when you do.'.format(verb2, noun2, emotion1))
print('\tIf you do not, you will {} this {}.\n'.format(verb3, noun3))
print('\tThis {} was {}. Were you {} when {} won\n\tthe {}?\n'.format(season, adjective2, emotion2, team_name, noun4))
print('\tHave a/an {} day!'.format(adjective3))