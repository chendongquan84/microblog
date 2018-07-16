#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年7月16日

@author: dongquan
'''
from app import app 
from flask import render_template

@app.route('/') 
@app.route('/index') 
def index():
    user = { 'nickname': 'chendq' }
    posts = [
        {
            'author':{'nickname':'john'},
            'body':'Beautiful day in'
        },
        {
            'author':{'nickname':'chendq'},
            'body':'the aengers movie wacth'
        }
    ]
    return render_template('index.html',
                           title='chendq',
                           user=user,
                           posts = posts )
    
    