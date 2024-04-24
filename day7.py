# Question No_1
gtst = "Day7"
# Question No_2
print(f"Hello Today is our {gtst} course")
# Question No_3
List = [0, 2, 4]
print(f"The first even number is {List[0]}")
print(f"The second even number is {List[1]}")
print(f"The third even number is {List[2]}")
# Question No_4
fruits = {'apple':10,'banana':15,'pineapple':20}
# Question No_5
choice = input("Choose Your fruit: ").lower()
if choice in fruits:
    print("The value of {} is: {} birr".format(choice,fruits[choice]))
else:
    print("Error! Your choose must be apple, banana or pineapple")