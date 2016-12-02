# -*- coding: utf-8 -*-
__author__ = 'Nil'
from DAdbCommon import *
# 检查设备是否存在
def attached_devices():
   return AndroidDebugBridge().attached_devices()

def open_app(packagename,activity):
    return AndroidDebugBridge().open_app(packagename, activity)