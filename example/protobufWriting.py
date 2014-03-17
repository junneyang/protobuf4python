#!/usr/bin/env python
#-*- coding: utf-8 -*-
import addressbook_pb2
filepath=u'./addressbook.db'

#数据构造
addressbook=addressbook_pb2.AddressBook()
for item in xrange(0,10):
    person=addressbook.person.add()
    person.id=1234+item
    person.name="John Doe"+str(item)
    person.email="jdoe@example.com"+str(item)
    phone=person.phone.add()
    phone.number="555-4321"+str(item)
    phone.type=addressbook_pb2.Person.HOME

#写入到文件
f=open(filepath,"wb")
f.write(addressbook.SerializeToString())
f.close()

