#!/usr/bin/env python3

import unittest
import ProcSrv
#import ProcClient
import multiprocessing
#import threading
import time
import os

class TestProcSrv(unittest.TestCase):
    
    # def setup(ProcSrv):
    #     p = multiprocessing.Process(target=ProcSrv, name="ProcSrv")#, args=(,))
    #     p.daemon = True
    #     p.start()
    
    # def tearDown(ProcSrv):
    #     time.sleep(3)
    #     print("Terminating")
        
    #     p.terminate()
    #     print('TERMINATED:', p, p.is_alive())
        
    #     if(p.is_alive()):
    #         os.kill(p.pid, signal.SIGKILL)

    #     p.join()
    #     print('JOINED:', p, p.is_alive())
      
    # def test_accept_timeout(n):
    #     p = multiprocessing.Process(target=ProcSrv, name="ProcSrv")#, args=(,))
    #     p.daemon = True
    #     p.start()
    
    #     # Wait 10 seconds 
    #     time.sleep(3)
    #     print("Terminating")
        
    #     p.terminate()
    #     print('TERMINATED:', p, p.is_alive())
        
    #     if(p.is_alive()):
    #         os.kill(p.pid, signal.SIGKILL)

    #     p.join()
    #     print('JOINED:', p, p.is_alive())
        
    def test_server():
        p = multiprocessing.Process(target=ProcSrv, name="ProcSrv")#, args=(,))
        p.daemon = True
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
    