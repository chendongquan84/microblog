#!flask/bin/python 
# -*- coding: utf-8 -*-
'''
Created on 2018年7月16日

@author: dongquan
'''

from app import app
app.run(debug = True,host='0.0.0.0',port='8080')