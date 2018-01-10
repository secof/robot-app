# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import yaml
from django.shortcuts import render
from django.conf import settings
from time import gmtime, strftime, localtime
from .forms import SettingsForm
from robot.api import ExecutionResult
import robot


# Create your views here.
#---------------------------------------------------------------------------------------
def home(request):

    try:
        os.environ['TEST_PATH']
    except:
        with open('settings.yml', 'r') as outfile:
            stngs = yaml.load(outfile)
            os.environ["TEST_PATH"] = str(stngs["TestPath"])
            print "Path updated!"

    path = os.path.join(os.environ['TEST_PATH'], "results")
    folder = sorted(next(os.walk(path))[1])[-1]
    run_results_path = os.path.join(os.environ['TEST_PATH'], "results", folder)
    results_files = {}
    results_files[folder] = {}
    passed = 0
    failed = 0
    if os.path.isdir(run_results_path):
        for result_file in os.listdir(run_results_path):
            if os.path.splitext(result_file)[1] == ".html" and "Report" not in os.path.splitext(result_file)[0]: 
                results_files[folder][os.path.splitext(result_file)[0]]=[]      
                xml_file = os.path.splitext(result_file)[0]+'.xml'
                xml_file_path = os.path.join(path, folder, xml_file)
                results_files[folder][os.path.splitext(result_file)[0]].append({'failed' : ExecutionResult(xml_file_path).statistics.total.critical.failed })
                results_files[folder][os.path.splitext(result_file)[0]].append({'passed' : ExecutionResult(xml_file_path).statistics.total.critical.passed })
                failed += ExecutionResult(xml_file_path).statistics.total.critical.failed
                passed += ExecutionResult(xml_file_path).statistics.total.critical.passed

    sorted_results = reversed(sorted(results_files.items()))
 
    return render(request, 'dashboard.html', {"folders":sorted_results,"failed":failed,"passed":passed,})
#---------------------------------------------------------------------------------------
def testsList(request):

    try:
        os.environ['TEST_PATH']
    except:
        with open('settings.yml', 'r') as outfile:
            stngs = yaml.load(outfile)
            os.environ["TEST_PATH"] = str(stngs["TestPath"])
            print "Path updated!"

    path = os.path.join(os.environ['TEST_PATH'], "tests")
    test_folders = os.listdir(path)
    test_list = {}
    for folder in test_folders:
        testsPath = os.path.join(path, folder)
        test_list[folder] = []
        if os.path.isdir(testsPath):
            for test in os.listdir(testsPath):
                file_extension = os.path.splitext(test)[1]
                if file_extension == ".robot":
                    test_list[folder].append(test)

    context = {"testlist": test_list,}
    return render(request, 'testslist.html', context)
#---------------------------------------------------------------------------------------
def lastResults(request):
    try:
        os.environ['TEST_PATH']
    except:
        with open('settings.yml', 'r') as outfile:
            stngs = yaml.load(outfile)
            os.environ["TEST_PATH"] = str(stngs["TestPath"])
            print "Path updated!"

    path = os.path.join(os.environ['TEST_PATH'], "results")

    dir_list = next(os.walk(path))[1]
    test_dir_results = reversed(sorted(dir_list))
    results_files = {}

    for folder in test_dir_results:
        run_results_path = os.path.join(path, folder)
        results_files[folder] = {}
        if os.path.isdir(run_results_path):
            for result_file in os.listdir(run_results_path):
                if os.path.splitext(result_file)[1] == ".html" and "Report" not in os.path.splitext(result_file)[0]: 
                    results_files[folder][os.path.splitext(result_file)[0]]=[]
                    xml_file = os.path.splitext(result_file)[0]+'.xml'
                    xml_file_path = os.path.join(path, folder, xml_file)
                    results_files[folder][os.path.splitext(result_file)[0]].append({'failed' : ExecutionResult(xml_file_path).statistics.total.critical.failed })
                    results_files[folder][os.path.splitext(result_file)[0]].append({'passed' : ExecutionResult(xml_file_path).statistics.total.critical.passed })

    sorted_results = reversed(sorted(results_files.items()))

    return render(request, 'lastresults.html', {"folders":sorted_results,})
#---------------------------------------------------------------------------------------
def show_result(request,result,log):
    try:
        os.environ['TEST_PATH']
    except:
        with open('settings.yml', 'r') as outfile:
            stngs = yaml.load(outfile)
            os.environ["TEST_PATH"] = str(stngs["TestPath"])
            print "Path updated!"

    path = os.path.join(os.environ['TEST_PATH'], "results")
    
    log_page = os.path.join(path, result, log) + ".html"
    with open(log_page, 'r') as logfile:
        content = logfile.read()
    return render(request, 'show_result.html', {"content":content,})
#---------------------------------------------------------------------------------------
def show_test(request, folder, name):
    try:
        os.environ['TEST_PATH']
    except:
        with open('settings.yml', 'r') as outfile:
            stngs = yaml.load(outfile)
            os.environ["TEST_PATH"] = str(stngs["TestPath"])
            print "Path updated!"
    path = os.path.join(os.environ['TEST_PATH'], "tests")
    
    robot_test = os.path.join(path, folder, name)
    with open(robot_test, 'r') as rtest:
        content = rtest.read()
    return render(request, 'show_test.html', {"content":content,"name":name,})
#---------------------------------------------------------------------------------------
def robotSettings(request):
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            os.environ["TEST_PATH"] = form.cleaned_data['test_path'] #/home/constantin/Test/test
            data = dict(
                GitRepo = form.cleaned_data['git_repo'],
                SeleniumHost = form.cleaned_data['sel_host'],
                SeleniumPort = form.cleaned_data['sel_port'],
                SeleniumOs = form.cleaned_data['sel_os'],
                Browser = form.cleaned_data['browser'],
                TestPath = form.cleaned_data['test_path'],
                )
            with open('settings.yml', 'w') as outfile:
                yaml.dump(data, outfile, default_flow_style=False)
    else:
        form = SettingsForm()
    try:
        with open('settings.yml', 'r') as outfile:
            oldset = yaml.load(outfile)
            # for key in oldset:
            #     print key, oldset[key]
    except:
        oldset = "No settings present!"
    context = {
        'form': form,
        'old_settings':oldset,
    }
    return render(request, 'settings.html', context)
