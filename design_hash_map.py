"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
"""

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.map = [None]*self.size
    
    def __hash(self, key):
        obj = str(key)
        som = 0
        for i in obj: som+=ord(i);
        return som

    def put(self, key: int, value: int) -> None:
        hashed_key = self.__hash(key)
        if self.map[hashed_key]==None:
            self.map[hashed_key]=[[key,value],]
        else:
            for m in self.map[hashed_key]:
                if m[0]==key:
                    m[1]=value; return
            self.map[hashed_key].append([key,value])

    def get(self, key: int) -> int:
        hashed_key = self.__hash(key)
        if self.map[hashed_key]!=None:
            for m in self.map[hashed_key]:
                if m[0]==key: return m[1]
        return -1

    def remove(self, key: int) -> None:
        hashed_key = self.__hash(key)
        if self.map[hashed_key]!=None:
            m = 0
            while m< len(self.map[hashed_key]):
                if self.map[hashed_key][m][0]==key:
                    del self.map[hashed_key][m]
                m+=1
