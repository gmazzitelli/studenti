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
print('scarica root')
wget('https://github.com/MohamedElashri/HEP-ML/releases/download/ROOT/ROOT.tar.zip')
print('unzip root')
unzip('/content/ROOT.tar.zip')
print('untar root')
tar('ROOT.tar')
print('istalla pacchetti')
aptget('git dpkg-dev cmake g++ gcc binutils libx11-dev libxpm-dev libxft-dev libxext-dev tar gfortran subversion')
print('root-numpy')
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
