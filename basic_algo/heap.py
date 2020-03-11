class MinHeap():
    def __init__(self):
        self.data = []
        self.count = 0

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def add(self, x):
        self.data.append(x)
        self.count += 1
        idx = self.count - 1
        while idx > 0 and x < self.data[(idx - 1) // 2]:
            self.data[idx] = self.data[(idx - 1) // 2]
            idx = (idx - 1) // 2
            if idx <= 0:
                break
        self.data[idx] = x

    def pop(self):
        if self.count > 0:
            result = self.data[0]
            last = self.data[-1]
            self.data.pop()
            self.count -= 1
            if self.count == 0:
                return result
            idx = 1
            while idx < self.count:
                if idx + 1 < self.count and self.data[idx + 1] < self.data[idx]:
                    idx += 1
                if last > self.data[idx]:
                    self.data[(idx - 1) // 2] = self.data[idx]
                else:
                    break
                idx = idx * 2 + 1
            self.data[(idx - 1) // 2] = last
            return result


if __name__ == '__main__':
    heap = MinHeap()
    heap.add(3)
    print(heap.data)
    heap.add(1)
    print(heap.data)
    heap.add(4)
    print(heap.data)
    heap.add(0)
    print(heap.data)
    heap.add(8)
    print(heap.data)
    heap.add(1)
    print(heap.data)
    heap.add(-4)
    print(heap.data)
    heap.add(83)
    print(heap.data)
    heap.add(11)
    print(heap.data)
    print("====================")
    print(heap.pop())
    print(heap.data)
    print(heap.pop())
    print(heap.data)
    print(heap.pop())
    print(heap.data)
    print(heap.pop())
    print(heap.data)
    print(heap.pop())
    print(heap.data)
    print(heap.pop())
    print(heap.data)
    print(heap.pop())
    print(heap.data)
    print(heap.pop())
    print(heap.data)
    print(heap.pop())
    print(heap.data)



