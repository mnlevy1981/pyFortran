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

###########################
# Read library via ctypes #
###########################

libadd = ctypes.cdll.LoadLibrary("../fortran/libfort.so")

########################
# 1. print "hello world"
########################

libadd.__hello_mod_MOD_print_hello(None)

###################################
# 2. print int scalar and r8 scalar
###################################

# fairly intuitive way to declare scalar ctypes
int_scalar = ctypes.c_short(1)
r8_scalar = ctypes.c_double(2.801)
libadd.__pass_ints_mod_MOD_print_val(ctypes.byref(int_scalar))
libadd.__pass_reals_mod_MOD_print_val(ctypes.byref(r8_scalar))

#################################
# 3. print int array and r8 array
#################################

# unintuitive way to declare arrays of ctypes...
int_array = (ctypes.c_short*10)(1,2,3,4,5,6,7,8,9,10)
r8_array  = (ctypes.c_double*10)(1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0)
libadd.__pass_ints_mod_MOD_print_array(int_array)
libadd.__pass_reals_mod_MOD_print_array(r8_array)