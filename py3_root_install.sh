wget https://github.com/MohamedElashri/HEP-ML/releases/download/ROOT/ROOT.tar.zip
unzip /content/ROOT.tar.zip
tar -xf  ROOT.tar
apt-get install git dpkg-dev cmake g++ gcc binutils libx11-dev libxpm-dev libxft-dev libxext-dev tar gfortran subversion
install root_numpy # optional if you want to convert Trees to numpy arrays and other things like that
wget https://raw.githubusercontent.com/gmazzitelli/cygno_cloud/main/cygnus_lib.py
wget https://raw.githubusercontent.com/gmazzitelli/cygno/master/mylib.py
madir out
mkdir ped
wget https://raw.githubusercontent.com/gmazzitelli/studenti/master/rootenv.py
%run rootenv.py
pip install root-numpy
