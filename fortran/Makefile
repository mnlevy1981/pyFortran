SRC_FILES=hello_mod.F90

.PHONY: all
all: libfort.so

.PHONY: clean
clean:
	rm -f libfort.so fortran.mod

libfort.so: $(SRC_FILES)
	gfortran -shared -o $@ -fPIC $(SRC_FILES)
