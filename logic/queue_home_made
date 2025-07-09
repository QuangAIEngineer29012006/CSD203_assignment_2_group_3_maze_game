import heapq
class Queue:
    def __init__(self):
        self.data = []
        self.size = 0
        
    def isEmpty(self):
        return self.size ==0
    def enqueue(self,t):
        heapq.heappush(self.data, t)
        self.size +=1
        
    def dequeue(self):
        self.size -=1
        return heapq.heappop(self.data)

    def show(self):
        print(self.data)
        
     