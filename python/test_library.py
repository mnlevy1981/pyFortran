#!/usr/bin/env python

import ctypes

"""
$ nm ../fortran/libfort.so
0000000000000ee3 T ___hello_mod_MOD_print_hello
                 U __gfortran_st_write
                 U __gfortran_st_write_done
                 U __gfortran_transfer_character_write
                 U dyld_stub_binder

"""

# Read library via ctypes
libadd = ctypes.cdll.LoadLibrary("../fortran/libfort.so")

libadd.__hello_mod_MOD_print_hello(None)

