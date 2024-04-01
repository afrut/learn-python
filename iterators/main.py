class _Node:
    """
    _Node for linked-list implementation
    """

    def __init__(self, value: int = None):
        self.value = value
        self.next = None


# A linked-list. This is the container data type that needs an iterator.
class LinkedList:
    # Class for iterator object that needs to be returned by __iter__().
    class _LinkedListIterator:
        def __init__(self, root: _Node):
            self.last = root

        def __iter__(self):
            # An iterator object must be able to return itself
            return self

        def __next__(self):
            # An iterator must have a next object that returns the next element
            if self.last.value is None:
                raise StopIteration
            ret = self.last.value
            self.last = self.last.next
            return ret

    def __init__(self):
        self.last = _Node()
        self.root = self.last
        self.N = 0

    def append(self, x: int):
        self.last.value = x
        self.last.next = _Node()
        self.last = self.last.next
        self.N += 1

    def __iter__(self):
        # An iterable container must have an __iter__() method that returns an
        # iterator object
        return self._LinkedListIterator(self.root)


# A class that returns an iterator object
class MyIterator:
    def __init__(self):
        self.looped = False
        self.x = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.x < 0:
            raise StopIteration

        ret = self.x

        # Update for next value
        if self.looped:
            self.x -= 1
        else:
            self.x += 1

        # Check if counting back to 0
        if self.x == 10:
            self.looped = True
        return ret


# Generators can also be used to return objects. See generators.

if __name__ == "__main__":
    # Loop through a simple iterator object
    it = MyIterator()
    for x in it:
        x

    # Use an iterable container
    ll = LinkedList()
    for x in range(3):
        ll.append(x)
    for x in ll:
        print(x)
