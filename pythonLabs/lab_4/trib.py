#Tribonacci list
#
# def tribonacci_list(n):
#     if n <= 0:
#         return [0]
#     else:
#         tr_nums = [0, 1, 1]
#         for _ in range(0,n):
#             num = tr_nums[-1] + tr_nums[-2] + tr_nums[-3]
#             tr_nums.append(num)
#         return tr_nums
#
# n = int (input("Enter quantity of numbers: "))
# print(f"List of Tribonacci numbers (quantity: {n}): {tribonacci_list(n)}")
#

# Generator Tribonacci
def trib_generator(n):
   num1, num2, num3 = 0, 1, 1
   for i in range(n):
       yield num1
       num1, num2, num3 = num2, num3, num1 + num2 + num3

quantity = 7
list = trib_generator(quantity)
print(*(list))
