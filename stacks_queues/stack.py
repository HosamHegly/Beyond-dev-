class Stack:
    def __init__(self):
        self.queue1=[]
        self.queue2=[]
        self.size = 0

    def push(self,element):# insert element in first queue
        self.queue1.append(element)
        self.size +=1

    def pop(self):

        if not self.queue1:
            return None

        while len(self.queue1)>1:
            self.queue2.append(self.queue1.pop(0))

        last_element = self.queue1.pop(0) # last element
        self.size -=1
        while len(self.queue2)>0:
            self.queue1.append(self.queue2.pop((0)))
        return last_element






if __name__=="__main__":
    new_stk = Stack()
    new_stk.push(1)
    new_stk.push(23)
    new_stk.push(134)
    print(new_stk.pop())

    new_stk.push(2)
    print(new_stk.pop())

    new_stk.push(43)
    new_stk.push(5)




    for i in range(0,new_stk.size):
        print(new_stk.pop())





