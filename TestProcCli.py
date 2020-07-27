#!/usr/bin/env python3

import unittest
#import ProcSrv
import ProcClient
import multiprocessing
#import threading
import time
import os

class TestProcClient(unittest.TestCase):
   
     
    def test_client():
        p = multiprocessing.Process(target=ProcClient, name="ProcClient")#, args=(,))
        p.start()
        print("started server")
        
        p.terminate()
        print('TERMINATED:', p, p.is_alive())
        
        if(p.is_alive()):
            os.kill(p.pid, signal.SIGKILL)

        p.join()
        print('JOINED:', p, p.is_alive())
        
if __name__ == '__main__':
    unittest.main()
    