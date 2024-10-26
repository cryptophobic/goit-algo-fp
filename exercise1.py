class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        curr = self.head
        prev = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


def insertion_sort(linked_list):
    sorted_list = LinkedList()
    current = linked_list.head

    while current:
        # Додаємо поточний елемент до відсортованого списку
        if sorted_list.head is None or sorted_list.head.data >= current.data:
            new_node = Node(current.data)
            new_node.next = sorted_list.head
            sorted_list.head = new_node
        else:
            search = sorted_list.head
            while search.next and search.next.data < current.data:
                search = search.next
            new_node = Node(current.data)
            new_node.next = search.next
            search.next = new_node

        current = current.next

    return sorted_list


def merge_sorted_lists(list1, list2):
    # Створюємо новий однозв'язний список для зберігання результату
    merged_list = LinkedList()
    current1 = list1.head
    current2 = list2.head

    # Вказівник на кінець нового списку
    tail = None

    # Об'єднуємо два списки
    while current1 and current2:
        if current1.data <= current2.data:
            new_node = Node(current1.data)
            current1 = current1.next
        else:
            new_node = Node(current2.data)
            current2 = current2.next

        # Додаємо новий вузол до злитого списку
        if merged_list.head is None:
            merged_list.head = new_node
        else:
            tail.next = new_node
        tail = new_node

    # Якщо залишилися елементи в list1
    while current1:
        new_node = Node(current1.data)
        if merged_list.head is None:
            merged_list.head = new_node
        else:
            tail.next = new_node
        tail = new_node
        current1 = current1.next

    # Якщо залишилися елементи в list2
    while current2:
        new_node = Node(current2.data)
        if merged_list.head is None:
            merged_list.head = new_node
        else:
            tail.next = new_node
        tail = new_node
        current2 = current2.next

    return merged_list


llist = LinkedList()
llist2 = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)
# Вставляємо вузли в початок
llist2.insert_at_beginning(6)
llist2.insert_at_beginning(11)
llist2.insert_at_beginning(16)

# Вставляємо вузли в кінець
llist2.insert_at_end(21)
llist2.insert_at_end(26)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()
llist.reverse()
print("\n")
llist.print_list()
soprted = insertion_sort(llist)
print("\n")
soprted.print_list()
soprted2 = insertion_sort(llist2)
print("\n")

result = merge_sorted_lists(soprted, soprted2)
result.print_list()
