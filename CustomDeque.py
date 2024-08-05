class CustomDequeOutOfRange(Exception):
    pass


class ChangeElementOfDeque(Exception):
    pass


class CustomDequeIterator:
    def __init__(self, deque):
        self.deque = deque
        self.counter = 0

    def __iter__(self):
        return self.deque.front()

    def __next__(self):
        if self.counter < len(self.deque):
            value = self.deque[self.counter]
            self.counter += 1
            return value
        raise StopIteration


class CustomDeque:
    def __init__(self, *args):
        self.__elements = list(args)

    def __len__(self):
        return len(self.__elements)

    def __iter__(self):
        return CustomDequeIterator(self)

    def __getitem__(self, key):
        if key >= len(self):
            raise CustomDequeOutOfRange("Deque is empty.")
        return self.__elements[key]

    def __setitem__(self, key, value):
        raise ChangeElementOfDeque("It's impossible to set a new value in deque.")

    def push_back(self, new_element):
        self.__elements.append(new_element)

    def push_front(self, new_element):
        self.__elements = [new_element] + self.__elements

    def pop_back(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        raise CustomDequeOutOfRange("Deque is empty.")

    def pop_front(self):
        if len(self.__elements) > 0:
            return self.__elements.pop(0)
        raise CustomDequeOutOfRange("Deque is empty.")

    def back(self):
        if len(self.__elements) > 0:
            return self.__elements[-1]
        raise CustomDequeOutOfRange("Deque is empty.")

    def front(self):
        if len(self.__elements) > 0:
            return self.__elements[0]
        raise CustomDequeOutOfRange("Deque is empty.")
