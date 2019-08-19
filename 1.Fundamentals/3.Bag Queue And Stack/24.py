def remove_after(self, node):
    if node is None or node.next is None:
        pass
    node.next = None
