#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年7月16日

@author: dongquan
'''
from flask import Flask 

app = Flask(__name__) 
app.config.from_object('config')

from app import views