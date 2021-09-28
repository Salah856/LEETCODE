def gcd(a, b):
  
  if not b:
    return a
  
  return gcd(b, a % b)
