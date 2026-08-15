# student = 1
# while student <=5:
#     student = student + 1
#     print(1, end = ' ') 


# student = 0
# while student <5:
#     student = student + 1
#     print(student, end = ' ')


# count=1
# position=0
# while(count<6):
#     position=position+2
#     count=count+1
#     print('Position:',position)


# count=1
# floor=3
# while(count<6):
#     floor=floor+3
#     count=count+1
#     print('Floor:',floor )


# count=10
# while count >= 2:
#     print(count)
#     count = count - 2


# station = 1
# last_station = station
# first_station = True
# while station <= 100:
#     if station % 3 == 0 and station % 5 == 0:
#         if first_station == True:
#             print('First Station is: ', station)
#             first_station = False
#         else:
#             print(station) 
#         last_station = station   
#     station+=1
# print("Last Common Station is", last_station)


# common = []
# station= 1

# while station <= 100:
#     if station % 3 == 0 and station % 5 == 0:
#     #   common += [station]
#         common =common + [station]
#     station += 1

# print("First common station:", common[0])
# print("Last common station:", common[-1])
# print("All common stations:", common)



# common = []
# station= 1

# while station <= 45:
#     if station % 3 == 0 and station % 5 == 0:
#     #   common += [station]
#         common =common + [station]
#     station += 1

# print("First common station:", common[0])
# print("Last common station:", common[-1])
# print("All common stations:", common)


no = 21
div = 2
while div < no: 
    if no % div == 0:   # 9 % 2 != 0
        print('Not A Prime Number')
        break
    div+=1
else:
    print('Prime Number')