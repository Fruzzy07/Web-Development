# A
# N = int(input())
#
# array = input().split()
#
# for i in range(0, N, 2):
#     print(array[i], end=" ")

# B

# N = int(input())
# array = input().split()
#
# for i in range(N):
#     array[i] = int(array[i])
#
# for num in array:
#     if num % 2 == 0:
#         print(num, end=" ")

# C
# N = int(input())
# array = input().split()
# count_positive = 0
#
# for num_str in array:
#     num = int(num_str)
#     if num > 0:
#         count_positive += 1
# print(count_positive)

# D

# N = int(input())
# numbers = input().split()
# count = 0
#
# for i in range(1, N):
#     current_num = int(numbers[i])
#     previous_num = int(numbers[i - 1])
#     if current_num > previous_num:
#         count += 1
# print(count)

# E

# N = int(input())
# array = input().split()
# has_same_sign_pair = False
#
# for i in range(N - 1):
#     current_num = int(array[i])
#     next_num = int(array[i + 1])
#     if current_num * next_num > 0:
#         has_same_sign_pair = True
#         break
#
# if has_same_sign_pair:
#     print("YES")
# else:
#     print("NO")

# F

# N = int(input())
# array = input().split()
# count = 0
#
# for i in range(1, N - 1):
#     current_num = int(array[i])
#     prev_num = int(array[i - 1])
#     next_num = int(array[i + 1])
#     if current_num > prev_num and current_num > next_num:
#         count += 1
# print(count)

# G

# N = int(input())
# array = input().split()
#
# for i in range(N // 2):
#     array[i], array[N - i - 1] = array[N - i - 1], array[i]
# print(" ".join(array))




