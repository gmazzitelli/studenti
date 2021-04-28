# istallazione di ROOT dal CERN
!mkdir -p APPS
!pwd
!cd APPS && wget --no-check-certificate https://root.cern.ch/download/root_v6.13.08.Linux-ubuntu18-x86_64-gcc7.3.tar.gz 
!cd APPS && tar -xf root_v6.13.08.Linux-ubuntu18-x86_64-gcc7.3.tar.gz

base_lib_path = '/content/APPS/root/lib/'
# main paths for ROOT  
import sys
sys.path.append(base_lib_path)
import ctypes
sys.path.append(base_lib_path)
ctypes.cdll.LoadLibrary(base_lib_path+'libCore.so')
ctypes.cdll.LoadLibrary(base_lib_path+'libThread.so')
ctypes.cdll.LoadLibrary(base_lib_path+'libImt.so')
ctypes.cdll.LoadLibrary(base_lib_path+'libRIO.so')
ctypes.cdll.LoadLibrary(base_lib_path+'libNet.so')
ctypes.cdll.LoadLibrary(base_lib_path+'libTree.so')
ctypes.cdll.LoadLibrary(base_lib_path+'libMathCore.so')
ctypes.cdll.LoadLibrary(base_lib_path+'libMatrix.so')
ctypes.cdll.LoadLibrary(base_lib_path+'libHist.so')
ctypes.cdll.LoadLibrary(base_lib_path+'libGraf.so')
# itsllation and root-numpy main PATH
!pip install root-numpy
ctypes.cdll.LoadLibrary(base_lib_path+'libMultiProc.so')
ctypes.cdll.LoadLibrary(base_lib_path+'libGpad.so')
ctypes.cdll.LoadLibrary(base_lib_path+'libGraf3d.so')
ctypes.cdll.LoadLibrary(base_lib_path+'libTreePlayer.so')
# patch to open online FILE
! sudo apt-get install libdavix0v5
ctypes.cdll.LoadLibrary(base_lib_path+'libRDAVIX.so')
! echo "Davix.GSI.CACheck: n" >> $ROOTSYS/etc/system.rootrc
! cp $ROOTSYS/etc/system.rootrc $HOME/.rootrc
! tail -1 $HOME/.rootrc
! pip install -q  python-swiftclient
! pip install -q  keystoneauth1
! pip install -q  h5py
! rm cygnus_lib.*; rm mylib.*
! wget https://raw.githubusercontent.com/gmazzitelli/cygno/master/cygnus_lib.py
! wget https://raw.githubusercontent.com/gmazzitelli/cygno/master/mylib.py
sys.path.append('.')
! mkdir -p data
