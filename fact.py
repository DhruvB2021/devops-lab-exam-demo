import math

def fact(x):
  if x<0:
    raise ValueError("Negative Value Given")
  return math.factorial(x)

