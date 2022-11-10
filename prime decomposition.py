num = (input("Introduce your number: "))

def prime_factors(n):
  list_of_factors=[]
  i=2
  while n>1:
    if n%i==0:
      list_of_factors.append(i)
      n=n/i
      i=i-1
    i+=1  
  return list_of_factors

print (prime_factors(int(num)))
