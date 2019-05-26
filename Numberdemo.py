# Find the sum of all the multiples of 3 or 5 below 1000.

nums = [3, 5]
max = 999
result = 0
for i in range(0, max):
    if i % 3 == 0 or i % 5 == 0:
        result += i
print(result)