#!/usr/bin/python3

import json
import os

process = input("Which operation would you like to do \
\t\nPlease enter 1 to CREATE a new user \
\t\nPlease enter 2 to SEARCH for a user \
\t\nPlease enter 3 to CHANGE phone number \
\t\nPlease enter 4 to DELETE a user \
\t\nPlease enter 5 to LIST all contact \
\n \
_ ")

try:
    with open ('phone_book.json', 'r') as js:
        phoneBook = json.load(js)
except FileNotFoundError:
    print('This application is depended on phone_book.sh script to create phone_book.json file. You need to start this application using that script.')
    
if process == '1':
    name = input('Please enter the name         _ ').strip().capitalize()
    lastName = input('Please enter the last name    _ ').strip().capitalize()
    phone = ''.join([i for i in input('Please enter the phone number _ ') if i.isdigit()])
    phone = f'({phone[:3]}){phone[3:6]}-{phone[6:]}'
    newEntry = {'name': name, 'lastName': lastName, 'phoneNumber': phone}

    duplicate = []
    for person in phoneBook:
        if str(newEntry).split(':')[:3] == str(person).split(':')[:3]:
            duplicate.append(person)
    if duplicate:
        print('You already have record(s) with the same name : ')
        for each in duplicate:
            print(each['name'], each['lastName'], each['phoneNumber'])
        res = input('Do you want to create anyway? [y/n] _ ').strip().lower()
        if res == 'y':
            phoneBook.append(newEntry)
        else: print('Phone Book application ended')
    else: phoneBook.append(newEntry)


    os.remove('phone_book.json')
    with open('phone_book.json', 'w') as pb:
        json.dump(phoneBook, pb, indent = 4)

elif process == '2':
    name = input('Please enter the name _ ').strip().capitalize()
    request = []
    for person in phoneBook:
        if person['name'] == name:
            request.append(person)
    if request:
        for p in request:
            print(p['name'], p['lastName'],': ', p['phoneNumber'])
    else: print('No match found')

elif process == '3':
    name = input('Please enter the name you want to make changes _ ').strip().capitalize()
    request = []
    for person in phoneBook:
        if person['name'] == name:
            request.append(person)
    if len(request) == 1:
        toBeChanged = request[0]
    elif len(request) > 1:
        count = 1
        for p in request:
            print(count, p['name'], p['lastName'],': ', p['phoneNumber'])
            count += 1
        rep = int(input(f'{len(request)} match found. Please enter the number to be deleted _ '))
        toBeChanged = request[rep - 1]
    else: 
        print('No match found')
        exit()

    phone = ''.join([i for i in input('Please enter the phone number _ ') if i.isdigit()])
    phone = f'({phone[:3]}){phone[3:6]}-{phone[6:]}'
    phoneBook[phoneBook.index(toBeChanged)]['phoneNumber'] = phone
   

    os.remove('phone_book.json')
    with open('phone_book.json', 'w') as pb:
        json.dump(phoneBook, pb, indent = 4)

elif process == '4':
    name = input('Please enter the name you want to delete _ ').strip().capitalize()
    request = []
    for person in phoneBook:
        if person['name'] == name:
            request.append(person)
    if len(request) == 1:
        toBeDeleted = request[0]
        phoneBook.remove(toBeDeleted)

    elif len(request) > 1:
        count = 1
        for p in request:
            print(count, p['name'], p['lastName'],': ', p['phoneNumber'])
            count += 1
        rep = int(input(f'{len(request)} match found. Please enter the number to be deleted _ '))
        toBeDeleted = request[rep - 1]
        phoneBook.remove(toBeDeleted)

    else: print('No match found')
    
    os.remove('phone_book.json')
    with open('phone_book.json', 'w') as pb:
        json.dump(phoneBook, pb, indent = 4)

elif process == '5':
    gap1 = max(len(person['name']) for person in phoneBook)
    gap2 = max(len(person['lastName']) for person in phoneBook)
    count = 1
    for person in phoneBook:
        print(f"{count:>1} - {person['name']:<{gap1}} \
{person['lastName']:<{gap2}} :    {person['phoneNumber']}")
        count += 1
    

else:
    print('You did not choose a proper option ! \
    \nPhone Book application ended')