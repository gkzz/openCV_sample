# Sample Code's openCV for Python

## How to setup??

### move to openCV_sample directory
cd /xxx/openCV_sample

### type these commands before you install install necessary packages.
pip install --upgrade pip
sudo apt-get update
sudo apt-get upgrade

#### if you got the error as bellow;
Errors were encountered while processing:
/var/cache/apt/archives/libpython3.6-stdlib_3.6.5-5~16.04.york1_amd64.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)
#### try to type this command
sudo dpkg --install --force all /var/cache/apt/archives/libpython3.6-stdlib_3.6.5-5~16.04.york1_amd64.deb
#### sources
https://askubuntu.com/questions/1037528/apt-get-upgrade-error-for-python-packages-in-ubuntu-16-04

### create python virtual environment
python -m venv <x: name of virtual environment ex) python version>

### move into python virtual environment
source x/bin/activate

### install all libraries that are needed in order to run this program
pip install -r requirements.txt
 
pip install opencv-python

pip install pandas

pip install jupyter

pip install matplotlib

pip install seaborn

git clone git@github.com:opencv/opencv.git


python3.x test.py
### you would lile to check if images are shown by jupyter notebook.
jupyter notebook

## Notes
python --version
Python 3.6.5

## If you face trouble...
plz give me comments!

