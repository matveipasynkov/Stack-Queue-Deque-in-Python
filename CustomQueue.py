class CustomQueueOutOfRange(Exception):
    pass


class CustomQueueIterator:
    def __init__(self, queue):
        self.queue = queue

    def __iter__(self):
        return self.queue.front()

    def __next__(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        raise StopIteration


class CustomQueue:
    def __init__(self, *args):
        self.__elements = list(args)

    def __len__(self):
        return len(self.__elements)

    def __iter__(self):
        return CustomQueueIterator(self)

    def push(self, new_element):
        self.__elements.append(new_element)

    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop(0)
        raise CustomQueueOutOfRange("Queue is empty.")

    def front(self):
        if len(self.__elements) > 0:
            return self.__elements[0]
        raise CustomQueueOutOfRange("Queue is empty.")
