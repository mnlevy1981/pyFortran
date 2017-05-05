module pass_reals_mod

  Implicit None
  Private

  integer, parameter :: r8 = selected_real_kind(15, 307)

  public :: print_val
  public :: print_array

contains

  subroutine print_val(val)

    real(r8), intent(in) :: val

    print*, val

  end subroutine print_val

! *********************************************************

  subroutine print_array(arr)

  real(kind=r8), dimension(2,5), intent(in) :: arr

  integer :: j

  do j = 1,5
    print*, arr(:,j)
  end do

end subroutine print_array


end module pass_reals_mod