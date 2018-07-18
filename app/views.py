#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年7月16日

@author: dongquan
'''
from app import app  
from flask import render_template,flash, redirect

from forms import LoginForm
 
# index view function suppressed for brevity
 
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', 
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])

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
    
@app.route('/base')
def base():
    user = {'nickname':'dongquan'}
    posts = [
        {
            'author':{'nickname':'chendq'},
            'body':'I like test'},
        {
            'author':{'nickname':'tester'},
            'body':'my name is tester'}
             ]
    return render_template('base.html')
    
    