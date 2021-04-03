import datetime

user_input = input("Enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

"""splitted list elements  are always strings. we need to convert it to date element"""
#print(datetime.datetime.strptime(deadline, "%d.%m.%Y"))
#print(type(datetime.datetime.strptime(deadline, "%d.%m.%Y")))

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_till = deadline_date - today_date

#Need f to use variables in printed text. conversion from float to int is below
print(f"Dear Omer, Time remaining to {goal} is {int(time_till.total_seconds()/60/60)} hours")