def fibonacci(x): 
    fib_list = [0, 1] 
  
    any(map(lambda _: fib_list.append(sum(fib_list[-2:])), range(2, x))) 
  
    return fib_list[:x] 
  
print(fibonacci(eval(input())))

from functools import reduce
#The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.
fib =  lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1])
n = eval(input("Enter the number of terms: "))
print(fib(n))

def fibbonaci_long(n):
    result = [0, 1]
    for i in range(n-2):
        result.append(result[-1] + result[-2])
    return result

