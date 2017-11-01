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
#      Description:
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

# Connect to the database
connection = pymysql.connect(**config)

# Show all tables
cursor=connection.cursor()
cursor.execute("show tables;")
result = cursor.fetchall()
connection.commit()
for i in result: print(i.values())

# Show all lines in a table
cursor = connection.cursor()
cursor.execute("select * from t_cif_bank;")
result = cursor.fetchall()
connection.commit()
print(result[0].keys())
for i in result: print(i.values())

cursor.close()
connection.close()
