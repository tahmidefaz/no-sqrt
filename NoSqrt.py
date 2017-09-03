import math
import time
import random

def diff(n1,n2):
  return(abs(n2-n1))

# num=float(input("Enter the number: "))
num = random.uniform(1,1000000000000000)

print("The number is: "+str(num))

start=0
mid=num/2
end=num
computation=0

start_time = time.time()
while(mid*mid!=num):
  
  elapsed_time= time.time() - start_time
  if(elapsed_time >= 5.0):
    break
  
  if(diff(mid*mid,num)<=0.0000000000000001 and diff(mid*mid,num)>=0.00000000000000001):
    break
  
  if(mid*mid > num):
    end = mid
    mid=(start+end)/2
  else:
    start=mid
    mid=(start+end)/2
  computation+=1

end_time= time.time()

realroot = math.sqrt(num)
error=((mid-realroot)/realroot)*100
runtime = end_time - start_time

print("Calculated Square root: "+str(mid))
print("Actual square root: " + str(realroot))
print("Percentage Error: "+ str(error)+"%")

print("Number of computations: "+str(computation))
print("Runtime: "+str(runtime)+" sec")