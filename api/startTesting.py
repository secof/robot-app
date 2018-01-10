import os
import sys
import robot
import yaml
from time import gmtime, strftime, localtime


#####################################################################################
path = os.path.join(os.environ['TEST_PATH'], "tests")
test_folder = os.listdir(path)
# print test_folder
dts=strftime("%d.%m.%Y_%H.%M", localtime())
var_arg = '--variable'
log_arg = '--log'
report_arg = '--report'
report_val = 'NONE'
output_arg = '-o'
result_arg = '-d'
sel_host = '"SELENIUM_HOST:%s"'%('172.21.3.103')
sel_port = '"SELENIUM_PORT:%s"'%('4444')
browser = '"BROWSER:%s"'%('chrome')
sel_os = '"SELENIUM_OS:%s"'%('LINUX')
tst ={}
sorted_list = []
results_folder = "Results_" + strftime("%d.%m.%Y_%H.%M", localtime())
#####################################################################################



try:
    with open('settings.yml', 'r') as outfile:
        oldset = yaml.load(outfile)
        sel_host = '"SELENIUM_HOST:%s"'%(oldset['SeleniumHost'])
        sel_port = '"SELENIUM_PORT:%s"'%(oldset['SeleniumPort'])
        browser = '"BROWSER:%s"'%(oldset['Browser'])
        sel_os = '"SELENIUM_OS:%s"'%(oldset['SeleniumOs'])
        # for key in oldset:
        #     print key, oldset[key]
except:
    print "No settings present!"




for folder in test_folder:
    tst[folder]=[]
    test_path = os.path.join(path, folder)
    if os.path.isdir(test_path):
        for test in os.listdir(test_path):
            file_extension = os.path.splitext(test)[1]
            if file_extension == ".robot":            
                # tst[folder].append(test)
                sorted_list.append(test)
    tst[folder] = sorted(sorted_list, key=str.lower)
    sorted_list = []

def run_robot(test_name, test_folder):
    #Test absolute path
    test_path = os.path.join(path, test_folder)
    individual_test_path = os.path.join(test_path,test_name)
    #Result absolute path
    result_path = os.path.join(os.environ['TEST_PATH'], "results")
    result_folder = os.path.join(result_path, results_folder)
    #Log name
    log_name = '%s-%s.html'%(os.path.splitext(test_name)[0],dts)
    # report_val = 'Report-%s-%s.html'%(os.path.splitext(test_name)[0],dts)
    output_file = '%s-%s.xml'%(os.path.splitext(test_name)[0],dts)
    #Run ROBOT
    robot.run_cli([log_arg,log_name,result_arg,result_folder,var_arg,sel_host,var_arg,sel_port,var_arg,browser,var_arg,sel_os,report_arg,report_val,output_arg,output_file,str(individual_test_path)], exit=False)
    # print log_arg,log_name,result_arg,result_folder,var_arg,sel_host,var_arg,sel_port,var_arg,browser,var_arg,sel_os,report_arg,report_val,output_arg,output_file,str(individual_test_path)


for key in tst:
    for test in tst[key]:
        run_robot(test, key)
