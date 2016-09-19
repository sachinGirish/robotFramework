# RobotFramework

[![ScreenShot](https://blog.codecentric.de/files/2012/04/Sample_Overview1.png)]

<h2>Welcome to the Robot-Framework</h2>

**Requirement and Prerequisite jars**

1. [Installation-Instructions](https://github.com/robotframework/RIDE/wiki/Installation-Instructions)

Selenium Robot Framework Installation with Python
To use Robot Framework with Python, you need to install Python, robot framework, Selenium2Library and other supporting libraries. 

Step 1: Install Python 2.7 version

        Before installing Robot Framework, you need to install Python 2.5 or later. Robot Framework has not been updated to work with Python 3 or above, so you should certainly install Python 2.7 version. Visit the link to download and install Python 2.7 version. After installing Python 2.7, add your python installation to your system environment path. 

on Windows, add "c:\Python27\;c:\Python27\Scripts\;" to your path. On Windows vista or Windows 7 environment, it is recommended to install Python to all users, and to run the installation as an administrator. After installing, you can confirm python installation with the command below. 

Step 2: Verify Python 2.7 version

python --version
command result will be

Python 2.7.6
Step 3: install robot framework with pip command. When you install Python, pip application will be installed automatically. If you are familiar with installing Python packages and have pip available, just run the following command.

pip install robotframework
 Step 4: Verify robot framework installation

After a successful installation with Python, you should be able to  execute the following commands on the command prompt to verify the installation. 

pybot --version
Command Result

Robot Framework 2.8.4 (Python 2.7.6 on win32)
Step 5: Install Selenium2Library

You can install robotframework-selenium2library by downloading the packaged executable file or using the python pip application. Here is the link to download. Use the following command to install robotframework-selenium2library with pip. 

pip install robotframework-selenium2library
Step 6: Install Selenium Library

Since Selenium2Library has some dependencies for selenium library, you need to install selenium library. The easy way of installing selenium library is to use pip. You can use the following command to install selenium.

pip install -U selenium
Step 7:  Install the Selenium robot framework IDE - RIDE

RIDE is a light-weight and intuitive editor for Robot Framework test case files. Since RIDE uses wxpython 2.8, you need to install the package as well. Visit the link for details. RIDE does not yet support Python 3. On OS X RIDE requires 32-bit Python version. 

To install wxpython 2.8 or later version, visit the wxpython.org download page and download the version depending on your OS. Please note that the package has 32 bit and 64 bit, so you need to install the corresponding package depending on your operating system version. 

To install RIDE, you can use pip with the following command. 

pip install robotframework-ride
Step 8: Verify RIDE Installation

After a successful installation, RIDE can be started from the command line by running

 ride.py 
Alternatively you can specify a file or directory to open as an argument like ride.py path/to/tests. Starting from RIDE 0.54, you can also create a desktop shortcut during installation on Windows.

On Windows running ride.py requires having <PythonInstallationDir>\Scripts on PATH. If pybot command to run tests with Robot Framework works you should be fine. If it does not, see Robot Framework installation instructions for more information about setting PATH. When RIDE starts, you will see the UI as shown below. This screenshot has a MaharaDemoTest created by RIDE Program. 

**2. Prerequisite jars**

pip install jarName --ver    (use higher version )        


$ pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs pip install -U   (To update All jars )


apipkg==1.4
Appium-Python-Client==0.20
backports.ssl-match-hostname==3.4.0.2
beautifulsoup4==4.4.1
colorama==0.3.3
coverage==4.0.1
decorator==4.0.4
docutils==0.12
ecdsa==0.13
enum34==1.0.4
et-xmlfile==1.0.0
execnet==1.4.1
formencode==1.3.0
funcsigs==0.4
gdata==2.0.18
gspread==0.2.5
jdcal==1.0
jsonpatch==1.11
jsonpointer==1.9
mock==1.3.0
mysql-connector-python==2.0.4
mysql-python==1.2.4b4
natsort==4.0.3
openpyxl==2.3.0b2
pbr==1.8.0
py==1.4.30
pycrypto==2.6.1
pydispatcher==2.0.5
Pygments==2.0.2
PyMySQL==0.6.6
pytest==2.7.3
pytest-cov==2.1.0
pytest-pythonpath==0.7
pytest-xdist==1.13.1
python-dateutil==2.4.2
python-google-spreadsheet==2.0.0
requests==2.7.0
robotframework==2.9.2
robotframework-androidlibrary==0.2.0
robotframework-appiumlibrary==1.3.4
robotframework-databaselibrary==0.6
robotframework-debuglibrary==0.4
robotframework-difflibrary==0.1.dev0
robotframework-excellibrary==0.0.2
robotframework-httplibrary==0.4.2
robotframework-ioslibrary==0.2.0
robotframework-ride==1.5a2
robotframework-selenium2library==1.7.4
sauceclient==0.2.1
selenium==2.48.0
simplejson==3.8.0
six==1.9.0
SQLAlchemy==1.0.8
sqlobject==3.0.0a1.dev20150327
waitress==0.8.10
WebOb==1.4.1
WebTest==2.0.18
xlrd==0.9.4
xlutils==1.7.1
xlwt==1.0.0
yolk==0.4.3


**3. Paste chromedriver.exe in Scripts folder for compatibility test**

C:\Python27\Scripts 

