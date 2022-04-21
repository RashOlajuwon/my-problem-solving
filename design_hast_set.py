"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
"""
class MyHashSet:

    def __init__(self):
        self.lst = []

    def add(self, key: int) -> None:
        if not key in self.lst:
            self.lst.append(key)

    def remove(self, key: int) -> None:
        if key in self.lst:
            i = 0
            while i<len(self.lst):
                if self.lst[i]==key:
                    del self.lst[i]
                    break
                i+=1

    def contains(self, key: int) -> bool:
        return True if key in self.lst else False
