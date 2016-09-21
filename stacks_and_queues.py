# stacks and ques... YAY!

from linkedlist import LinkedList

class Stack:
    
    def __init__(self, init_items = []):
        self.items = LinkedList()
        
    def push(self, data):
        self.items.append(data)
        
    def pop(self):
        pop_data = self.items.data_at_place(0)
        self.items.remove_at_place(0)
        return pop_data
        
    def peek(self):
        return self.items.data_at_place(0)
        
    def __len__(self):
        return len(self.items)
        


mystack = Stack()

print ("Stack length is " + str(len(mystack)))
mystack.push("Hello")
mystack.push("World")

print ("Stack length is now " + str(len(mystack)))
print (mystack.pop())



class Queue:
    
    
    