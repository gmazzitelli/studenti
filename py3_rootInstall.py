import os
import importlib
def wget(url):
    command = 'wget ' + url
    return os.system(command)
def unzip(file):
    command = 'unzip ' + file
    return os.system(command)
def tar(file):
    command = 'tar -xf ' + file
    return os.system(command)
def aptget(file):
    command = 'apt-get install ' + file
    return os.system(command)

# vai
wget('https://github.com/MohamedElashri/HEP-ML/releases/download/ROOT/ROOT.tar.zip')
unzip('/content/ROOT.tar.zip')
tar('ROOT.tar')
aptget('git dpkg-dev cmake g++ gcc binutils libx11-dev libxpm-dev libxft-dev libxext-dev tar gfortran subversion')
importlib.import_module('root-numpy')
import sys
sys.path.append("/content/root_build/")
sys.path.append("/content/root_build/bin/")
sys.path.append("/content/root_build/include/")
sys.path.append("/content/root_build/lib/")
import ctypes
ctypes.cdll.LoadLibrary('/content/root_build/lib//libCore.so')
ctypes.cdll.LoadLibrary('/content/root_build/lib//libThread.so')
ctypes.cdll.LoadLibrary('/content/root_build/lib//libTreePlayer.so')
