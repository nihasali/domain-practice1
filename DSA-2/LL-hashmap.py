# Step 1: Create a Node for Linked List
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Step 2: Create HashTable Class
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size  # Array of linked lists (initially empty)

    # Hash function (simple one using remainder)
    def _hash(self, key):
        return hash(key) % self.size

    # Insert key-value pair
    def insert(self, key, value):
        index = self._hash(key)
        new_node = Node(key, value)

        if self.table[index] is None:
            # No linked list at this index → just insert
            self.table[index] = new_node
        else:
            # Collision → add to the end of the linked list
            current = self.table[index]
            while current:
                if current.key == key:
                    # Update value if key already exists
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node

    # Search for a value by key
    def get(self, key):
        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None  # Key not found

    # Delete a key
    def delete(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next
        return False


ht = HashTable()

ht.insert("name", "Alice")
ht.insert("age", 25)
ht.insert("city", "New York")

print(ht.get("name"))  # Output: Alice
print(ht.get("age"))   # Output: 25

ht.insert("name", "Bob")  # Update existing key
print(ht.get("name"))  # Output: Bob

ht.delete("age")
print(ht.get("age"))  # Output: None (deleted)

