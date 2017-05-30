class StackNode:
    def __init__(self, value, prev):
        self.prev = prev
        self.value = value


class Stack:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.stack = [None]*3*stack_size
        self.last_index = -1
        self.stack_pointers = [-1, -1, -1]

    def is_empty(self, stack_num):
        return self.stack_pointers[stack_num] == -1

    def memory_is_full(self):
        return self.last_index >= self.stack_size * 3 - 1

    def push(self, stack_num, value):
        self.last_index += 1
        self.stack[self.last_index] = StackNode(value, self.stack_pointers[stack_num])
        self.stack_pointers[stack_num] = self.last_index

    def pop(self, stack_num):
        curr_index = self.stack_pointers[stack_num]
        node = self.stack[curr_index]
        self.stack[curr_index] = None
        prev_index = node.prev
        self.stack_pointers[stack_num] = prev_index
        self.last_index -= 1
        return node.value


class StackQueue:
    def __init__(self):
        self._stack1 = []
        self._stack2 = []

    def _move_to_stack1(self):
        while self._stack2:
            self._stack1.append(self._stack2.pop())

    def add(self, item):
        self._stack2.append(item)

    def remove(self):
        if self._stack1:
            return self._stack1.pop()
        else:
            self._move_to_stack1()
            if not self._stack1:
                raise Exception('StackQueue is empty')
            return self._stack1.pop()

    def peek(self):
        if not self._stack1:
            self._move_to_stack1()
        if not self._stack1:
            raise Exception('StackQueue is empty')
        return self._stack1[-1]

    def is_empty(self):
        return not (self._stack1 or self._stack2)


def sort_stack(stack):
    sorted_stack = []
    if not stack:
        return stack
    for i in range(len(stack)):
        counter = 0
        tmp = stack.pop()
        while sorted_stack and sorted_stack[-1] > tmp:
            stack.append(sorted_stack.pop())
            counter += 1
        sorted_stack.append(tmp)
        while counter > 0:
            sorted_stack.append(stack.pop())
            counter -= 1
    for i in range(len(sorted_stack)):
        stack.append(sorted_stack.pop())
    return stack


import random
stack = [random.randint(-1000, 1000) for i in range(100000)]
stack_copy = stack[:]
stack_copy.sort(reverse=True)
print(stack_copy == sort_stack(stack))
