#task1
# if __name__ == '__main__':
#     print("Hello, World!")

#task2
# if __name__ == '__main__':
#     n = int(input().strip())
#     if(n % 2 != 0):
#         print("Weird")
#     elif((n % 2 == 0) and (n>=2 and n<=5)):
#         print("Not Weird")
#     elif((n % 2 == 0) and (n>=6 and n<=20)):
#         print("Weird")
#     else:
#         print('Not Weird')

#task3
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(a+b)
#     print(a-b)
#     print(a*b)

#task4
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(a//b)
#     print(a/b)

#task5
# if __name__ == '__main__':
#     n = int(input())
#     for i in range(n):
#         print(i*i)

#task6
# def is_leap(year):
#     leap = False
#
#     if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
#         leap = True
#
#     return leap
# year = int(input())
# print(is_leap(year))

# task7
# if __name__ == '__main__':
#     n = int(input())
#     for i in range(1, n+1):
#         print(str(i),end='')

#task8
# N = int(input())
# array = [int(x) for x in input().split()]
#
# M = int(input())
# arr = [int(x) for x in input().split()]
#
# total_unique = len(set(array + arr))
#
# print(total_unique)

#task9
# n_english = int(input())
# english_subs = set(int(x) for x in input().split())
#
# n_french = int(input())
# french_subs = set(int(x) for x in input().split())
#
# total_subs = len(english_subs.intersection(french_subs))
#
# print(total_subs)

#task10
n_english = int(input())
english_subs = set(int(x) for x in input().split())

n_french = int(input())
french_subs = set(int(x) for x in input().split())

total_subs = len(english_subs.difference(french_subs))

print(total_subs)


