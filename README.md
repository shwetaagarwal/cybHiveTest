# cybHiveTest
client sends process list to server every 5s, serer writes data recv to a file
change host names before using
Requires python 3
used unittest,coverage for coverage
todo:
error check and exception handling
only process name list or pid etc too
file overwritten everytime at server.

$ coverage run -m unittest TestProcSrv.py
$ python ProcClient.py
$ coverage report -m
Name             Stmts   Miss  Cover   Missing
----------------------------------------------
ProcSrv.py          39      6    85%   21-23, 31-33
TestProcSrv.py      19     11    42%   50-62, 65
----------------------------------------------
TOTAL               58     17    71%

$ProcSrv.py
$ coverage report -m unittest TestProcCli.py
$ coverage report -m
Name             Stmts   Miss  Cover   Missing
----------------------------------------------
ProcClient.py       30      5    83%   19-20, 38-40
TestProcCli.py      18     16    11%   6-29
----------------------------------------------
TOTAL               48     21    56%
