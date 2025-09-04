class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a = 0
        b = 0
        if z >= x:
            a = z - x
        else:
            a = x - z

        if z >= y:
            b = z - y
        else:
            b = y - z

        if a > b:
            return 2
        elif b > a:
            return 1
        else:
            return 0