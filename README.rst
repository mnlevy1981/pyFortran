
===================================
Python Wrappers for Fortran Library
===================================

The ``fortran`` directory contains modules with a variety of different Fortran interfaces.
Build ``libfort.so`` in that directory with

::

  $ cd fortran
  $ make

The ``python`` directory contains a python script that calls various Fortran subroutines.

::

 $ cd python
 $ ./test_library.py

---------------
Curently Tested
---------------

* Subroutine with no arguments
* Subroutine with integer ``intent(in)``
* Subroutine with real ``intent(in)``
* Subroutine with integer array ``intent(in)``
* Subroutine with real array ``intent(in)``

-------------------
Things To Also Test
-------------------

* Various ``intent(out)`` types
* Allocatable arrays (I suspect this will not work)
* Derived-type arguments
