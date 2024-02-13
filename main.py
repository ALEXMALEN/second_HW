# # print("Hello player!")
# #
# # first_diagonal = int(input("Enter the first diagonal: "))
# # second_diagonal = int(input("Enter the second diagonal: "))
# # area = (first_diagonal * second_diagonal) / 2
# # print("Total: ", area)
# #
# # v1
# # n1 = 10
# # n2 = 20
# # v2
# n1, n2 = 10, 20 # множинне привласнення
# print(n1 > n2)
# print(n1 >= n2)
# print(n1 < n2)
# print(n1 <= n2)
# print(n1 == n2) # поверне true якщо обидва операнди однакові
# print(n1 != n2) # поверне true якщо обидва операнди різні
#
# # print(1 == 1 and 3 = 3) # поверне true якщо обидва операнди рівні true, інашке false
# # print(1 == 1 or 2 = 3) # поверне true якщо хоча б один операнд дорівнює true, інашке false
#
# is_valid = False
# print(is_valid)
# print(not is_valid) # not --> інверсіяб якщо значення False стане True, і навпаки
#
# print("hello" in "Hello world")
#
#
hours = int(input("Enter hours: "))

if hours >= 12 and hours <= 23:
    print("PM")
elif hours >= 0 and hours < 12:
    print("AM")
else:
    print("Incorrect hours!!!")
