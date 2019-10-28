print("WELCOME")
start_hour = int(input("Enter start time(hours): "))
start_min = int(input("Enter start time(mins): "))
end_hour = int(input("Enter ending time(hours): "))
end_min = int(input("Enter ending time(mins): "))
slot_time = int(input("Enter an average time given to a interviewer(in mins): "))

No_of_Slots = int((((end_hour*60)+end_min) - ((start_hour*60)+start_min))/slot_time)

print(No_of_Slots)

slots = []

start = [start_hour,start_min]
slots.append(start)

for x in range(No_of_Slots):
    if((start[1]+slot_time)>=60):
        start[0]=start[0]+1
        start[1]=(start[1]+slot_time)-60
    else:
        start[1]=start[1]+slot_time
    print(start)
