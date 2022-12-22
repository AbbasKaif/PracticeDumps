def arraySum(numbers):
    s = 0;
    for i in numbers:
        s = s + i;
    return s;
num = [3, 13, 4, 11, 9];
print(arraySum(num));