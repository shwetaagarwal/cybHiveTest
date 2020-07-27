#!/usr/bin/env python3

import socket
import os
import sys
from struct import unpack

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


output_dir = '.'
file_num = 1
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print('Server...')
    s.bind((HOST, PORT))
    s.listen()
    s.settimeout(10) #for testing
    try:
        conn, addr = s.accept()
    except socket.timeout:
        print('caught a timeout')
        exit(1)
    
    with conn:
        print('Connected by', addr)
        while True:
            try:
                dataLenBin = conn.recv(8)
                #raise Exception("Testing exception")
            except OSError as error:
                print("Couldnt recv: %s\n terminating program" % error.strerror)
                continue
            if not dataLenBin:
                break
            (dataLen,) = unpack('>Q', dataLenBin)
            data = b''
            print(dataLen)
            while len(data) < dataLen:
                to_read = dataLen - len(data)
                data += conn.recv(4096 if to_read > 4096 else to_read)
            assert len(b'\00') == 1
            conn.sendall(b'\00')
            print('Sent reply')
            with open(os.path.join(output_dir, 'ProcList%02d.txt' % file_num), 'w') as fp:
                fp.write(data.decode(sys.stdout.encoding)) 