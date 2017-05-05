SRC_FILES=hello_mod.F90      \
          pass_ints_mod.F90  \
          pass_reals_mod.F90

.PHONY: all
all: libfort.so

libfort.so: $(SRC_FILES)
	gfortran -shared -o $@ -fPIC $(SRC_FILES)

.PHONY: clean
clean:
	rm -f libfort.so *.mod

.PHONY: contents
contents:
	nm libfort.so

