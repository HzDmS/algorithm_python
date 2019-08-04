""" Exploring hash function. """


class Node(object):

    """ Data node in a hash map.

    Attributes
    ----------
    val: value in this node.
    next: next node.

    Methods
    -------
    get_val(): return the value of val.
    get_next(): return the next node.
    set_next(node): set the next node.

    """

    def __init__(self, val):

        """ Init.

        Parameters
        ----------
        val: value stored in this node.

        """
        self.val = val
        self.next = None

    def get_val(self):

        """ Return the value.

        Returns
        -------
        self.val

        """

        return self.val

    def set_next(self, node):

        """ Set the next node.

        Parameters
        ----------
        node: Node instance.

        """

        self.next = node

    def get_next(self):

        """ Return the next node.

        Returns
        -------
        self.next

        """

        return self.next


class HashMap(object):

    """ HashMap.

    Methods
    -------
    insert(key, val): insert a key-value pair into the hash map.
    search(val): search val in the hash map.
    delete(val): delete val in the hash map.

    """

    def __init__(self, base=100):
        self.values = [None] * base
        self.base = base

    def hash(self, val):

        """ Hash function.

        Parameters
        ----------
        val: int.

        Returns
        -------
        hash value of the val.

        """

        return val % self.base

    def insert(self, val):

        """ Insert a key-value pair into the hash map.

        Parameters
        ----------
        key: int.
        val: int.

        """

        key = self.hash(val)
        if not self.values[key]:
            self.values[key] = [val]
        else:
            self.values[key].append(val)

    def search(self, val):

        """ Search val in the hash map.

        Parameters
        ----------
        val: int.

        Returns
        -------
        bool, True if val is found in the hash map, else False.

        """

        key = self.hash(val)
        for element in self.values[key]:
            if element == val:
                return True
        return False

    def delete(self, val):

        """ Delete val in the hash map.

        Parameters
        ----------
        val: int.

        Returns
        -------
        bool, True if val is found and successfully deleted, else False.

        """

        key = self.hash(val)
        for element in self.values[key]:
            if element == val:
                self.values[key].remove(val)
                print("{} is deleted!".format(val))
                return True
        return False


class HashMapLinkedList(object):

    """ HashMap.

    Methods
    -------
    insert(key, val): insert a key-value pair into the hash map.
    search(val): search val in the hash map.
    delete(val): delete val in the hash map.

    """

    def __init__(self, base=100):
        self.values = [None] * base
        self.base = base

    def hash(self, val):

        """ Hash function.

        Parameters
        ----------
        val: int.

        Returns
        -------
        hash value of the val.

        """

        return val % self.base

    def insert(self, val):

        """ Insert a key-value pair into the hash map.

        Parameters
        ----------
        key: int.
        val: int.

        """

        key = self.hash(val)
        new_node = Node(val)
        if not self.values[key]:
            self.values[key] = new_node
        else:
            node = self.values[key]
            while node.get_next():
                node = node.get_next()
            node.set_next(new_node)

    def search(self, val):

        """ Search val in the hash map.

        Parameters
        ----------
        val: int.

        Returns
        -------
        bool, True if val is found in the hash map, else False.

        """

        key = self.hash(val)
        node = self.values[key]
        while node:
            if node.val == val:
                return True
            node = node.get_next()
        return False

    def delete(self, val):

        """ Delete val in the hash map.

        Parameters
        ----------
        val: int.

        Returns
        -------
        bool, True if val is found and successfully deleted, else False.

        """

        key = self.hash(val)
        node = self.values[key]
        pre = None
        while node:
            if node.val == val:
                if not pre:
                    self.values[key] = node.get_next()
                else:
                    pre.set_next(node.get_next())
                print("{} is deleted!".format(val))
                return True
            pre = node
            node = node.get_next()
        return False


if __name__ == "__main__":

    import random

    hash_map = HashMap(100)
    hash_map_ll = HashMapLinkedList(100)

    for i in range(1000):
        val = random.randint(0, 100)
        hash_map.insert(val)
        hash_map_ll.insert(val)

    target = 42

    print('\n{:*^30}\n'.format(" HashMap "))

    hash_map.insert(target)
    print("{} is in the hash map: {}".format(target, hash_map.search(target)))

    while hash_map.search(target):
        hash_map.delete(target)

    print("{} is in the hash map: {}".format(target, hash_map.search(target)))

    print('\n{:*^30}\n'.format(" HashMapLinkedList "))

    hash_map_ll.insert(target)
    print("{} is in the hash map: {}".format(target, hash_map_ll.search(target)))

    while hash_map_ll.search(target):
        hash_map_ll.delete(target)

    print("{} is in the hash map: {}".format(target, hash_map_ll.search(target)))
