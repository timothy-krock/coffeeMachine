#!/usr/bin/env python
################################################
##  RASPBERRY PI POWERED COFFEE MACHINE
##  WRITTEN AND BUILT BY TIM KROCK
##  TODO:CUE
###############################################
import RPi.GPIO as GPIO
import time
import json
import time
import os
import subprocess
from time import localtime, strftime
import sys
sys.path.append('~/Desktop/coffee/')
import myjson
url = 'IM_NOT_GONNA_MAKE_THIS_PUBLIC_SORRY'
timer = 0

os.environ['TZ'] = 'US/Central'
#####################################
## CODE TO FIRE THE RELAY THAT MAKES
## THE COFFEE BOTH ON AND OFF SWITCH
#####################################
import RPi.GPIO as GPIO
def makeCoffee():
    pin = 12
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin,GPIO.OUT)
    
    GPIO.output(pin, GPIO.HIGH)
    
    time.sleep(.1)
    
    GPIO.output(pin, GPIO.LOW)

#####################################
## CODE THAT FETCHE'S PI'S IP ADDRESS
## I OPTED TO PUT THIS IN SO THAT
## THE MACHINE CAN SEND IT'S IP TO
## MY HUD FOR EASY SSH ACCESS
#####################################
def getIP():
    proc = subprocess.Popen('hostname -I', shell=True, stdout=subprocess.PIPE)
    output = proc.stdout.read()
    ip = ''
    for i in range(len(output)):
        if output[i] == ' ':
            ip = output[:i]
            break
    print ip
    return ip




while(1):
    ##################################
    ##  DEFINE CURRENT TIME
    ##  USEFUL FOR timetocoffee
    ##  AS WELL AS json.coffee.updated
    ##################################
    currentTime = strftime("%a, %d %b, %Y %X +0000", localtime())[:-6]
    ip = getIP()
    ##################################
    ##  MONITER JSON
    ##  if json.coffee.coffeetime = 1
    ##  we change it to zero and set
    ##  json.coffee.status to "Brewing"
    ##  For the next three minutes
    ##################################
    try:
        if not timer:
            print 'idle'
            
            jason = json.loads(myjson.get(url))
            
            
            if jason['coffee']['coffeeTime'] != '1':
                ## UPDATE json.coffee info to include ip address and such
                jason['coffee']['coffeeTime'] = '0'
                jason['coffee']['status'] = 'idle'
                jason['coffee']['ip'] = ip
                jason['coffee']['updated'] = currentTime
                #print 'a:',jason
                myjson.store(json.dumps(jason), update=url, id_only=True)
            
            elif jason['coffee']['coffeeTime'] == '1':
                ## UPDATE JSON TO SAY "BREWING"
                jason['coffee']['status'] = 'brewing'
                jason['coffee']['updated'] = currentTime
                jason['coffee']['ip'] = ip
                #print 'b:',jason
                myjson.store(json.dumps(jason), update=url, id_only=True)
                makeCoffee()
                print 'coffeeTime!'
                timer = 1
        else:
            print "brewing!"
            timer = timer + 3
            if timer > 1:
                timer = 0
                ## UPDATE JSON TO SAY IDLE, AND COFFEETIME TO 0
                jason = json.loads(myjson.get(url))
                jason['coffee']['coffeeTime'] = '0'
                jason['coffee']['status'] = 'idle'
                jason['coffee']['updated'] = currentTime
                jason['coffee']['ip'] = ip
                #print jason
                myjson.store(json.dumps(jason), update=url, id_only=True)

except:
    print "NO CONNECTION"
    
    time.sleep(4)
