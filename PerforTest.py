#!/usr/bin/python
#-*- coding: utf-8 -*-
#2016.11.30
__author__='Nil'
import Bphone
import re
import Globals as go
import Operatefile
import os
import BAdbCommon
import MMonkeyConfig
import BMonkeyConfig
import Dphone

#获得错误信息
def get_error(log):
    cp = open(log,'r')
    lines=cp.readline()
    for line in lines:
        if re.findall(go.ANR,line):
            print("存在ANR错误:"+line)
            go.I_ANR +=1
        if re.findall(go.CRASH,line):
            print("存在crash错误"+line)
            go.I_CRASH +=1
        if re.findall(go.EXCEPTION,line):
            print("存在exception异常"+line)
            go.I_EXCEPTION +=1
        if go.I_ANR == 0 and go.I_CRASH==0 and go.I_EXCEPTION==0:
            print("成功,没有错误")

#获取手机信息
def get_phone(phonelog):
    bg = Dphone.getPhone('/Users/admin/Documents/autotest/log.txt').get_phone_Kernel()
    logname = phonelog + "_" + bg[0]["phone_model"]+bg[0]["phone_name"]+bg[0]["release"]+".txt"
    of = Operatefile.base_file(logname,"w+")
    if of.mkdir_file():
        result = "手机型号：" + bg[0]["phone_name"] + "\n"
        result += "手机名字：" + bg[0]["phone_model"] + "\n"
        result += "系统版本：" + bg[0]["release"] + "\n"
        result += "手机分辨率：" + bg[3] + "\n"
        result += "手机运行内存：" + bg[1] + "\n"
        result += "CPU核数：" + bg[2] + "\n"
        of.write_txt(result)

#脚本测试
def start_monkey(cmd,logdir,now1):

    #Monkey测试结果日志:monkey_log
    os.popen(cmd)
    print(cmd)

    #Monkey时手机日志,logcat
    logcatname= logdir+"/"+"logcat.log"
    cmd2 = "adb logcat -d >%s" %(logcatname)
    os.popen(cmd2)

if __name__ =='__main__':
    ini_file = 'monkey.ini'
    ba = BAdbCommon
    if Operatefile.base_file(ini_file,"r").check_file():
        if ba.attached_devices():
            mconfig = MMonkeyConfig.monkeyconfig()
            mc = BMonkeyConfig.monkeyConfig(mconfig,ini_file)
            #打开想要的activity
            # ba.open_app(mc.package_name,mc.activity)
            temp=""
            #开始monkey测试
            start_monkey(mc.cmd,mc.logdir,mc.now)
            while True:
                with open(mc.monkey_log,'r') as monkeylog:
                    if monkeylog.read().count('Monkey finished')> 0:
                        print("测试完成诺")
                        get_error(mc.monkey_log)
                        get_phone(mc.phone_msg_log)
                        break
        else:
            print("设备不存在")
    else:
        print(u"配置文件不存在"+ini_file)
