class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        return str(self.data)

class DoppeltVerketteteListe:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_head(self, data):
        if self.head is None:
            # erstes Node auf Wert setzen
            self.head = self.tail = Node(data)
        else:
            new_head = Node(data=data, next=self.head)
            self.head.prev = self.head = new_head

    def add_after_node(self, data, node): 
        if self.head is None: 
            self.head = self.tail = Node(data)
        else: 
            searching_node = self.head
            while searching_node is not None: 
                if searching_node.data == node: 
                    break
                searching_node = searching_node.next
            if searching_node is None: 
                raise Exception("Node is not exisiting in this list!")
            new_node = Node(data=data, prev=searching_node, next=searching_node.next)
            searching_node.next = new_node
            if new_node.next == None: 
                self.tail, new_node = new_node, self.tail
            
    def add_tail(self, data):
        if self.tail is None:
            # erstes Node auf Wert setzen
            self.head = self.tail = Node(data)
        else:
            new_tail = Node(data=data, prev=self.tail)
            self.tail.next = self.tail = new_tail


    def delete_node(self, node): 
        if self.head.data == node:
            self.head = self.head.next
            return
        if self.tail.data == node: 
            self.tail = self.tail.prev
            self.tail.next = None
            return
        
        element_head = self.head
        element_tail = self.tail

        while element_head.next and element_tail.prev and element_head != element_tail: 
            if element_head.next.data is node:
                if element_head.next.next:
                    element_head.next = element_head.next.next
                else:
                    element_head.next = None
                    break
                return
            element_head = element_head.next
            
            if element_tail == element_head: 
                break

            if element_tail.prev.data is node:
                if element_tail.prev.prev:
                    element_tail.prev = element_tail.prev.prev
                else:
                    element_tail.prev = None
                    break
                return
            element_tail = element_tail.prev


    def sum(self): 
        if self.head is None:
            return 0
        mean = 0
        element_head = self.head
        element_tail = self.tail
        if not type(element_head.next.data) == int and not type(element_head.next.data) == float and \
            not type(element_tail.next.data) == int and not type(element_tail.next.data) == float:     
            raise Exception("Node not an Integer or Float!")
        mean += element_head.data + element_tail.data
        steps = 0
        while element_head.next and element_tail.prev and element_head != element_tail: 
            steps += 1
            if not type(element_head.next.data) == int and not type(element_head.next.data) == float:     
                raise Exception("Node not an Integer or Float!")
            mean += element_head.next.data
            
            element_head = element_head.next
            if element_tail == element_head: 
                break
            mean += element_tail.prev.data
            if not type(element_tail.prev.data) == int and not type(element_tail.prev.data) == float:     
                raise Exception("Node not an Integer or Float!")
            element_tail = element_tail.prev
        return mean
    


    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __reversed__(self):
        current = self.tail
        while current  is not None:
            yield current
            current = current.prev

double_linked_list = DoppeltVerketteteListe()

double_linked_list.add_head(1)
double_linked_list.add_tail(3)



for node in double_linked_list:
    print(node)

print()
print(double_linked_list.sum())
