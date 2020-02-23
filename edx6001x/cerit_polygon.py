# -*- coding: utf-8 -*-

"""
input: n sides and s side length.
return the sum of area and perimeter squeared of a regular polygon with
n sides of length s.

function begin with 'rp _' ... to indicate they are for regular polygons.

tau = 2 pi, thus 360 degree = tau radians.

Code by cerit rev: 0.1, 02/13/20
"""

debug = False
test = True
import math


def rp_perimeter(n, s):
    """
    input: integer number of sides n and numeric side length s.
    returns the perimeter length of a regular polygon with n sides of length n.
    """
    if debug is True: print('entering rp_perimeter with n', n, 'and s', s)
    if debug is True: print('exit rp_perimeter and return n * s = ', n * s)
    return n * s


def rp_apotheum(n, s):
    """
    input: integer number of sides n and numeric side length s.
    returns the length of the apotheum, the distance between the center and the
    middle of any of the sides (kindof like radius).
    
    The apotheum forms a right triangle with half of the side it intersects,
    and the acute angle of that triangle is necessarily tau/n radians.  Lets
    call that angle phi and apotheum a.   Then tan(phi) = (1/2 s) / a and
                  s
    Thus a =   ---------
               2 tan(phi)
    """
    if debug is True: print('entering apotheum with n', n, 'and s', s)
    phi = math.tau/(2*n)
    phi_deg = math.degrees(phi)
    if debug is True:
        print('calculated interior angle of pie piece phi =', phi, 'rad or',
               phi_deg, 'degrees')
    apotheum = s / (2 * (math.tan(phi)))
    if debug is True: print('exit rp_apotheum and return apotheum', apotheum)
    return apotheum


def rp_area(n, s):
    """
    input: integer number of sides n and numeric side length s.
    returns the area of a regular polygon with n sides of length n.
    
    Consider the area of one 'pie piece': the area of the triangle formed
    against one side of the polygon by drawing line from the vertex on either
    end of the side back to the center.  Call the length of the apotheum, which
    is also the height of that triangle, a.  The length of the base of that
    triangle is s.  Thus the area of that triangle A_t = (1/2)*a*s.
    There are n such triangle in the polygon.  Therefore the area of the
    polygon A_p = (n*a*s) / 2.  Since the permimeter of the polygon p = ns,
    we can say that
           p*a
    A_p = ------
            2
    """
    if debug is True: print('entering rp_area with n', n, ' and s', s)
    perimeter = rp_perimeter(n, s)
    apotheum = rp_apotheum(n, s)
    area = perimeter * apotheum / 2
    if debug is True: print('exit rp_area and return area', area)
    return area

def rp_sum(n, s):
    """
    input: integer number of sides n and numeric side length s.
    returns the sum of the perimeter^2 and the area of a regular polygon with
    n sides of length s.
    """
    if debug is True: print('entering rp_sum with n', n, ', and s', s)
    sum = round(rp_area(n, s) + rp_perimeter(n, s)**2, 4)
    if debug is True: print('exit rp_sum and return sum', sum)
    return sum


# If cerit_polygon is called directly and test is set to True, run test code:
if __name__ == '__main__' and test is True:
    n = int(input('enter number of sides n: '))
    s = float(input('enter side length s: '))
    area = rp_area(n, s)
    sum = rp_sum(n, s)
    print('The sum of the squared perimeter and area of the reg poly is', sum)
    

    