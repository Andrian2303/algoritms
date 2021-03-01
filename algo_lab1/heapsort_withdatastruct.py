import sort_counter

class Heap:
    def __init__(self, HeadNode):
        self.root = HeadNode


    @staticmethod
    def heap_sort(array):
        result = []
        our_heap = Heap(Node(array.pop(0)))
        for val in array:
            our_heap.root.add_val(val)
        our_heap.root.rnl(result)
        return result


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def add_val(self, new_val):
        sort_counter.heap_sort_comparisons_counter += 1
        if new_val.max_height > self.val.max_height:
            if self.right:
                sort_counter.heap_sort_swap_counter += 1
                self.right.add_val(new_val)
            else:
                self.right = Node(new_val)

        else:
            if self.left:
                sort_counter.heap_sort_swap_counter += 1
                self.left.add_val(new_val)
            else:
                self.left = Node(new_val)

    def rnl(self, res):
        if self.right:
            self.right.rnl(res)
        res.append(self.val)
        if self.left:
            self.left.rnl(res)