#write a python program for a simple reflex agent. first create an env of 5x5 matrix populated by hyphens and randomly placed cross marks. search through for the cross marks and clean them by replacing them with hyphens.
#print no of replaced items
import random
matenv = []
count = 0
items = ['-', 'x']
for i in range(5):
    for j in range(5):
        matenv.append(random.choice(items))
#print env before cleaning
print(matenv)
#search env for crosses
for i in range(5):
    for j in range(5):
        if matenv[i][j]=='x':
            #replace crosses with hyphens
            matenv[i][j]=='-'
            count+=1
print("Cleaned env:")
print(matenv)
#print no of replaced items
print("No of crosses cleaned: ", count)
