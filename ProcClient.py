#!/usr/bin/env python3 -x
#client

import socket
from struct import pack
import subprocess
import time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def send_data():
    #commandStr = ['ps -eas | tr -s " " | cut -d " " -f 2,5']
    out = subprocess.run(["ps", "-eas"], stdout=subprocess.PIPE)
    # out2  = subprocess.run(['tr', '-s', '" "'], input=out1.stdout, stdout=subprocess.PIPE)
    # out  = subprocess.run(['cut', '-d', '" "-f ', '2,5'], input=out2.stdout, stdout=subprocess.PIPE)
    #out = subprocess.run(commandStr,stdout=subprocess.PIPE,shell=True)
    if(0!=out.returncode):
        print("The exit code was: %d" % out.returncode)
        exit(1)
    else:
        process_data = out.stdout
        print(process_data)
        length = pack('>Q', len(process_data))
        s.sendall(length)
        s.sendall(process_data)
        print('sent %d' % len(process_data) )
        ack = s.recv(1)
        print('Received', repr(ack))

def sendPeriodically():    
    send_data()
    time.sleep(5.0)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
    except OSError as error:
        print("Couldnt connect with the socket-server: %s\n terminating program" % error.strerror)
        exit(1)
    while(True):
        sendPeriodically()   
    
    
   

