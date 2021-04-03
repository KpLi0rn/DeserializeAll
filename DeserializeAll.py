#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import subprocess
import sys

# 批量反编译
def DeserializeAll(paths,outputpath):
    if paths.endswith("jar"):
        popen = subprocess.Popen(['java','-jar','cfr-0.151.jar',paths,'--outputpath',outputpath],stdout=subprocess.PIPE)
        data = popen.stdout.read()
        print(data)
    else:
        for path in os.listdir(paths):
            childpath = os.path.join(paths,path)
            if os.path.isfile(childpath):
                if childpath.endswith("jar") or childpath.endswith("class"):
                    popen = subprocess.Popen(['java','-jar','cfr-0.151.jar',childpath,'--outputpath',outputpath],stdout=subprocess.PIPE)
                    data = popen.stdout.read()
                    print(data)
            elif os.path.isdir(childpath):
                DeserializeAll(childpath)

try:
    OriginPath = sys.argv[1]
    OutputPath = sys.argv[2]
    DeserializeAll(OriginPath,OutputPath)
except Exception as e:
    print("python DeserializeAll.py <OriginPath> <OutputPath>")
