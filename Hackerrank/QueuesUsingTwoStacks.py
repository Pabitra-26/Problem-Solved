# Problem name: Queues using two stacks
# Description: A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue
# (i.e., the one that has been waiting the longest) is always the first one to be removed.
# Strategy: we can use a single list instead
class Queue(object):
    def __init__(self):
        self.S1=[]
    def enQueue(self,element):
        self.S1.append(element)
    def deQueue(self):
        self.S1.pop(0)
    def print_q(self):
        print(self.S1[0])

if __name__=="__main__":
    n=int(input())
    que=Queue()
    for i in range(n):
        l=list(map(int,input().split()))
        if(l[0]==1):
            que.enQueue(l[1])
        elif(l[0]==2):
            que.deQueue()
        else:
            que.print_q()
