#!/bin/bash
sudo echo "Welcome $USER" 2> /dev/null

if [ $? != 0 ];
then
    echo "You are not authorized to switch to root"
fi

[ -e ./AccessLog.txt ] || touch AccessLog.txt

record=$( tail -n 1 AccessLog.txt | cut -d' ' -f1 )

echo "$(( record += 1 )) - $USER $( date +"%Y-%m-%d %T")" >> AccessLog.txt

 
type python3 1> /dev/null || sudo yum install -y python3

[ -e  $( which python3 ) ] && \
echo
echo "python binaries exist" || \
PATH=$PATH:/usr/bin/

[ -e ./phone_book.json ] || echo '[
    {
        "name": "John",
        "lastName": "Smith",
        "phoneNumber": "(555)632-9696"
    },
    {
        "name": "Jane",
        "lastName": "Doe",
        "phoneNumber": "(555)523-1214"
    },
    {
        "name": "John",
        "lastName": "Doe",
        "phoneNumber": "(555)236-5474"
    }
]' > phone_book.json

[ -e phone_book.py ] || wget -L https://raw.github.com/talha-01/python-projects/python-01-phonebook-application/phone_book.py
echo
python3 phone_book.py