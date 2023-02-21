import math
import statistics

numbers = [10, 10, 10, 5000, 20, 30, 40, 50, 60, 70, 80, 90, 1000, 1000]

# mean
print(sum(numbers) / len(numbers))
print(statistics.mean(numbers))

# median
print(statistics.median(numbers))
## remember PEMDAS
if len(numbers) % 2 == 0:
    print((numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2)
else:
    print(numbers[len(numbers) // 2])


print(statistics.mode(numbers))