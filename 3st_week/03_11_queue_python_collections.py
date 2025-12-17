from collections import deque
from queue import Queue

queue = deque()
queue.append(3)
queue.append(4)
print(queue.popleft())