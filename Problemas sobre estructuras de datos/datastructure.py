from collections import deque
from sys import stdin


def delete_stack(stack, element):
    return stack.pop() == element if stack else False


def delete_queue(queue, element):
    return queue.popleft() == element if queue else False


def delete_priority(priority, element):
    try:
        max_val = max(priority)
        priority.remove(max_val)
        return max_val == element
    except:
        return False


def load_structures(number_operations):
    stack = deque()  # creo una pila
    queue = deque()  # creo una cola
    priority_queue = []  # creo una cola con prioridad
    can_be_stack = True
    can_be_queue = True
    can_be_priority_queue = True
    for i in range(number_operations):
        operation = stdin.readline().strip().split()
        element = int(operation[1])
        if int(operation[0]) == 1:
            stack.append(element)
            queue.append(element)
            priority_queue.append(element)
        else:
            if can_be_stack:
                can_be_stack = delete_stack(stack, element)
            if can_be_queue:
                can_be_queue = delete_queue(queue, element)
            if can_be_priority_queue:
                can_be_priority_queue = delete_priority(priority_queue, element)
    if can_be_stack and not can_be_queue and not can_be_priority_queue:
        return "stack"
    if can_be_queue and not can_be_stack and not can_be_priority_queue:
        return "queue"
    if can_be_priority_queue and not can_be_stack and not can_be_queue:
        return "priority queue"
    if can_be_stack or can_be_queue or can_be_priority_queue:
        return "not sure"
    return "impossible"


for line in stdin:
    print(load_structures(int(line)))
