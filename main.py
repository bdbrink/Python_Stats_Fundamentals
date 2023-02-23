import math
import statistics

def simple_stats(numbers):
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

    print(statistics.median_high(numbers))
    print(statistics.median_low(numbers))

    # mode
    print(statistics.mode(numbers))
    print(max(set(numbers), key=numbers.count))

    # deviation both should return same values
    print(statistics.stdev(numbers))
    print(math.sqrt(statistics.variance(numbers)))

def main():
    numbers = [10, 10, 10, 5000, 20, 30, 40, 50, 60, 70, 80, 90, 1000, 1000]
    simple_stats(numbers)

if __name__ == "__main__":
    main()