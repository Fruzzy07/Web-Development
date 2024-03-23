#WARPMUP-1
#sleep_in
# def sleep_in(weekday, vacation):
#   if not weekday or vacation:
#     return True
#   else:
#     return False
#
# print(sleep_in(False, False))

#monkey_trouble
# def monkey_trouble(a_smile, b_smile):
#   if a_smile and b_smile:
#     return True
#   if not a_smile and not b_smile:
#     return True
#   return False
# print(monkey_trouble(True, False))

#sum_double
# def sum_double(a, b):
#     sum = a + b
#     if a == b:
#         sum = sum * 2
#     return sum
# print(sum_double(1, 1))

#diff21
# def diff21(n):
#   if n <= 21:
#     return 21 - n
#   else:
#     return (n - 21) * 2
# print(diff21(22))

#parrot_trouble
# def parrot_trouble(talking, hour):
#   return (talking and (hour < 7 or hour > 20))
# print(parrot_trouble(False, 6))
# print(parrot_trouble(True, 23))

#WARMUP 2
#string_times
# def string_times(str, n):
#   result = ""
#   for i in range(n):
#     result = result + str
#   return result
# print(string_times("Yer", 2))

#front_times
# def front_times(str, n):
#     front_len = 3
#     if front_len > len(str):
#         front_len = len(str)
#     front = str[:front_len]
#
#     result = ""
#     for i in range(n):
#         result = result + front
#     return result
# print(front_times("Yernur", 5))

#string_bits
# def string_bits(str):
#   result = ""
#   for i in range(len(str)):
#     if i % 2 == 0:
#       result = result + str[i]
#   return result
# print(string_bits("Alibaba"))

#array_count9
# def array_count9(nums):
#   count = 0
#   for num in nums:
#     if num == 9:
#       count = count + 1
#   return count
# print(array_count9([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#array_front9
# def array_front9(nums):
#     end = len(nums)
#     if end > 4:
#         end = 4
#     for i in range(end):
#         if nums[i] == 9:
#             return True
#     return False
# print(array_front9([1, 2, 9, 3, 4]))

#STRING 1
#hello_name
# def hello_name(name):
#     return "Hello " + name + "!"
# print(hello_name("Yernur"))

#make_abba
# def make_abba(a, b):
#     return a + b + b + a
# print(make_abba("Hi", "Bye"))

#make_tags
# def make_tags(tag, word):
#     return "<" + tag + ">" + word + "</" + tag + ">"
# print(make_tags('i', 'Yay'))

#make_out_word
# def make_out_word(out, word):
#     return out[:2] + word + out[2:]
# print(make_out_word('<<>>', 'Yay'))

#extra_end
# def extra_end(str):
#     return str[-2:] * 3
# print(extra_end('Hi'))

#LIST1
#first_last6
# def first_last6(nums):
#     n = len(nums)
#     if(nums[0] == 6 or nums[n-1]==6):
#         return True
#     else:
#         return False
# print(first_last6([1, 2, 6]))
# print(first_last6([6, 1, 2, 3]))
# print(first_last6([13, 6, 1, 2, 3]))

#same_first_last
# def same_first_last(nums):
#     n = len(nums)
#     if(n>=1 and (nums[0] == nums[n-1])):
#         return True
#     else:
#         return False
# print(same_first_last([1, 2, 3]))
# print(same_first_last([1, 2, 3, 1]))

#make_pi
# def make_pi():
#     array = [3, 1, 4]
#     return array
# print(make_pi())

#common_end
# def common_end(a, b):
#     n = len(a)
#     m = len(b)
#     if((n>=1 and m>=1) and (a[0]==b[0] or a[n-1]==b[m-1])):
#         return True
#     else:
#         return False
# print(common_end([1, 2, 3], [7, 3]))
# print(common_end([1, 2, 3], [7, 3, 2]))

#sum3
# def sum3(nums):
#     return sum(nums)
# print(sum3([1,2,3,4]))

#LOGIC1
#cigar_party
# def cigar_party(cigars, is_weekend):
#     if is_weekend:
#         return cigars >= 40
#     else:
#         return 40 <= cigars <= 60
#
# # Example usage:
# print(cigar_party(30, False))  # False
# print(cigar_party(50, False))  # True
# print(cigar_party(70, True))   # True

#date_fashion
# def date_fashion(you, date):
#     if (you > date and you < 8 or you <= 2 or date <= 2):
#         return 0
#     elif (you <= date and date >= 8 or you >= 9):
#         return 2
#     else:
#         return 1
# print(date_fashion(5, 10))
# print(date_fashion(5, 2))
# print(date_fashion(5, 5))

#squirrel_play
# def squirrel_play(temp, is_summer):
#     if is_summer == True and (temp>=60 and temp<=100):
#         return True
#     elif is_summer == False and (temp>=60 and temp<=90):
#         return True
#     else:
#         return False
# print(squirrel_play(70, False))
# print(squirrel_play(95, False))
# print(squirrel_play(95, True))

#caught_speeding
# def caught_speeding(speed, is_birthday):
#     if is_birthday:
#         speed -= 5
#     if speed <= 60:
#         return 0
#     elif 61 <= speed <= 80:
#         return 1
#     else:
#         return 2
#
# print(caught_speeding(60, False))  # 0
# print(caught_speeding(65, False))  # 1
# print(caught_speeding(65, True))   # 0

#sorta_sum
# def sorta_sum(a, b):
#     total = a + b
#     if total < 10 or total > 19:
#         return total
#     else:
#         return 20
# print(sorta_sum(3, 4))
# print(sorta_sum(7, 5))

