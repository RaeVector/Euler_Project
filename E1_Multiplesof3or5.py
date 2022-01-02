# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

from time import process_time

n = 1000

# slow method
def threeorfiveslow(n):
    slow = []
    time1_start = process_time()
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            slow.append(i)
    time1_end = process_time()
    print(f"The sum of all multiples of 3 or 5 under 1000 is: {sum(slow)}")
    print(f"The above method took: {time1_end - time1_start} seconds")


def threeorfivescomprehension(n):
    comprehension = []
    time2_start = process_time()
    [comprehension.append(i) for i in range(n) if i % 3 == 0 or i % 5 == 0]
    time2_end = process_time()
    print(f"The sum of all multiples of 3 or 5 under 1000 is: {sum(comprehension)}")
    print(f"The above method took: {time2_end - time2_start} seconds")


if __name__ == "__main__":
    threeorfiveslow(n)
    threeorfivescomprehension(n)
