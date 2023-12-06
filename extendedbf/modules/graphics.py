size = (0,0)
screen = []
posPtr = (0,0)
def initDrw(prgmPtr, stackPtr, prgm, stack):
  global size
  global screen
  global posPtr
  size = (stack[0],stack[1])
  posPtr = (stackPtr,stackPtr + 1)
  screen = [[[0] for i in range(size[0])] for j in range(size[1])]
  
  return prgmPtr, stackPtr, prgm, stack

def setPxl(prgmPtr, stackPtr, prgm, stack):
  screen[stack[posPtr[0]]][stack[posPtr[1]]] = [stack[stackPtr]]
  return prgmPtr, stackPtr, prgm, stack

def getPxl(prgmPtr, stackPtr, prgm, stack):
  stack[stackPtr] = screen[stack[posPtr[0]]][stack[posPtr[1]]]
  return prgmPtr, stackPtr, prgm, stack
def draw(prgmPtr, stackPtr, prgm, stack):
  for i in screen:
    for j in i:
      print(j,end="")
    print("")
  return prgmPtr, stackPtr, prgm, stack
  
chars = {"i":initDrw, "=":setPxl,"^":getPxl,"*":draw,}
