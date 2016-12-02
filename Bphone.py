#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Nil'
import  Dphone

class getPhone():
    def __init__(self,log):
        self.log =log
        self.gp = Dphone.getPhone(self,log)

    def get_phone_Kernel(self):
        return self.gp.get_cpu_kel()