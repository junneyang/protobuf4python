#!/usr/bin/env python
#-*- coding: utf-8 -*-
import addressbook_pb2
filepath=u'./addressbook.db'

addressbook=addressbook_pb2.AddressBook()

#文件读取解析
f=open(filepath,"rb")
addressbook.ParseFromString(f.read())
f.close()

#print(addressbook)

for index,person in enumerate(addressbook.person):
    print('*'*30)
    print(index)
    print(person.id)
    print(person.name)
    if(person.HasField("email")):
        print(person.email)
    for phone in person.phone:
        print(phone.number)
        if(phone.type==addressbook_pb2.Person.MOBILE):
            print('MOBILE')
        elif(phone.type==addressbook_pb2.Person.HOME):
            print('HOME')
        elif(phone.type==addressbook_pb2.Person.WORK):
            print('WORK')
    print('*'*30)

