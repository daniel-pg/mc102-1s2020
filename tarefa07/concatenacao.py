A = input().split()
B = input().split()

for i in range(len(A) - 1):
    print(A[i] + B[i], end=" ")

print(A[-1] + B[-1], end="")
