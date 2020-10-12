def fibonacci(x): 
    fib_list = [0, 1] 
  
    any(map(lambda _: fib_list.append(sum(fib_list[-2:])), range(2, x))) 
  
    return fib_list[:x] 
  
print(fibonacci(eval(input())))