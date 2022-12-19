number = int(input("Check this number:"))
def prime_checker(n):
  c = 0
  for i in range(2,n):
    if number%i == 0:
      c=1
  if c==1:
    print(f"{number} is not a prime number")
  else:
    print(f"{number} is a prime number")
prime_checker(number)
