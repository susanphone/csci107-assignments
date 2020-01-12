#base case do nothing
#solve the problem using smaller versions of the problem
def hanoi(disks, start, finish, intermediate):
    if disks >0:
        #recursively move disks-1 disk from start to intermediate
        hanoi(disks-1, start, intermediate, finish)
        #move immediately disk "disks" from start to finish
        print("Move disk", disks, "from", start, "to", finish)
        #recursively move disks-1 disks from intermediate to finish
        hanoi(disks-1, intermediate, finish, start)
hanoi(8, "A", "C", "B")