"""
A tree that can be searched resursively.
"""

class Tree:
    def __init__(self, key, data):
        "Create a new Tree object with empty L & R subtrees."
        self.key = key
        self.left = self.right = None
        self.data = data
    def insert(self, key, data):
        "Insert a new element into the tree in the correct position."
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Tree(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Tree(key, data)
        else:
            raise ValueError("Attempt to insert duplicate value")
    def walk(self):
        "Generate the keys from the tree in sorted order."
        if self.left:
            for n in self.left.walk():
                yield n
        yield self.key
        if self.right:
            for n in self.right.walk():
                yield n
    def find(self, key):
        """"Find the value for any given key, if key is not found a KeyError
        is raised"""
        r = self.finder(key)
        if not r:
            raise KeyError('Invalid key')
        else:
            return r
          
    def finder(self, key):
        if self.left:
            data = self.left.finder(key)
            if data:
                return data
        if self.key == key:
            return (self.data)
        if self.right:
            data = self.right.finder(key)
            if data:
                return data

if __name__ == '__main__':
    t = Tree("D","4")
    for c,v in zip("BJQKFAC","2687513"):
        t.insert(c,v)
    for c in "ABCDFJKQ":
        print(t.find(c))
    try:
        t.find('key')
    except KeyError as e:
        print('Key Error')

