def Is_Armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** len(str(num))
        temp //= 10
    return num == sum

Armstrong_Numbers = []
for i in range(100001):
    if Is_Armstrong(i):
        Armstrong_Numbers.append(str(i))

print(", ".join(Armstrong_Numbers))