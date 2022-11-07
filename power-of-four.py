def isPowerOfFour(n):
  if (n <= 0):
      return False
  if (n % 4 == 0):
      return isPowerOfFour(n//4)
  if (n == 1):
      return True
  return False
