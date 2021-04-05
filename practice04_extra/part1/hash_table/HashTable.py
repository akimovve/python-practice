from practice04_extra.part1.hash_table.Node import Node


class HashTable:
    def __init__(self, capacity=50):
        self.capacity = capacity
        self.size = 0
        self.n = 0
        self.b = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        return hash(key) % self.capacity

    def get(self, key):
        index = self.hash(key)
        node = self.buckets[index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value

    def add(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]

        if node is None:
            self.buckets[index] = Node(key, value)
            return

        while node.next is not None:
            node = node.next

        node.next = Node(key, value)

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = None

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return None

        result = node.value

        if prev is None:
            self.buckets[index] = node.next
        else:
            prev.next = prev.next.next

        self.size -= 1
        return result

    def size(self):
        return self.size

    def __next__(self):
        if self.n is not None:
            current = self.n
            self.n = self.n.next
            return current.key, current.value

        self.b += 1
        if self.b == self.capacity:
            raise StopIteration
        self.n = self.buckets[self.b]

        return self.__next__()

    def __iter__(self):
        self.b = 0
        self.n = self.buckets[0]
        return self

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.add(key, value)

    def __len__(self):
        return self.size
