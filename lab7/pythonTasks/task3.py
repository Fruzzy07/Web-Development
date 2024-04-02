# A
# a = int(input())
# b = int(input())
# for i in range(a, b+1):
#     if(i % 2 == 0):
#         print(i, end=' ')

# B
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# for i in range(a, b+1):
#     if(i % d == c):
#         print(i, end=" ")

# C
# a = int(input())
# b = int(input())
#
# for num in range(a, b + 1):
#     if num**0.5 == int(num**0.5):
#         print(num, end=" ")

# D
# x = int(input())
# d = int(input())
#
# x_str = str(x)
# count = 0
#
# for digit in x_str:
#     if int(digit) == d:
#         count += 1
# print(count)

# E
# x = int(input())
#
# x_str = str(x)
# sum = 0
#
# for digit in x_str:
#         sum += int(digit)
# print(sum)

# F
# x = int(input())
# x_str = str(x)
# s_reversed = ''.join(reversed(x_str))
#
# s_reversed = s_reversed.lstrip('0')
#
# print(s_reversed)

# G
# import math
# x = int(input())
#
# for i in range(2, math.isqrt(x) + 1):
#     if x % i == 0:
#         print(i)
#         break
# else:
#     print(x)

# H
# x = int(input())
# for i in range (1, x+1):
#     if(x % i == 0):
#         print(i, end=" ")

# I
# import math
#
# x = int(input())
# count = 0
#
# for i in range(1, math.isqrt(x) + 1):
#     if x % i == 0:
#         count += 1
#         if i != x // i:
#             count += 1
# print(count)

# J
# sum = 0
#
# for _ in range(100):
#     num = int(input())
#     sum += num
#
# print(sum)

# K
# n = int(input())
# sum = 0
# for i in range(n):
#     x = int(input())
#     sum += x
# print(sum)

# L
# n = input()
# number = 0
#
# for i in range(len(n)):
#     number += int(n[-i - 1]) * (2 ** i)
# print(number)

# M
# n = int(input())
# cnt = 0
# for i in range(n):
#     a = int(input())
#     if(a==0):
#         cnt += 1
# print(cnt)

