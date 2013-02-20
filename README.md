aims2vectors
============
Read *FHI-aims*-formatted geometry.in file and return vectors in a, b, c, alpha, beta, gamma form.
Intended for easy reporting and comparison of periodic unit cells for quantum chemistry.

Requirements
------------
Python with Numpy, Unix-like file system.


To Do
-----
* Allow user to specify precision with optional argument
    * e.g. `aims2vectors ~/geometry.in  --length 4 --angle 3`

Disclaimer
----------
This script is not affiliated with *FHI-aims*. Feel free to use it and build on it, but do so at your own risk.