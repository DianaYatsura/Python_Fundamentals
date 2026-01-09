''' The volume of a spherical shell is the difference between the enclosed volume of the outer sphere
and the enclosed volume of the inner sphere.
Create a function vol_shell() that takes r1 (R) and r2 (r4) as arguments and prints the volume of
a spherical shell rounded to the nearest hundredths.'''

def vol_shell(r1, r2):
    PI = 3.14
    return 4/3 * PI * (r1**3 - r2**3)

## input the r1 and r2 for checking
print(round(vol_shell(r1=, r2=), 2))

