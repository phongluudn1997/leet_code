class Tower:
    def __init__(self, index):
        self.index = index
        self.disks = []

    def add(d):
        self.disks.push(d)
    
    def move_top_to(destination):
        top = self.disks.pop()
        destination.add(top)
    
    def move_disks(n, destination, buffer):
        if n > 0:
            self.move_disks(n-1, buffer, destination)
            self.move_top_to(destination)
            buffer.move_disks(n-1, destination, self)

towers = []
for i in range(1, 4):
    towers[i] = Tower(i)

print(towers)