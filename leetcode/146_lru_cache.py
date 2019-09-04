class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()

    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        for keyi in self.cache.keys():
            self.cache[keyi][1] += 1
        self.cache[key][1] = 0        
        print(self.cache)
        return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache.keys() and len(self.cache) == self.capacity:
            remove_item = max(self.cache, key=lambda i: self.cache[i][1])
            self.cache.pop(remove_item)
        for keyi in self.cache.keys():
            self.cache[keyi][1] += 1
        self.cache[key] = [value, 0]
        print(self.cache)


from collections import deque

class LRUCache2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.order = deque()

    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)
        self.cache[key] = value
        self.order.append(key)
        if len(self.cache) > self.capacity:
            self.cache.pop(self.order.popleft())


if __name__ == '__main__':
    obj = LRUCache(2)
    obj.get(2)
    obj.put(2, 6)
    obj.get(1)
    obj.put(1, 5)
    obj.put(1, 2)
    print(obj.get(1))
    # print(obj.cache)
    print(obj.get(2))
