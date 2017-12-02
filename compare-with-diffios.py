###################################################
## Created by Fajar for IT Automation test case  ##
##    compare cisco config with previous day     ##
## diffios: https://pypi.python.org/pypi/diffios ##
###################################################
## import function
import datetime
import diffios
import os
import os.path

## define time
today = datetime.date.today()
yesterday = datetime.date.today() - datetime.timedelta(days = 1)
T = today.strftime("%Y%m%d")
Y = yesterday.strftime("%Y%m%d")

## define file cisco config with timestamp
baseline1 = '/PATH/TO/FILE/SWITCH-ANSIBLE_{}.txt'.format(Y, Y)
comparison1 = '/PATH/TO/FILE/SWITCH-ANSIBLE_{}.txt'.format(T, T)
baseline2 = '/PATH/TO/FILE/ROUTER-ANSIBLE_{}.txt'.format(Y, Y)
comparison2 = '/PATH/TO/FILE/ROUTER-ANSIBLE_{}.txt'.format(T, T)

## write to file diff
DiffToday = '/PATH/TO/FILE/diff_{}.txt'.format(T)
file = open(DiffToday, "w")

## compare switch config today and yesterday with error handling
if os.path.isfile(baseline1) and os.path.isfile(comparison1):
    diff1 = diffios.Compare(baseline1, comparison1)
    file.write("\n Comparison SWITCH-ANSIBLE Today and Yesterday \n")
    file.write(diff1.delta())
    file.write("\n \n")
else:
    file.write("DC-SWITCH-ANSIBLE Backup Config File doesn't exist \n \n")

## compare router config today and yesterday with error handling   
if os.path.isfile(baseline2) and os.path.isfile(comparison2):
    diff2 = diffios.Compare(baseline2, comparison2)
    file.write("Comparison ROUTER-ANSIBLE Today and Yesterday \n")
    file.write(diff2.delta())
    file.write("\n \n")
else:
    file.write("ROUTER-ANSIBLE Backup Config File doesn't existi \n \n")

file.close()
## close file diff