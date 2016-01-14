import re
import os
import subprocess
import commands
vt = "/opt/vde/services/instances/vde_latest/bin/vde_tool "
vtn = vt + "--Vno_sync "

cur_dir = os.getcwd();

dir = re.search('(/ws/jelou/[^/]*)', cur_dir)

if dir is not None:
    main_dir = dir.group(1)
    print "main dir is " + main_dir
else:
    print "can't get main dir"


ubr_ios = main_dir + '/ios/sys'
cbr_ios = main_dir + '/ios/ios/sys'
cbr_binos = main_dir + '/binos'

if os.path.exists(ubr_ios) :
    print  ubr_ios + " is exist, go to clean it"
    os.chdir(ubr_ios)
    print "cur dir is " + os.getcwd()
    args = [r"/opt/vde/services/instances/vde_latest/bin/vde_tool ws info"]
    result = subprocess.Popen(args, stdout=subprocess.PIPE, shell=True)
    (out, err) = result.communicate()
    print "lyp out " +  out

