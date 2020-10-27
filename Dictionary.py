from Vector import *

class mydict:
    count = 0

    def __init__(self, pairs = []):
        """pairs is a list of key, value tuples"""
        self.size = len(pairs)
        self.vect = vector(defsize = self.size, defval = [], isUnbounded = True, capFunc = lambda x:x+20)
        for x in pairs:
            self.__setitem__(x[0], x[1])

    def __setitem__(self, key, value):
        if self.__contains__(key):
            del self[key]
        else:
            self.size += 1
        index = key.__hash__()
        self.vect[index].append((key, value, count.copy()))
        count += 1

    def __getitem__(self, key):
        index = key.__hash__()
        if index > len(self.vect):
            return None
        ans = None
        for x in self.vect[index]:
            if x[0] == key:
                ans = x[1]
                break
        return ans

    def __delitem__(self, key):
        index = key.__hash__()
        if index > len(self.vect):
            return
        for x in self.vect[index]:
            if x[0] == key:
                self.vect[index].remove(x)
                self.size -= 1
                break

    def __contains__(self, key):
        index = key.__hash__()
        if index > len(self.vect):
            return False
        for x in self.vect[index]:
            if x[0] == key:
                return True
        return False

    def __missing__(self, key):
        return self.__contains__(key)

    def __len__(self):
        return self.size

    def __str__(self):
        pairiter = internalIterator(self.vect)
        ans = "{"
        for i in range(0, self.size):
            x = pairiter.__next__()
            ans += x[0].__str__() + ": " + x[1].__str__()
            if i < self.size - 1:
                ans += ", "
        return ans + "}"

    def __iter__(self):
        return iterator(self.vect).__iter__()

    def __reversed__(self):
        return iteratorReversed(self.vect)

    def __add__(self, other):
        ans = mydict()
        for x in self.vect:
            for y in x:
                ans[y[0]] = y[1]
        for x in other.vect:
            for y in x:
                ans[y[0]] = y[1]
        return ans

    def __iadd__(self, other):
        for x in other.vect:
            for y in x:
                self.__setitem__(y[0], y[1])
        self.size += len(other.vect)
        return self

    def __copy__(self):
        ans = mydict()
        ans += self
        return ans

    def __deepcopy__(self, memodict = {}):
        ans = mydict()
        for x in self.vect:
            for y in x:
                ans.__setitem__(y[0].__deepcopy__(), y[1].__deepcopy__())
        return ans

    def __eq__(self, other):
        if self.size != len(other):
            return False
        for x in self.vect:
            for y in x:
                if y[0] not in other:
                    return False
                if self.__getitem__(y[0]) != other[y[0]]:
                    return False
        return True


    class iterator:
        def __init__(self, dicto):
            countlist = []
            for x in dicto:
                for y in x:
                    countlist.append((y[1], y[2]))
            countlist.sort(key = lambda x : x[1])
            self.keylist = [x[0] for x in countlist]
            self.curr = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.curr >= len(self.keylist):
                raise StopIteration
            temp = self.keylist[self.curr]
            self.curr += 1
            return temp

    class iteratorReversed:
        def __init__(self, dicto):
            countlist = []
            for x in dicto:
                for y in x:
                    countlist.append((y[1], y[2]))
            countlist.sort(key = lambda x : x[1])
            self.keylist = [x[0] for x in countlist]
            self.curr = len(self.keylist)-1

        def __iter__(self):
            return self

        def __next__(self):
            if self.curr <= 0:
                raise StopIteration
            temp = self.keylist[self.curr]
            self.curr -= 1
            return temp

    class internalIterator:
        """for internal use only"""
        def __init__(self, dicto):
            countlist = []
            for x in dicto:
                for y in x:
                    countlist.append((y[0], y[1], y[2]))
            countlist.sort(key = lambda x : x[2])
            self.pairlist = [(x[0], x[1]) for x in countlist]
            self.curr = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.curr >= len(self.pairlist):
                raise StopIteration
            temp = self.pairlist[self.curr]
            self.curr += 1
            return temp


if __name__ == "__main__":
    b = {1:"one", 3:"three", "[2,3,4]":"array", 2:"two"}
    for x in b:
        print(x)
    print(b)