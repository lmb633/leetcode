class Solution(object):
    def swapNumbers(self, numbers):
        numbers[0], numbers[1] = numbers[1], numbers[0]
        return numbers


class Solution1(object):
    def swapNumbers(self, numbers):
        numbers[0] = numbers[0] + numbers[1]
        numbers[1] = numbers[0] - numbers[1]
        numbers[0] = numbers[0] - numbers[1]
        return numbers


class Solution3(object):
    def swapNumbers(self, numbers):
        numbers[0] = numbers[0] / 2 + numbers[1] / 2
        numbers[1] = numbers[0] - numbers[1] / 2
        numbers[0] = numbers[0] - numbers[1]
        numbers[0] = int(numbers[0] * 2)
        numbers[1] = int(numbers[1] * 2)
        return numbers


class Solution2(object):
    def swapNumbers(self, numbers):
        numbers[0] = numbers[0] ^ numbers[1]
        numbers[1] = numbers[0] ^ numbers[1]
        numbers[0] = numbers[0] ^ numbers[1]
        return numbers
