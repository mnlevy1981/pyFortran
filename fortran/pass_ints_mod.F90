module pass_ints_mod

  Implicit None
  Private

  public :: print_val
  public :: print_array

  integer, parameter :: int_kind = selected_int_kind(4)

contains

  subroutine print_val(val)

    integer(int_kind), intent(in) :: val

    print*, val

  end subroutine print_val

! *********************************************************

  subroutine print_array(arr)

  integer(int_kind), dimension(2,5), intent(in) :: arr

  integer :: j

  do j = 1,5
    print*, arr(:,j)
  end do

end subroutine print_array


end module pass_ints_mod