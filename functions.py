import math as m


def get_D(a, b, c):
    return b ** 2 - 4 * a * c


def solve(a, b, c):

    if a == 0:
        if b == 0:
            if c == 0:
                return ['all']
            else:
                return []
        else:
            return [-c / b]
        
    D = get_D(a, b, c)

    if D < 0:
        return []
    elif D == 0:
        return [-b / (2 * a)]
    else:
        x1 = (-b + m.sqrt(D)) / (2 * a)
        x2 = (-b - m.sqrt(D)) / (2 * a)
        return [x1, x2]
