#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Nil'
import configparser
import time
def monkeyConfig(mmonkeyconfig,init_file):
    config = configparser.ConfigParser()
    config.read(init_file)
    mmonkeyconfig.package_name = config['DEFAULT']['package_name']
    mmonkeyconfig.logdir = config['DEFAULT']['logdir']
    mmonkeyconfig.remote_path = config['DEFAULT']['logdir']
    mmonkeyconfig.now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    mmonkeyconfig.activity = config['DEFAULT']['activity']
    mmonkeyconfig.sum = int(config['DEFAULT']['sum'])
    mmonkeyconfig.monkey_log = mmonkeyconfig.logdir + "/" + "monkey.log"
    mmonkeyconfig.cmd = config['DEFAULT']['cmd'] + " " + str(mmonkeyconfig.sum) + ">>" + mmonkeyconfig.monkey_log
    mmonkeyconfig.phone_msg_log = mmonkeyconfig.logdir + "/" +"log.txt"
    return mmonkeyconfig
