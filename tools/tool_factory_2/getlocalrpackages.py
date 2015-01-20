import os
import subprocess

def find_packages(prefix="package_r_"):
    """
    """
    #locate env.sh | grep -i package_r_
    #/data/extended/galaxyJune14_2014/tool_dependency/readline/6.2/devteam/package_r_2_15_0/8ab0d08a3da1/env.sh
    #/data/home/rlazarus/galaxy/tool_dependency_dir/R_3_1_1/3.1.1/fubar/package_r_3_1_1/5f1b8d22140a/env.sh
    #/data/home/rlazarus/galaxy/tool_dependency_dir/R_3_1_1/3.1.1/fubar/package_r_3_1_1/d9964efbfbe3/env.sh
    #/data/home/rlazarus/galtest/tool_dependency_dir/R_3_1_1/3.1.1/fubar/package_r_3_1_1/63cdb9b2234c/env.sh
    eprefix = prefix
    if prefix.find('/') <> -1:
        eprefix = prefix.replace('/','\/') # for grep
    cl = ['locate env.sh | grep -i %s' % eprefix,]
    p = subprocess.Popen(cl, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
    out, err = p.communicate()
    fpaths = out.split('\n')
    fpaths = [x for x in fpaths if len(x) > 1]
    fver = [x.split(os.path.sep)[-4:-1] for x in fpaths]
    # >>> foo.split(os.path.sep)[-4:-1]
    # ['fubar', 'package_r_3_1_1', '63cdb9b2234c']
    res = [['%s rev %s owner %s' % (x[1],x[2],x[0]),fpaths[i],False] for i,x in enumerate(fver)]
    res.insert(0,['Use default (system) interpreter','system',False])
    if len(res) > 1:
        res[1][2] = True # selected if more than one
    # return a triplet - user_sees,value,selected - all unselected if False
    return res

if __name__ == "__main__":
   print find_packages()