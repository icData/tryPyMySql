#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

#  ==============================================
#
#      Author: Maoji Wang
#
#      maoji.wang@cs.nyu.edu
#
#      Filename: pymysql_connect.py
#
#      COPYRIGHT 2017
#
#      All rights reserved
#
#  ==============================================

import pymysql.cursors

# Setup connector with dict
config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'',
          'db':'jingle_db_base',
          'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.DictCursor,
          }

# Connect to a database
connection = pymysql.connect(**config)

# Show all tables of the database
cursor = connection.cursor()
cursor.execute("show tables;")
result = cursor.fetchall()
connection.commit()
for i in result: print(i.values())

# Show all col-attributes of a table
cursor.execute("desc t_cif_bank;")
result = cursor.fetchall()
connection.commit()
print(result[0].keys())
for i in result: print(i.values())

# Show all lines in a table
cursor.execute("select * from t_cif_bank;")
result = cursor.fetchall()
connection.commit()
print(result[0].keys())
for i in result: print(i.values())

# Get a col from a table
cursor.execute("select * from t_cif_bank;")
result = cursor.fetchall()
connection.commit()
print(result[0].keys())
# for i in result: print(list(i.values())[4])
x = [list(i.values())[4] for i in result]
#        ^--- got the dict value of each result line;
#             then convert it to list, and
#             pick the 4-th elem.  Lastly,
#             rearrange them back to another list.
print('the 4-th col is:', x)

# Get a certain col from a table --- a better way:
this_attr = 'bankCode'
cursor.execute("select %s from t_cif_bank;"%this_attr)
result = cursor.fetchall()
connection.commit()
print(result[0].keys())
# for i in result: print(list(i.values())[0])
x = [list(i.values())[0] for i in result]
#  same with the above group, only that, it is always 0 nowhere
print('the %s col is:'%this_attr, x)

cursor.close()
connection.close()
