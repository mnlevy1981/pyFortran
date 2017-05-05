module hello_mod

  Implicit None
  Private

  public :: print_hello

contains

  subroutine print_hello()

    print*, "Hello world!"

  end subroutine print_hello

end module hello_mod
