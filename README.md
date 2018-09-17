pip install --upgrade pip
sudo apt-get update
sudo apt-get upgrade

# if you got the error as bellow;
#
# Errors were encountered while processing:
# /var/cache/apt/archives/libpython3.6-stdlib_3.6.5-5~16.04.york1_amd64.deb
#E: Sub-process /usr/bin/dpkg returned an error code (1)
#
# sudo dpkg --install --force all /var/cache/apt/archives/libpython3.6-stdlib_3.6.5-5~16.04.york1_amd64.deb
# sources
# https://askubuntu.com/questions/1037528/apt-get-upgrade-error-for-python-packages-in-ubuntu-16-04

# if you would like to install all necessary libraries at one time.
# pip install -r requirements.txt
 
pip install opencv-python
pip install pandas
pip install jupyter
pip install matplotlib
pip install seaborn

git clone git@github.com:opencv/opencv.git


python3.x test.py
# jupyter notebook.
