#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

x = int(input("Enter a number: "))

ans, res = 0, 0
for i in range(3):
    ans = x * (10**i) + ans
    res = res + ans

print(res)