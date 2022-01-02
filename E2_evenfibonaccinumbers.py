# Each new term in the Fibonacci sequence is generated
# by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence
# whose values do not exceed four million, find the sum of the even-valued terms.

def fibonacci():
    f1, f2 = 1, 2
    count = 0
    max = 4000000
    while f2 < max:
        f1, f2 = f2, f1 + f2
        if f1 % 2 == 0:
            count+=f1
    print(count)







if __name__ == "__main__":
    fibonacci()
