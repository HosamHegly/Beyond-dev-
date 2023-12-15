class Queue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        self.size = 0

    def enqueue(self,element):# insert element in first stack
        self.stack1.append(element)
        self.size +=1

    def dequeue(self):

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            self.size -=1

            return self.stack2.pop()
        else:
            return None



if __name__=="__main__":
    new_queue = Queue()
    new_queue.enqueue(1)
    new_queue.enqueue(2)
    new_queue.enqueue(13)
    new_queue.enqueue(23)
    new_queue.enqueue(1)


    for i in range(0,new_queue.size):
        print(new_queue.dequeue())





