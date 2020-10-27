class linklist:
    def __init__(self, inlist = []):
        self.size = len(inlist)
        if self.size > 0:
            self.head = node(inlist[0])
            temp = self.head
            for i in range(1, self.size):
                temp.next = node(inlist[i])
                temp = temp.next
        else:
            self.head = None

    def append(self, value):
        self.size += 1
        if self.head == None:
            self.head = node(value)
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = node(value)

    def __iadd__(self, other):
        """if param is an iterable, will append each value; otherwise will append a plain value"""
        try:
            for x in other:
                self.append(x)
        except TypeError:
            self.append(other)

    def __getitem__(self, key):
        if key < 0 or key >= self.size or self.head == None:
            raise IndexError("key out of bounds of linked list")
        temp = self.head
        for i in range(0, key):
            temp = temp.next
        return temp.val

    def __setitem__(self, key, value):
        """functions as an insertion"""
        if key < 0 or key > self.size or self.head == None:
            raise IndexError("key out of bounds of linked list")
        if key == self.size:
            self.append(value)
            return
        temp = self.head
        for i in range(0, key-1):
            temp = temp.next
        temp2 = temp.next
        temp.next = node(value)
        temp.next.next = temp2
        self.size += 1

    def __delitem__(self, key):
        """functions as a removal"""
        if key < 0 or key >= self.size or self.head == None:
            raise IndexError("key out of bounds of linked list")
        if key == 0:
            self.head = self.head.next
            return
        temp = self.head
        for i in range(0, key-1):
            temp = temp.next
        temp.next = temp.next.next

    def __len__(self):
        return self.size

    def __contains__(self, value):
        temp = self.head
        while temp != None:
            if temp.val == value:
                return True
            temp = temp.next
        return False

    def __iter__(self):
        return iterator(self.head).__iter__()

    def __reversed__(self):
        raise TypeError("cannot reverse iterate over a singly-linked list")

    def __eq__(self, other):
        temp = self.head
        for x in other:
            if temp.val != x:
                return False
            temp = temp.next
        return True

    def count(self, value):
        ans = 0
        temp = self.head
        while temp != None:
            if temp.val == value:
                ans += 1
            temp = temp.next
        return ans

    def index(self, value):
        ans = None
        i = 0
        temp = self.head
        while temp != None:
            if temp.val == value:
                ans = i
                break
            temp = temp.next
            i += 1
        return ans

    def __copy__(self):
        ans = linklist()
        temp = self.head
        while temp != None:
            ans.append(temp.val)
            temp = temp.next
        return ans

    def __deepcopy__(self):
        ans = linklist()
        temp = self.head
        while temp != None:
            ans.append(temp.val.__deepcopy__())
            temp = temp.next
        return ans

    class node:
        def __init__(self, value, nextNode = None):
            self.val = value
            self.next = nextNode

    class iterator:
        def __init__(self, head):
            self.curr = head

        def __iter__(self):
            return self

        def __next__(self):
            temp = self.curr
            self.curr = self.curr.next
            return temp