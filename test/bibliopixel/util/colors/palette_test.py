import unittest
from fractions import Fraction

from bibliopixel.util.colors.palette import Palette
from bibliopixel.util.colors.classic import Black, White, Red, Green, Blue


class PaletteTest(unittest.TestCase):
    def test_empty(self):
        p = Palette()
        self.assertEqual(p[0], Black)
        self.assertEqual(p.get(0), Black)
        self.assertEqual(p.get(1), Black)

    def test_single(self):
        p = Palette([Red])
        self.assertEqual(p[0], Red)
        self.assertEqual(p.get(0), Red)
        self.assertEqual(p.get(1), Red)

    def test_get(self):
        p = Palette([Red, Green, Blue], continuous=True)
        result = [p.get(-1 + Fraction(i) / 2) for i in range(12)]
        expected = [
            (0, 170, 85),
            (0, 85, 170),
            (255, 0, 0),
            (170, 85, 0),
            (85, 170, 0),
            (0, 255, 0),
            (0, 170, 85),
            (0, 85, 170),
            (255, 0, 0),
            (170, 85, 0),
            (85, 170, 0),
            (0, 255, 0)]
        self.assertEqual(result, expected)

    def test_get_serpentine(self):
        p = Palette([Red, Green, Blue], serpentine=True, continuous=True)
        result = [p.get(-1 + Fraction(i) / 2) for i in range(12)]
        expected = [
            (85, 170, 0),
            (170, 85, 0),
            (255, 0, 0),
            (170, 85, 0),
            (85, 170, 0),
            (0, 255, 0),
            (0, 170, 85),
            (0, 85, 170),
            (0, 0, 255),
            (0, 85, 170),
            (0, 170, 85),
            (0, 255, 0)
        ]
        self.assertEqual(result, expected)

    def test_double(self):
        p = Palette([Red, Green], continuous=True)

        self.assertEqual(p[0], Red)
        self.assertEqual(p[1], Green)

        result = [p.get(-1 + Fraction(i) / 3) for i in range(12)]
        expected = [
            (127.5, 127.5, 0),
            (85, 170, 0),
            (42.5, 212.5, 0),
            (255, 0, 0),
            (212.5, 42.5, 0),
            (170, 85, 0),
            (127.5, 127.5, 0),
            (85, 170, 0),
            (42.5, 212.5, 0),
            (255, 0, 0),
            (212.5, 42.5, 0),
            (170, 85, 0)
        ]
        self.assertEqual(result, expected)

    def test_double_serpentine(self):
        p = Palette([Red, Green], serpentine=True, continuous=True)

        result = [p.get(-1 + Fraction(i) / 3) for i in range(12)]
        expected = [
            (127.5, 127.5, 0.0),
            (170.0, 85.0, 0.0),
            (212.5, 42.5, 0.0),
            (255.0, 0.0, 0.0),
            (212.5, 42.5, 0.0),
            (170.0, 85.0, 0.0),
            (127.5, 127.5, 0.0),
            (85.0, 170.0, 0.0),
            (42.5, 212.5, 0.0),
            (0.0, 255.0, 0.0),
            (42.5, 212.5, 0.0),
            (85.0, 170.0, 0.0)
        ]
        self.assertEqual(result, expected)

    def test_discontinuous(self):
        colors = [Red, Green, Blue, White]
        p = Palette(colors)

        result = [p.get(Fraction(i) / 2) for i in range(10)]
        expected = [Red, Red, Green, Green, Blue, Blue, White, White, Red, Red]

        self.assertEqual(expected, result)

    def test_discontinuous_serpentine(self):
        colors = [Red, Green, Blue, White]
        p = Palette(colors, serpentine=True)
        self.assertEqual(Green, p.get(7))

        self.assertEqual(Red, p.get(0))
        self.assertEqual(Green, p.get(1))
        self.assertEqual(Blue, p.get(2))
        self.assertEqual(White, p.get(3))
        self.assertEqual(Blue, p.get(4))
        self.assertEqual(Green, p.get(5))
        self.assertEqual(Red, p.get(6))
        self.assertEqual(Green, p.get(7))
        self.assertEqual(Blue, p.get(8))

        self.assertEqual(Red, p.get(0.1))
        self.assertEqual(Green, p.get(1.9))

    def test_continuous(self):
        colors = [Red, Green, Blue, White]
        p = Palette(colors, continuous=True)
        result = [p.get(-1 + Fraction(i) / 3) for i in range(16)]

        expected = [
            (63.75, 63.75, 255.0),
            (127.5, 127.5, 255.0),
            (191.25, 191.25, 255.0),
            (255.0, 0.0, 0.0),
            (191.25, 63.75, 0.0),
            (127.5, 127.5, 0.0),
            (63.75, 191.25, 0.0),
            (0.0, 255.0, 0.0),
            (0.0, 191.25, 63.75),
            (0.0, 127.5, 127.5),
            (0.0, 63.75, 191.25),
            (0.0, 0.0, 255.0),
            (63.75, 63.75, 255.0),
            (127.5, 127.5, 255.0),
            (191.25, 191.25, 255.0),
            (255.0, 0.0, 0.0),
        ]
        self.assertEqual(expected, result)

    def test_continuous_serpentine(self):
        colors = [Red, Green, Blue, White]
        p = Palette(colors, serpentine=True, continuous=True)
        result = [p.get(-1 + Fraction(i) / 3) for i in range(15)]

        expected = [
            (63.75, 191.25, 0.0),
            (127.5, 127.5, 0.0),
            (191.25, 63.75, 0.0),
            (255.0, 0.0, 0.0),
            (191.25, 63.75, 0.0),
            (127.5, 127.5, 0.0),
            (63.75, 191.25, 0.0),
            (0.0, 255.0, 0.0),
            (0.0, 191.25, 63.75),
            (0.0, 127.5, 127.5),
            (0.0, 63.75, 191.25),
            (0.0, 0.0, 255.0),
            (63.75, 63.75, 255.0),
            (127.5, 127.5, 255.0),
            (191.25, 191.25, 255.0)
        ]
        self.assertEqual(expected, result)

    def test_scale(self):
        colors = [Red, Green, Blue, White]
        p = Palette(colors, continuous=False, serpentine=True, scale=3)

        result = [p.get(Fraction(2 * i) / 9) for i in range(25)]
        expected = [
            Red, Red, Green, Blue, Blue, White, Blue, Green,
            Red, Red, Red, Green, Blue, Blue, White, Blue,
            Green, Red, Red, Red, Green, Blue, Blue, White,
            Blue]

        # result2 = [tuple(float(i) for i in c) for c in result]
        # print('', *result2, sep=',\n            ')
        self.assertEqual(expected, result)

    def test_autoscale(self):
        colors = [Red, Green, Blue, White]
        p = Palette(colors, autoscale=True)

        expected = [Red, Red, Green, Green, Blue, Blue, White, White, Red, Red]
        result = [p.get(32 * i, 256) for i in range(10)]
        print(*result, sep='\n')
        self.assertEqual(expected, result)

        result = [p.get(Fraction(i) / 2) for i in range(10)]
        self.assertEqual(expected, result)
