from datetime import datetime

"""
Task class contains properties id, priority, arrival_time, deadline and created by.
"""
class Task:
    def __init__(self, task_id, priority, arrival_time, deadline, created_by):
        self.task_id = task_id           # Unique identifier for the task
        self.priority = priority         # Priority of the task (higher priority = more important)
        self.arrival_time = arrival_time # When the task arrives
        self.deadline = deadline         # Deadline by which the task must be completed
        self.created_by = created_by     # Creator of the task  

    # creating a max-heap where higher priority comes first
    def __lt__(self, other):
        return self.priority < other.priority  


"""
This is the implementation of queue or the scheduler program.
"""
class MaxHeapPriorityQueue:
    def __init__(self):
        # creating an array-based heap as it is more efficient and easy to access.
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _heapify_up(self, index):
        # Ensure the max-heap property is maintained by bubbling the element up.
        while index > 0 and self.heap[self._parent(index)].priority < self.heap[index].priority:
            self.heap[self._parent(index)], self.heap[index] = self.heap[index], self.heap[self._parent(index)]
            index = self._parent(index)

    # Ensure the max-heap property is maintained by bubbling the element down.
    def _heapify_down(self, index):
        largest = index
        left = self._left_child(index)
        right = self._right_child(index)

        if left < len(self.heap) and self.heap[left].priority > self.heap[largest].priority:
            largest = left

        if right < len(self.heap) and self.heap[right].priority > self.heap[largest].priority:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    # This method inserts a new task into the heap.
    def insert(self, task):
        self.heap.append(task)  # Add the task at the end
        self._heapify_up(len(self.heap) - 1)  # Restore the max-heap property
        print(f"Task {task.task_id} inserted with priority {task.priority}")

    # This method removes and returns the task with the highest priority (root of the heap).
    # Item is no longer present once max is extracted.
    def extract_max(self):
        if len(self.heap) == 0:
            return None  # If the heap is empty
        max_task = self.heap[0]
        # Move the last element to the root and heapify down
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        print(f"Extracted task {max_task.task_id} with priority {max_task.priority} created by {max_task.created_by}")
        return max_task

    #Increases the priority of the item/task in queue
    def increase_key(self, task, new_priority):
        if new_priority < task.priority:
            raise ValueError("New priority must be greater than the current priority.")
        task.priority = new_priority
        index = self.heap.index(task)
        self._heapify_up(index)
        print(f"Task {task.task_id} priority increased to {new_priority}")

    #Decreases the priority of an existing task and adjust its position.
    def decrease_key(self, task, new_priority):
        if new_priority > task.priority:
            raise ValueError("New priority must be smaller than the current priority.")
        task.priority = new_priority
        index = self.heap.index(task)
        self._heapify_down(index)
        print(f"Task {task.task_id} priority decreased to {new_priority}")

    #method to check if the heap is empty.
    def is_empty(self):
        return len(self.heap) == 0


# Creating new instance of priority queue
pq = MaxHeapPriorityQueue()

#Creating 3 tasks to simulate the use case.
task1 = Task(1, 5, datetime(2025, 1, 1), datetime(2025, 1, 10), "Bishal")
task2 = Task(2, 3, datetime(2025, 1, 2), datetime(2025, 1, 20), "Bishal1")
task3 = Task(3, 2, datetime(2025, 1, 3), datetime(2025, 1, 15), "Bishal2")

# Insert tasks into the priority queue
pq.insert(task1)
pq.insert(task2)
pq.insert(task3)

# Extract task with max priority
# This should give task 1
pq.extract_max()

# Increase and decrease task priority
pq.increase_key(task2, 7)
pq.increase_key(task3, 9)

#This should give task 3
pq.extract_max()

#The only one left is task 2 now.
pq.extract_max()
#Queue should be empty at the end
if pq.is_empty:
    print("Queue is empty now")
