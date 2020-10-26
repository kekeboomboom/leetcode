class Solution_190:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret

    def reverseBits2(self, n):
        result = 0
        for i in range(32):
            result = (result << 1) + (n & 1)
            n >>= 1
        return result


if __name__ == '__main__':
    print(Solution_190().reverseBits(4294967293))
