Stack  =  [None, None, None, None, None, None, None, None, None, None]
TopPointer = -1

#ADD
def push(newdata):
      global TopPointer
      if (TopPointer+1> len(Stack)):
            print("Stack is full - cannot add")
      else:
            TopPointer = TopPointer +1
            Stack[TopPointer] = newdata
      
#REMOVE      
def pop():
      global TopPointer
      if TopPointer < 0:
            print("Cannot pop, stack is empty")
      else:
            print(f"removed {Stack[TopPointer]} from stack")
            TopPointer = TopPointer -1
