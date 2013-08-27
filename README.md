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
This program is not affiliated with *FHI-aims*.
The program is made available under the GNU General Public License; you are free to modify and use the code, but do so at your own risk.