#LOGIC2
#make_bricks
# def make_bricks(small, big, goal):
#     remaining_inches = goal - min(goal // 5, big) * 5
#     return remaining_inches <= small
#
# # Example usage:
# print(make_bricks(3, 1, 8))   # True
# print(make_bricks(3, 1, 9))   # False
# print(make_bricks(3, 2, 10))  # True

#lone_sum
# def lone_sum(a, b, c):
#     if a != b and b != c and a != c:
#         return a + b + c
#     elif a == b and b == c:
#         return 0
#     elif a == b:
#         return c
#     elif b == c:
#         return a
#     else:
#         return b
#
# print(lone_sum(1, 2, 3))   # 6
# print(lone_sum(3, 2, 3))   # 2
# print(lone_sum(3, 3, 3))   # 0

#lucky_sum
# def lucky_sum(a, b, c):
#     if a == 13:
#         return 0
#     elif b == 13:
#         return a
#     elif c == 13:
#         return a + b
#     else:
#         return a + b + c
#
# # Example usage:
# print(lucky_sum(1, 2, 3))   # 6
# print(lucky_sum(1, 2, 13))  # 3
# print(lucky_sum(1, 13, 3))  # 1

#no_teen_sum
# def fix_teen(n):
#     if 13 <= n <= 14 or 17 <= n <= 19:
#         return 0
#     return n
#
# def no_teen_sum(a, b, c):
#     a = fix_teen(a)
#     b = fix_teen(b)
#     c = fix_teen(c)
#     return a + b + c
#
# print(no_teen_sum(1, 2, 3))   # 6
# print(no_teen_sum(2, 13, 1))  # 3
# print(no_teen_sum(2, 1, 14))  # 3

#round_sum
# def round10(num):
#     if num % 10 >= 5:
#         return num + (10 - num % 10)
#     else:
#         return num - num % 10
#
# def round_sum(a, b, c):
#     a = round10(a)
#     b = round10(b)
#     c = round10(c)
#     return a + b + c
#
# print(round_sum(16, 17, 18))  # 60
# print(round_sum(12, 13, 14))  # 30
# print(round_sum(6, 4, 4)) #10

#STRING2
#double_char
# def double_char(str):
#     result = ''
#     for char in str:
#         result += char * 2
#     return result
#
# print(double_char('The'))        # 'TThhee'
# print(double_char('AAbb'))       # 'AAAAbbbb'
# print(double_char('Hi-There'))   # 'HHii--TThheerre

#counti_hi
# def count_hi(str):
#     return str.count('hi')
#
# print(count_hi('abc hi ho'))   # 1
# print(count_hi('ABChi hi'))    # 2
# print(count_hi('hihi'))        # 2

#cat_dog
# def cat_dog(str):
#     return str.count('cat') == str.count('dog')
#
# print(cat_dog('catdog'))      # True
# print(cat_dog('catcat'))      # False
# print(cat_dog('1cat1cadodog')) # True

#count_code
# def count_code(str):
#     count = 0
#     for i in range(len(str) - 3):
#         if str[i:i+2] == 'co' and str[i+3] == 'e':
#             count += 1
#     return count
#
# print(count_code('aaacodebbb'))   # 1
# print(count_code('codexxcode'))   # 2
# print(count_code('cozexxcope'))   # 2

#end_other
# def end_other(a, b):
#     a_lower = a.lower()
#     b_lower = b.lower()
#     return a_lower.endswith(b_lower) or b_lower.endswith(a_lower)
#
# print(end_other('Hiabc', 'abc'))    # True
# print(end_other('AbC', 'HiaBc'))    # True
# print(end_other('abc', 'abXabc'))   # True

#LIST2
#count_evens
# def count_evens(nums):
#     count = 0
#     for num in nums:
#         if num % 2 == 0:
#             count += 1
#     return count
#
# print(count_evens([2, 1, 2, 3, 4]))  # 3
# print(count_evens([2, 2, 0]))        # 3

#big_diff
# def big_diff(nums):
#     min_val = min(nums)
#     max_val = max(nums)
#     return max_val - min_val
#
# print(big_diff([10, 3, 5, 6]))  # 7
# print(big_diff([7, 2, 10, 9]))  # 8

#centered_average
# def centered_average(nums):
#     nums.sort()
#     sum_without_extremes = sum(nums[1:-1])
#     centered_avg = sum_without_extremes // (len(nums) - 2)
#     return centered_avg
#
# print(centered_average([1, 2, 3, 4, 100]))        # 3
# print(centered_average([1, 1, 5, 5, 10, 8, 7]))   # 5
# print(centered_average([-10, -4, -2, -4, -2, 0])) # -3

#sum13
# def sum13(nums):
#     total = 0
#     i = 0
#     while i < len(nums):
#         if nums[i] == 13:
#             i += 2
#         else:
#             total += nums[i]
#             i += 1
#     return total
#
# print(sum13([1, 2, 2, 1]))        # 6
# print(sum13([1, 1]))               # 2
# print(sum13([1, 2, 2, 1, 13]))     # 6

#sum67
# def sum67(nums):
#     total = 0
#     skip_section = False
#
#     for num in nums:
#         if num == 6:
#             skip_section = True
#         elif num == 7 and skip_section:
#             skip_section = False
#         elif not skip_section:
#             total += num
#     return total
#
# print(sum67([1, 2, 2]))  # 5
# print(sum67([1, 2, 2, 6, 99, 99, 7]))  # 5
# print(sum67([1, 1, 6, 7, 2]))  # 4






