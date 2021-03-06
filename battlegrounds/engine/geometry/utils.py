from .vector import Vector


def _det(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        total = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            total += mul * _det(m, sign * matrix[0][i])
        return total


def orient(a, b, c):
    "Determines the position of point c relative to the directed line\
    formed by points a and b.\
    If the return value is greater than 0, point c is to its left,\
    if less than 0, it is to the right,\
    and 0 means it is located on the line."

    return a.x * (b.y - c.y) - a.y * (b.x - c.x) + b.x * c.y - b.y * c.x


def incircle(a, b, c, d):
    "Determines whether point d lies within the circle formed \
    by points a, b, and c.\
    If the return value is greater than 0, point d is inside the circle,\
    if less than 0, it is outside, and 0 means the four points are cocircular."

    ort = orient(a, b, c)

    if (ort == 0):
        raise ValueError("Points a, b, and c are colinear and cannot form\
            a circle.")
    elif (ort > 0):
        return _det([[a.x, a.y, a.x * a.x + a.y * a.y, 1],
                    [b.x, b.y, b.x * b.x + b.y * b.y, 1],
                    [c.x, c.y, c.x * c.x + c.y * c.y, 1],
                    [d.x, d.y, d.x * d.x + d.y * d.y, 1]], 1)
    else:
        return ((-1) * _det([[a.x, a.y, a.x * a.x + a.y * a.y, 1],
                            [b.x, b.y, b.x * b.x + b.y * b.y, 1],
                            [c.x, c.y, c.x * c.x + c.y * c.y, 1],
                            [d.x, d.y, d.x * d.x + d.y * d.y, 1]], 1))


def seg_distance(a, b, c):
    "Calculates the distance between segment AB and point C."
    return c.distance(seg_closest(a, b, c))


def seg_closest(a, b, c):
    "Calculates the closest point on segment AB to point C."
    ab = b - a
    ac = c - a
    len2_ab = ab.length2()
    if len2_ab == 0:
        return a
    t = max(0, min(1, ab.dot(ac) / len2_ab))
    c_proj = a + t * ab
    return c_proj


def _x_op(v):
    return v.x


def _y_op(v):
    return v.y


def min_vector(*args):
    """ Returns min by x and y axes
    """
    return Vector(
        min(args, key=_x_op).x,
        min(args, key=_y_op).y
    )


def max_vector(*args):
    """ Returns max by x and y axes
    """
    return Vector(
        max(args, key=_x_op).x,
        max(args, key=_y_op).y
    )
