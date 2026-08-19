# def find_vip_number(no):
#     div = 2
#     while div <= no//2:
#         if no % div == 0:
#             return 'not VIP'
#         div+=1
#     else:
#         return 'VIP'
# no = 2
# count = 0
# while count < 5:
#     result = find_vip_number(no) #Function Calling Statement 
#     if result == 'VIP':
#         print(no)
#         count+=1
#     no = no+1


# def find_vip_number(no):
#     div = 2
#     while div <= no//2:
#         if no % div == 0:
#             return 'not VIP'
#         div+=1
#     else:
#         return 'VIP'
# no = 2
# while no < 20:
#     result = find_vip_number(no) #Function Calling Statement 
#     if result == 'VIP':
#         print(no)
#     no = no+1


# chocolate   = 20
# wrapper     = 20

# while wrapper >= 3:
#     wrapper = wrapper - 3
#     chocolate = chocolate + 1
#     wrapper = wrapper + 1
# else:
#     print("chocolate:", chocolate)


remains=8
count=0
while count<3:
    eaten=remains//2
    remains=remains+eaten
    count+=1
print("starting:", remains)