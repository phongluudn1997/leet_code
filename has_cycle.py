class Solution:
    def has_cycle(self, head):
        node_seen = set()
        while not head:
            if head in node_seen:
                return True
            node_seen.add(head)
        return False
