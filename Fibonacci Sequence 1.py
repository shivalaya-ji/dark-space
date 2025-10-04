# Python program to display the Fibonacci sequence.
# In this program, we store the number of terms to be displayed in nterms.
# A recursive function recur_fibo() is used to calculate the nth term of the sequence.
# We use a for loop to iterate and calculate each term recursively.

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))