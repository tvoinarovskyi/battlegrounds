import unittest

from engine.geometry import Circle
from engine.geometry import Vector
from engine.geometry.aabb import AABB


class TestAABB(unittest.TestCase):

    def test_dist(self):
        a = Vector(2, 2)
        b = Vector(6, 4)
        rect = AABB(a, b)

        self.assertEqual(rect.distance2(Vector(0, 0)), 8)
        self.assertEqual(rect.distance2(a), 0)
        self.assertEqual(rect.distance2(Vector(3, 3)), 0)
        self.assertEqual(rect.distance2(Vector(4, 3)), 0)
        self.assertEqual(rect.distance2(Vector(8, 5)), 5)
        self.assertEqual(rect.distance2(Vector(1, -1)), 10)
        self.assertEqual(rect.distance2(Vector(4, 1)), 1)
        self.assertEqual(rect.distance2(Vector(9, 3)), 9)
        self.assertEqual(rect.distance2(Vector(5, 5)), 1)
        self.assertEqual(rect.distance2(Vector(0, 4)), 4)

        self.assertEqual(rect.distance(Vector(0, 4)), 2)
        self.assertEqual(rect.distance(Vector(9, 3)), 3.0)

    def test_contains(self):
        a = Vector(2, 2)
        b = Vector(6, 4)
        rect = AABB(a, b)

        self.assertEqual(rect.contains(a), True)
        self.assertEqual(rect.contains(b), True)
        self.assertEqual(rect.contains(Vector(3, 3)), True)
        self.assertEqual(rect.contains(Vector(-1, -1)), False)
        self.assertEqual(rect.contains(Vector(213132534, -9843574398)), False)

    def test_intersects(self):
        rect = AABB(Vector(2, 2), Vector(6, 4))
        zr = Vector(0, 0)

        self.assertEqual(rect.intersects(Circle(zr, 1)), None)
        self.assertEqual(rect.intersects(Circle(Vector(6, 6.0001), 2)), None)

        self.assertEqual(rect.intersects(AABB(zr, Vector(1, 2))), None)
        self.assertEqual(rect.intersects(AABB(zr, Vector(3, 2))), None)