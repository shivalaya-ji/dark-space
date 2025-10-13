# Python program to display the Fibonacci sequence.
# In this program, we store the number of terms to be displayed in nterms.
# A recursive function recur_fibo() calculates the nth term.


def recur_fibo(n: int) -> int:
    if n <= 1:
        return n
    return recur_fibo(n - 1) + recur_fibo(n - 2)


# if __name__ == "__main__":
#     nterms = int(input("How many terms? "))
#     if nterms <= 0:
#         print("Please enter a positive integer")
#     else:
#         print("Fibonacci sequence:")
#         for i in range(nterms):
#             print(recur_fibo(i))
