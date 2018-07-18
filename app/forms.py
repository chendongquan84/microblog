#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年7月17日

@author: dongquan
'''
from flask_wtf import Form
from wtforms import TextField,BooleanField
from wtforms.validators import Required
 
class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)
    
