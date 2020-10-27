class vector:
    def __init__(self, inlist = [], defsize = 0, defval = None, isUnbounded = False, capFunc = lambda cap:cap+10, truesize = None):
        """Use keyword arguments.
        Don't enter a truesize value - this is used by vector when performing deepcopy.\n
        inlist: list with which to be initialized\n
        defsize: default size; if less than len(inlist), will be ignored\n
        defval: value with which to populate empty indices\n
        isUnbounded: enter true if you wish vector to expand for out-of-bounds list access\n
        capFunc: function for calculating excess capacity when vector expands; takes new size as input and returns new capacity"""
        
        self.arr = inlist.copy()
        self.arr += [defval] * (defsize - len(inlist))
        self.size = self.cap = len(self.arr)
        self.defval = defval
        self.isUnb = isUnbounded
        self.capFunc = capFunc
        if truesize != None:
            self.size = truesize

    def __getitem__(self, key):
        if isinstance(key, slice):
            indices = range(*key.indices(self.size))
            return [self.arr[i] for i in indices]
        if key < 0:
            raise IndexError("key less than 0")
        if key >= self.size:
            if self.isUnb and key >= self.cap:
                self._copy(key)
            else:
                raise IndexError("key greater than size")
        return self.arr[key]

    def __setitem__(self, key, value):
        if key < 0:
            raise IndexError("key less than 0")
        if key >= self.cap:
            self.__copy(key)
        self.arr[key] = value
        if key >= self.size:
            self.size = key+1

    def insert(self, key, value):
        if key < 0 or key > self.size:
            raise IndexError("key out of bounds")
        if key == self.size:
            self.append(value)
        for i in range(self.size-1, key-1, -1):
            self.__setitem__(i+1, self.arr[i])
        self.__setitem__(key, value)
        self.size += 1

    def append(self, value):
        self.__setitem__(self.size, value)

    def __delitem__(self, key):
        if key >= self.size or key < 0:
            raise IndexError("key out of bounds")
        for i in range(key, self.size-1):
            self.arr[i] = self.arr[i+1]
        self.arr[self.size-1] = self.defval
        self.size -= 1

    def remove(self, key):
        if key < 0 or key >= self.size:
            raise IndexError("key out of bounds")
        for i in range(key, self.size-1):
            self.arr[i] = self.arr[i+1]
        self.size -= 1

    def __add__(self, other):
        ans = []
        ans += self.arr[0:self.size]
        ans += other[0:len(other)]
        return vector(inlist=ans)

    def __iadd__(self, other):
        size2 = len(other)
        for i in range(0, size2):
            self.__setitem__(i+self.size, other[i])
        self.size += size2
        return self

    def __mul__(self, n):
        return vector(inlist=self.arr[0:self.size] * n, defval=self.defval)
    
    def __imul__(self, n):
        return self.__mul__(n)

    def __eq__(self, other):
        if self.size != len(other):
            return False
        for i in range(0, self.size):
            if self.arr[i] != other[i]:
                return False
        return True

    def _copy(self, index):
        temp = self.arr
        self.arr = [self.defval] * (self.capFunc(index+1))
        for i in range(0, self.size):
            self.arr[i] = temp[i]
        self.size = index+1
        self.cap = self.capFunc(index+1)

    def __len__(self):
        return self.size

    def __str__(self):
        return "["+", ".join(map(str, self.arr[0:self.size]))+"]"

    def __contains__(self, item):
        return item in self.arr[0:self.size]

    def count(self, item):
        count = 0
        for i in range(0, self.size):
            if self.arr[i] == item:
                count+=1
        return count

    def index(self, item, beg, end):
        for i in range(max(0, beg), min(self.size, end)):
            if self.arr[i] == item:
                return i
        return None

    def __copy__(self):
        return vector(inlist=self.arr[0:self.size], defval=self.defval)

    def copy(self):
        return self.__copy__()

    def __deepcopy__(self, memodict={}):
        return vector(inlist=[x.__deepcopy__(memodict) for x in self.arr], defval=self.defval, truesize=self.size)

    def __iter__(self):
        return vector.iterator(self).__iter__()
    
    def __reversed__(self):
        return vector.iteratorReversed(self, self.size).__iter__()


    class iterator:
        def __init__(self, vector):
            self.vect = vector
            self.curr = 0

        def __iter__(self):
            return self
        
        def __next__(self):
            if self.curr >= self.vect.size:
                raise StopIteration
            temp = self.vect[self.curr]
            self.curr+=1
            return temp

    class iteratorReversed:
        def __init__(self, vector, size):
            self.vect = vector
            self.curr = size-1

        def __iter__(self):
            return self

        def __next__(self):
            if self.curr <= 0:
                raise StopIteration
            temp = self.vect[self.curr]
            self.curr-=1
            return temp


if __name__ == "__main__":
    b = [0,1,2,3,4,5]
    print(b[0:6:2])
    b = vector(inlist=b)
    print(b[1:4])
    print(b[0:8])
    print(b[10:0:-1])
    if 10 in b:
        print("yes")
    else:
        print("no")
    print(b)
    c = b.copy()
    print(c)
    d = vector()
    d[9] = 12
    d[9] <- 12