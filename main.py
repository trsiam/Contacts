'''
Contact Book:
 Build a contact book that stores information like names, phone numbers, and email addresses. 
 The user should be able to add, search, and delete contacts.'''

import json
import os
from termcolor import colored

filename = 'data.json'
save = []

def function_load():
    global save
    if os.path.exists(filename):
        try:
            with open(filename,'r') as f:
                save = json.load(f)
        except json.JSONDecodeError:
            print('')
def function_save():
    global save
    with open(filename,'w') as f:
        json.dump(save,f,indent=4)
        print('\n')
        print("Data Saved")
        print('\n')
    what()

def function_contact():
    keys = ['Name','Phone Number','Email']
    global save
    D = {}
    for i in keys:
        value = input(f"Enter {i}--")
        D[i] = value
    save.append(D)
    function_save()
    what()

def function_show():
    global save
    if save == []:
        print('There is No Contact to show')
    else:
        for i in save:
            print(i,"\n")
    print('\n')
    what()

def function_find():
    global save
    temp = str(input('Enter---'))
    for i in save:
        for key in i:
            if temp == i[key]:
                print('\n')
                print(i)
    what()

def function_delete():
    global save
    while True:
        temp = str(input('Enter Name--'))
        if temp.replace(" "," ").isalpha():
            print("")
            break
        else:
            print("Only Input Name")
    for i in save:
        for key in i:
            if temp == i[key]:
                print('\n')
                save.remove(i)
    function_save()
    what()

def what():
    print("\n")
    print(" 1 . Contacts")
    print(" 2 . Add new Contact")
    print(" 3 . Search")
    print(" 4 . Delete Contact")
    print("\n")
    try:
        wh = int(input('What to Do- '))
        if wh == 1:
            print("\n")
            function_show()
        elif wh == 2:
            print("\n")
            function_contact()
        elif wh == 3:
            print("\n")
            function_find()
        elif wh == 4:
            print("\n")
            function_delete()
                
    except:
        print(colored("<------Enter which numbered task you want to do---->",'red'))
    what()
function_load()
what()


