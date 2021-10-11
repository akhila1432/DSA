from typing import ItemsView


a = ['code','edoc','da','d']
for i ,  item in enumerate(a):
    if item[::-1] == i:
        print(i,i+1)

