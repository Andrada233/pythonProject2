##functie care primeste ca param un nr natrAL 0-255 si intoarce
# val obt prin scaderea val de 255 a nr natural n
#problema Fibonacci
def fib():
 l=[1,1,2,3,5,8,13,21,34,55]
n=[]
f =[0]*n
if n<=2:
  return[-1]
for i in range(2,n):
    f[n]=f[n-1]+f[n-2]
return f


