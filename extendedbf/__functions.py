import importlib
import os

class sepLvls:
  def __init__(self,string):
    count = 0
    self.mask = []
    for i in string:
      if i == "[":
        count += 1
        self.mask.append(count)
      elif i == "]":
        self.mask.append(count)
        count -= 1
      else:
        self.mask.append(count)

  def locateEnd(self,count,pos,flip=False):
    mask = self.mask[::-1 if flip else 1]
    mask.append(-1)
    if flip:
      pos = len(self.mask) - pos
    for index,num in enumerate(mask[pos:]):
      index =  index + pos
      if num < count:
        if flip:
          return len(self.mask) - index 
        else:
          return index - 1
    return 0

class Interpreter:
  """Interpreter class for ExtendedBF. \n
  Parameters: \n
  --Modules(list): a list of module names to import.\n"""
  def __init__(self, modules = []):
    self.modules = modules
    self.libs = []
    for i in self.modules:
      if i + ".py" not in os.listdir(os.getcwd() + "/ExtendedBF/extendedbf/modules"):
        module = importlib.import_module(i)
        self.libs.append(module)
      else:
        module = importlib.import_module(("ExtendedBF/extendedbf/modules/").replace("/",".") + i)
        self.libs.append(module)
    
        

  def parse(self,prgm: str = "",filepath:str = "path/to/your/ebf/file.ebf") -> None:
    """A function to parse your EBF code. \n
    Parameters: \n
    --prgm(str): the code to parse. If reading from a file, leave blank. \n
    --filepath(str): the path to the file to read. Leave blank if reading from the prgm variable."""
    
    if filepath != "path/to/your/ebf/file.ebf":
      prgmFile = open(filepath,"r")
      prgm = prgmFile.read().replace("\n","")
      prgmFile.close()

    stack = [0] * 1000
    stackPtr = 0
    prgmPtr = 0
    count = 0
    
    levelMask = sepLvls(prgm)
  
    while prgmPtr < len(prgm):
    
      if prgm[prgmPtr] == ">":
        if stackPtr < len(stack):
          stackPtr += 1
        else:
          pass

      if prgm[prgmPtr] == "<":
        if stackPtr > 0:
          stackPtr -= 1
        else:
          pass

      if prgm[prgmPtr] == "+":
        if stack[stackPtr] < 255:
           stack[stackPtr] += 1
        else:
           stack[stackPtr] = 0

      if prgm[prgmPtr] == "-":
        if stack[stackPtr] > 0:
          stack[stackPtr] -= 1
        else:
          stack[stackPtr] = 255

      if prgm[prgmPtr] == "[":
        count += 1
        if int(stack[stackPtr]) == 0:
          prgmPtr = levelMask.locateEnd(count,prgmPtr) 

      if prgm[prgmPtr] == "]":
        prgmPtr = levelMask.locateEnd(count,prgmPtr,True) - 1
        count -= 1

      if prgm[prgmPtr] == ".":
        try:
          if prgm[prgmPtr + 1] == "C":
           print(chr(int(stack[stackPtr])),end="")
          else:
            print(str(stack[stackPtr]),end="")
        except IndexError:
          print(str(stack[stackPtr]),end="")
        
      if prgm[prgmPtr] == ",":
        inp = input("type smthn")
        try:
          if prgm[prgmPtr + 1] == "C":
            stack[stackPtr] = ord(inp)
          else:
            stack[stackPtr] = int(inp)
        except IndexError:
          stack[stackPtr] = int(inp)

      if prgm[prgmPtr] == "C":
        pass

      if prgm[prgmPtr] == "*":
        __push(stack,self.__draw)

      for library in self.libs:
        for char in library.chars:
          if prgm[prgmPtr] == char:
            prgmPtr, stackPtr, prgm, stack = library.chars[char](prgmPtr,stackPtr,prgm,stack)
        
      prgmPtr += 1


def __push(stack,draw):
  
  pixelPtr = 5 + stack[0]
  for i in range(stack[1] * stack[2]):
    t.color(__numberToRGB(stack[pixelPtr + i]))
    # Draw pixel
  print(t.color())
  return(0)

def __numberToRGB(number):
  number = bin(number) # Decimal to binary
  number = str(number) # Int to string
  number = number[2:] # Remove the binary tag
  while len(number) < 8: # Append 0s to the front of the
    number = "0" + number # string until it's 8 digits long
  return(__hexify(number[:3]) + __hexify(number[3:6]) + __hexify(number[6:]))
        # ^ Convert the binary values to hex values

def __hexify(number):
  if len(number) == 3:
    match number:
      case "000":
        return("00")
      case "001":
        return("18")
      case "010":
        return("40")
      case "011":
        return("68")
      case "100":
        return("90")
      case "101":
        return("B9")
      case "110":
        return("E0")
      case "111":
        return("FF")
      case _:
        return("fuck you")
  elif len(number) == 2:
    match number:
      case "00":
        return("00")
      case "01":
        return("B8")
      case "10":
        return("3A")
      case "11":
        return("FF")
      case _:
        return("fuck you")
  else:
    return("fuck you")