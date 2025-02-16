def solve_quadratic(a, b, c):
    if a == 0:
        if b != 0:
            return [-c / b]
        elif c == 0:
            return ["инфинити"]
        else:
            return []
    else:
        d = b**2 - 4 * a * c
        if d > 0:
            root1 = (-b - d**0.5) / (2 * a)
            root2 = (-b + d**0.5) / (2 * a)
            return sorted([root1, root2])
        elif d == 0:
            root = -b / (2 * a)
            return [root]
        else:
            return []
