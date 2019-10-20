class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next


class List:
    def __init__(self):
        self.len = 0
        self.first = None

    def add(self, x, y):
        self.len += 1
        if self.len == 1:
            self.first = Node(x)
        elif y == 1:
            self.first = Node(x, self.first)
        elif 1 < y <= self.len:
            cur = self.first
            k = 2
            while k != y:
                k += 1
                cur = cur.next
            n = Node(x, cur.next)
            cur.next = n
        else:
            print("BAD_add")

    def dele(self, y):
        if y == 1:
            self.first = self.first.next
            self.len -= 1
        elif 1 < y <= self.len:
            cur = self.first
            k = 2
            while k != y:
                k += 1
                cur = cur.next
            cur.next == cur.next.next
            self.len -=1
        else:
            print("BAD_del")
    
    def search(self, x):
        k = 1
        cur = self.first
        while cur.next != None:
            if cur.val == x:
                print(k, end=' ')
            k += 1
            cur = cur.next
        if cur.val == x:
            print(k, end=' ')
        print()


def MakeList(s):
    l = List()
    for i in s:
        l.add(int(i), l.len + 1)
    return l


def sum(s):
    s1, s2 = s.split(' + ')
    l1 = MakeList(s1)
    l2 = MakeList(s2)
    l = List()
    if l1.val > l2.val:
        t = l1
        l1 = l2
        l2 = t
    cur1 = l1.first
    cur2 = l2.first
    mem = 0
    for _ in range(l1.len):
        l.add((cur1.val + cur2.val + mem) % 10, l.len + 1)
        mem = (cur1.val + cur2.val + mem) // 10
        cur1 = cur1.next
        cur2 = cur2.next
    for _ in range(l2.len - l1.len):
        l.add((cur2.val + mem) % 10, l.len + 1)
        mem = (cur2.val + mem) // 10
        cur2 = cur2.next
    if mem != 0:
        l.add(mem, l.len + 1)
    return l
