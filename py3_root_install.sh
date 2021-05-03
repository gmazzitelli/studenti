# old
wget https://github.com/MohamedElashri/HEP-ML/releases/download/ROOT/ROOT.tar.zip
unzip /content/ROOT.tar.zip
tar -xf  ROOT.tar
apt-get install git dpkg-dev cmake g++ gcc binutils libx11-dev libxpm-dev libxft-dev libxext-dev tar gfortran subversion
install root_numpy # optional if you want to convert Trees to numpy arrays and other things like that

# latest credit to https://gist.github.com/MohamedElashri/ (https://gist.github.com/MohamedElashri/dab00a84ba6a65f99fb2694504ecc39e)
# mkdir -p APPS
# pwd
# wget https://raw.githubusercontent.com/gmazzitelli/studenti/master/rootenv.py
# cd APPS && wget https://root.cern.ch/download/root_v6.13.08.Linux-ubuntu18-x86_64-gcc7.3.tar.gz 
# cd APPS && tar -xf root_v6.13.08.Linux-ubuntu18-x86_64-gcc7.3.tar.gz


# more 
wget https://raw.githubusercontent.com/gmazzitelli/cygno_cloud/main/cygnus_lib.py
wget https://raw.githubusercontent.com/gmazzitelli/cygno/master/mylib.py
wget https://raw.githubusercontent.com/gmazzitelli/studenti/master/rootenv.py
madir out
mkdir ped

