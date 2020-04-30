#/bin/sh
mkdir -p $HOME/APPS
cd $HOME/APPS 
wget -q https://root.cern.ch/download/root_v6.13.08.Linux-ubuntu18-x86_64-gcc7.3.tar.gz 
cd $HOME/APPS
tar -xf root_v6.13.08.Linux-ubuntu18-x86_64-gcc7.3.tar.gz
pip install root-numpy
apt-get install libdavix0v5
echo "Davix.GSI.CACheck: n" >> $ROOTSYS/etc/system.rootrc
cp $ROOTSYS/etc/system.rootrc $HOME/.rootrc
tail -1 $HOME/.rootrc
pip install -q  python-swiftclient
pip install -q  keystoneauth1
pip install -q  h5py
wget -q https://raw.githubusercontent.com/gmazzitelli/cygno/master/cygnus_lib.py
wget -q https://raw.githubusercontent.com/gmazzitelli/cygno/master/mylib.py
mkdir -p $HOME/data
exit
