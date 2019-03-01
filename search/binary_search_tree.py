class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth_first_for_each(self, cb):
        # initialize cb input to self.value
        print(f'before cb: {self.value}')
        cb(self.value)
        # if we are capable of going left
        if self.left:
            # recursively call depth first_ search on left side
            print(f'self.left.value: {self.left.value}')
            self.left.depth_first_for_each(cb)
        # once we have gone furthest left possible, we check if we can go right
        if self.right:
            # recursively call depth first_ search on right side
            print(f'self.right.value: {self.right.value}')
            self.right.depth_first_for_each(cb)

    def breadth_first_for_each(self, cb):
        # initialize cb input to self.value
        print(f'before cb: {self.value}')
        cb(self.value)
        # create an empty queue for level traversal, breadth first search is FIFO
        queue = []
        print(f'queue: {queue}')
        # if we are capable of going left append to queue
        if self.left:
            print(f'self.left.value: {self.left.value}')
            queue.append(self.left)
        # if we are capable of going right append to queue
        if self.right:
            print(f'self.right.value: {self.right.value}')
            queue.append(self.right)
        # while the length of queue is greater than 0 we will pop the node's value in the queue
        while len(queue) > 0:
            # assign the current_queue to the value we pop
            current_queue = queue.pop(0)
            print(f'current_queue: {current_queue.value}')
            # recursively call current_queue value
            cb(current_queue.value)
            # if we are capable of going left from the current queue, append to queue
            if current_queue.left:
                print(f'current_queue.left.value: {current_queue.left.value}')
                queue.append(current_queue.left)
            # if we are capable of going right from the current queue, append to queue
            if current_queue.right:
                print(
                    f'current_queue.right.value: {current_queue.right.value}')
                queue.append(current_queue.right)

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if (value < self.value):
            if not self.left:
                self.left = new_tree
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.left:
            if self.left.contains(target):
                return True
        if self.right:
            if self.right.contains(target):
                return True
        return False

    def get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value
