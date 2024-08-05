class CustomStackOutOfRange(Exception):
    pass


class CustomStackIterator:
    def __init__(self, stack):
        self.stack = stack

    def __iter__(self):
        return self.stack.back()

    def __next__(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        raise StopIteration


class CustomStack:
    def __init__(self, *args):
        self.__elements = list(args)

    def __len__(self):
        return len(self.__elements)

    def __iter__(self):
        return CustomStackIterator(self)

    def push(self, new_element):
        self.__elements.append(new_element)

    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        raise CustomStackOutOfRange("Stack is empty.")

    def back(self):
        if len(self.__elements) > 0:
            return self.__elements[-1]
        raise CustomStackOutOfRange("Stack is empty.")
