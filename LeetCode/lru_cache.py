#!/usr/bin/env python
#coding: utf-8

class Node:
    def __init__(self, pre, next, value, valid):
        self.pre = pre
        self.next = next
        self.value = value
        self.valid = valid

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.data = {}
        self.count = 0
        self.capacity = capacity
        self.head = Node(None, None, None, None)
        self.tail = Node(None, None, None, None)
        self.head.next = self.tail
        self.tail.pre = self.head
    
    def _addhead(self, node):
        node.pre = self.head
        node.next = self.head.next
        node.pre.next = node
        node.next.pre = node

    def _remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    # @return an integer
    def get(self, key):
        node = self.data.get(key)
        if not node: return -1
        if not node.valid: return -1

        self._remove(node)
        self._addhead(node)
        
        return node.value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.data and self.data[key].valid:
            node = self.data[key]
            node.value = value
            self._remove(node)
            self._addhead(node)
        else:
            node = Node(None, None, value, True)
            self._addhead(node)
            self.data[key] = node
            self.count += 1

            if self.count > self.capacity:
                self.tail.pre.valid = False
                self._remove(self.tail.pre)


if __name__ == '__main__':
    s = LRUCache(2)
    s.set(1, 10)
    assert 10 == s.get(1)
    s.set(2, 20)
    assert 20 == s.get(2)

    s.set(3, 30)
    assert 30 == s.get(3)
    assert -1 == s.get(1)
    assert 20 == s.get(2)

    s.set(3, 40)
    assert 40 == s.get(3)

    s = LRUCache(0)
    s.set(1, 10)
    assert -1 == s.get(1)
