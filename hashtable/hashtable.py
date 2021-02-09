class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        print(f'{self.key}, {self.value}, {self.next}')


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
            # print(self.capacity)
        else:
            self.capacity = capacity
            # print(self.capacity)

        self.storage = [None]*self.capacity
        self.count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.storage)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        FNV_OFFSET_BASIS = 0xcbf29ce484222325
        FNV_PRIME = 0x100000001b3

        hash = FNV_OFFSET_BASIS

        for c in key:
            hash = hash * FNV_PRIME
            hash = hash ^ ord(c)
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # make use of the Fowler–Noll–Vo_hash_function
        return self.fnv1(key) % self.capacity

        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # hash the key with hash_index function
        key_index = self.hash_index(key)

        # create linked list new value
        """
        [None, None, None, None, None, None, None, None]
        [3, ...., None]

        """

        node = self.storage[key_index]
        new_value = HashTableEntry(key, value)

        self.count += 1

        if node == None:
            self.storage[key_index] = new_value
            if self.get_load_factor() >= 0.7:
                self.resize(self.capacity * 2)
            return

        prev = node

        while node != None:
            if node.key == key:
                node.value = value
                return
            else:
                node = node.next

        prev.next = new_value

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.

        [None, None, None, None, None, None, None, None]
        [3, 4, 5, ..., None]
         |
         56
         |
         43
        """
        # Your code here

        # Again hash key to get index
        key_index = self.hash_index(key)

        # check if found, then delete the key and value at index above

        # self.storage[key_index] = None
        node = self.storage[key_index]
        prev = None

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return None

        else:
            self.count -= 1
            deleted_node = node.value
            if prev is None:
                self.storage[key_index] = node.next

            else:
                prev.next = node.next

            if self.get_load_factor() <= 0.2 and self.capacity // 2 >= MIN_CAPACITY:
                self.resize(self.capacity // 2)

            return deleted_node

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

        """
        [None, None, None, None, None, None, None, None]
        [3, 4, 5, ..., None]

        """

        # Your code here

        # get the index of key by hashing the key
        key_index = self.hash_index(key)
        node = self.storage[key_index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        #store a copy of old storage here
        old_storage = self.storage

        #update to the new capacity 
        self.capacity = new_capacity

        # update storage to have length with new capacity
        self.storage = [None] * self.capacity

        # run through items in old storage and send to updated storage 
        for i in range(len(old_storage)):
            node = old_storage[i]

            if node != None:
                current_node = node

                while current_node != None:
                    self.put(current_node.key, current_node.value)
                    current_node = current_node.next

        return


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
