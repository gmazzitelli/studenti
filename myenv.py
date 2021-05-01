def root_env():
  import sys
  sys.path.append("/content/root_build/")
  sys.path.append("/content/root_build/bin/")
  sys.path.append("/content/root_build/include/")
  sys.path.append("/content/root_build/lib/")
  import ctypes
  ctypes.cdll.LoadLibrary('/content/root_build/lib//libCore.so')
  ctypes.cdll.LoadLibrary('/content/root_build/lib//libThread.so')
  ctypes.cdll.LoadLibrary('/content/root_build/lib//libTreePlayer.so')
