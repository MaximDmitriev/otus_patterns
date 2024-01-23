from typing import List
from math import sqrt, isnan, isinf

epsilon = 1e-05

def solve(a: float, b: float, c: float) -> List[float]:
    for k in [a, b, c]:
        if k == float('-inf') or isnan(k) or isinf(k):
            raise TypeError('invalid type')

    if abs(a) <= epsilon:
        raise ValueError('"a" can not be equal 0')

    discriminant = b*b - 4*a*c

    if discriminant < 0:
        return []

    if abs(discriminant) <= epsilon and discriminant >= 0:
        x = (-b + sqrt(discriminant))/ 2 * a

        return [x, x]
    
    x1 = (-b + sqrt(discriminant))/ 2 * a
    x2 = (-b - sqrt(discriminant))/ 2 * a

    return [x1, x2]

