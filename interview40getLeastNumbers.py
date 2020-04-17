class Solution(object):
    def getLeastNumbers(self, arr, k):
        def helper(arr, low, high, k):
            i = low
            j = high
            if i == j:
                return
            temp = arr[i]
            while i < j:
                while i < j and arr[j] > temp:
                    j -= 1
                if i < j:
                    arr[i] = arr[j]
                while i < j and arr[i] <= temp:
                    i += 1
                if i < j:
                    arr[j] = arr[i]
            arr[i] = temp
            if i == k:
                return
            elif i > k:
                helper(arr, low, i - 1, k)
            else:
                helper(arr, i + 1, high, k)
        helper(arr, 0, len(arr) - 1, k - 1)
        return arr[:k]
