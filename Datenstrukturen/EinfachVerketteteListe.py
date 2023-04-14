import random


class ListElement:
    def __init__(self, obj):
        self.obj = obj
        self.nextElement = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.obj)

    def get_next_element(self):
        return self.nextElement

    def set_next_element(self, nextElement):
        self.nextElement = nextElement

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.obj < other.obj
        return False

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.obj == other.obj
        return False

    def __hash__(self):
        return hash(self.obj)


class EinfachVerketteteListeIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current
            self.current = self.current.get_next_element()
            return item


class EinfachVerketteteListe:
    head = ListElement(None)

    def append(self, obj):
        new_element = ListElement(obj)
        if self.head.obj is None:
            self.head = new_element
            return
        last_element = self.get_last_element()
        last_element.set_next_element(new_element)

    # insert new object after first occurrence of previous object
    def insert(self, prev_obj, new_obj):
        element = self.head
        while element and element.obj is not prev_obj.obj:
            element = element.get_next_element()
        new_element = ListElement(new_obj)
        next_element = element.get_next_element()
        element.set_next_element(new_element)
        new_element.set_next_element(next_element)

    # does nothing if only head is in linked list!
    def delete_all(self, obj):
        element = self.head
        while element.get_next_element():
            if element.get_next_element().obj is obj:
                if element.get_next_element().get_next_element():
                    element.set_next_element(element.get_next_element().get_next_element())
                else:
                    element.set_next_element(None)
                    break
            element = element.get_next_element()

    def delete(self, obj):
        element = self.head
        if not element.get_next_element():
            self.head = None
            return
        while element.get_next_element():
            if element.get_next_element().obj is obj:
                if element.get_next_element().get_next_element():
                    element.set_next_element(element.get_next_element().get_next_element())
                else:
                    element.set_next_element(None)
                    break
                return
            element = element.get_next_element()

    def find(self, obj):
        element = self.head
        while element:
            if element.obj is obj:
                return True
            element = element.get_next_element()
        return False

    def __getitem__(self, index):
        if index < 0:
            raise IndexError("Do not use negative indices!")
        element = self.head
        counter = 0
        while element:
            if counter == index:
                return element
            counter += 1
            if element.get_next_element():
                element = element.get_next_element()
            else:
                raise IndexError("Index out of bounds at index {0}!".format(counter))

    def set_head(self, new_head):
        self.head.obj = new_head

    def get_first_element(self):
        return self.head

    def get_last_element(self):
        element = self.head
        while element.get_next_element():
            element = element.get_next_element()
        return element

    def count(self, obj):
        element = self.head
        counter = 0
        if element.obj == obj:
            counter += 1
        while element.get_next_element():
            if element.get_next_element().obj == obj:
                counter += 1
            element = element.get_next_element()
        return counter

    def extends(self, linked_list):
        if type(linked_list) is not EinfachVerketteteListe:
            raise TypeError("List is not a LinkedList!")
        element = linked_list.get_first_element()
        while element:
            self.append(element)
            element = element.get_next_element()

    def __str__(self):
        element = self.head
        elements = []
        while element:
            elements.append(element.obj)
            element = element.nextElement
        return "{}".format(elements)

    def __iter__(self):
        return EinfachVerketteteListeIterator(self.head)

    def __reversed__(self):
        previous = None
        element = self.head
        while element.nextElement:
            tmp = element.nextElement
            element.nextElement = previous
            previous = element
            element = tmp
        element.nextElement = previous
        self.head = element
        return self

    def __len__(self):
        if self.head is None:
            return 0
        element = self.head
        length = 0
        while element:
            length += 1
            element = element.nextElement
        return length

    def shuffle(self):
        indices = list(range(self.__len__()))
        random.shuffle(indices)
        new_linked_list = EinfachVerketteteListe()
        for index in indices:
            new_linked_list.append(self.__getitem__(index))
        return new_linked_list
