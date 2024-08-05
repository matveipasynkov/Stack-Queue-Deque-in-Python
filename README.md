# Stack-Queue-Deque-in-Python
Implementation of Stack, Queue and Deque in Python
## CustomStack
### Methods
  1) push() - add new element
  2) back() - show the last element
  3) pop() - delete last element
  4) len(Stack object) - returns the size of Stack
### Iterator
#### CustomStackIterator
Enumerates stack's elements, removing them from this stack.
### Exceptions
#### CustomStackOutOfRange
Error that is raised when accessing elements of an empty stack.
## CustomQueue
### Methods
  1) push() - add new element
  2) front() - show the first element
  3) pop() - delete first element
  4) len(Queue object) - returns the size of Queue
### Iterator
#### CustomQueueIterator
Enumerates queue's elements, removing them from this queue.
### Exceptions
#### CustomQueueOutOfRange
Error that is raised when accessing elements of an empty queue.
## CustomDeque
### Methods
  1) push_back() - add new element to the end of the deque.
  2) push_front() - add new element to the beggining of the deque.
  3) pop_back() - delete last element of deque.
  4) pop_front() - delete first element of deque.
  5) front() - show the first element
  6) show the last element
  7) [] operation
### Iterator
#### CustomDequeIterator
Enumerates deque's elements, but doesn't remove elements from this deque.
### Exceptions
#### CustomDequeOutOfRange
Error that is raised when accessing elements of an empty deque.
#### ChangeElementOfDeque
Error that is raised when user is trying to change the element of deque.
