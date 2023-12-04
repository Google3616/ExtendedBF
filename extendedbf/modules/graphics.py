import random

def func(prgmPtr, stackPtr, prgm, stack):
  stack[stackPtr] = random.randint(0,stack[stackPtr])
  return prgmPtr, stackPtr, prgm, stack

chars = {"u":func}
