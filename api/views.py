# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import JsonResponse

import subprocess
import sys
import os
import psutil
import signal
import yaml
# Create your views here.
#---------------------------------------------------------------------------------------
def startTesting(request):
    try:
        os.environ['TEST_PATH']
    except:
        with open('settings.yml', 'r') as outfile:
            stngs = yaml.load(outfile)
            os.environ["TEST_PATH"] = str(stngs["TestPath"])
            print "Path updated!"
    
    try:
        pid_file = 'process.pid'
        f = open(pid_file,'r')
        pid_number = f.readline()
        if (not psutil.pid_exists(int(pid_number))) or (psutil.Process(pid_number).status() == psutil.STATUS_ZOMBIE):
            app = os.path.join(os.path.dirname(os.path.realpath(__file__)),"startTesting.py")
            pid = subprocess.Popen([sys.executable, app]).pid
            # print pid
            f = open(pid_file,'w')
            f.write(str(pid))
            f.close
            content = {"Status":"Starting"}
        else:
            content = {"Status":"Already started"}

    except:
        pid_file = 'process.pid'
        app = os.path.join(os.path.dirname(os.path.realpath(__file__)),"startTesting.py")
        pid = subprocess.Popen([sys.executable, app]).pid
        f = open(pid_file,'w')
        f.write(str(pid))
        f.close
        content = {"Status":"Starting"} 
    
    return JsonResponse(content)
#---------------------------------------------------------------------------------------
def testStatus(request):
    try:
        os.environ['TEST_PATH']
    except:
        with open('settings.yml', 'r') as outfile:
            stngs = yaml.load(outfile)
            os.environ["TEST_PATH"] = str(stngs["TestPath"])
            print "Path updated!"
    try:
        pid_file = 'process.pid'
        f = open(pid_file,'r')
        pid_number = f.readline()
        if psutil.pid_exists(int(pid_number)):

            content = {"Status":"Started", "PID":pid_number}
        else:
            content = {"Status": "Not running"}
    except:
        content = {"Status": "Error"}

    return JsonResponse(content)
#---------------------------------------------------------------------------------------
def testKill(request):
    try:
        os.environ['TEST_PATH']
    except:
        with open('settings.yml', 'r') as outfile:
            stngs = yaml.load(outfile)
            os.environ["TEST_PATH"] = str(stngs["TestPath"])
            print "Path updated!"
    try:
        pid_file = 'process.pid'
        f = open(pid_file,'r')
        i = 0
        pid_number = f.readline()
        content = {"Status": "Not running"}
        for process in psutil.process_iter():
            if process.pid == int(pid_number):
                print('Process found. Terminating it.')
                os.kill(int(pid_number), signal.SIGKILL)
                process.terminate()
                content = {"Status":"Stopping"}
                break
    except:
        content = {"Status":"Error"}
    
    return JsonResponse(content)
#---------------------------------------------------------------------------------------