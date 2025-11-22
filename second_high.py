m = map(int,input('Enter the numbers seperated by spaces: ').split())
print (f"MAP : {m}")
numbers = list(m)
print (f"the second highest is : {sorted (set(numbers)) [-2]}")
 
print (f"the second lowest is : {sorted (set(numbers)) [1]}")