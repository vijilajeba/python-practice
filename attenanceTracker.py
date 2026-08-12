names=[]
days=[]
total_days=[]
attendancep=[]
low_attendance=[]
while True:
    name=input("Enter The Name(q to quit): ")
    if name.lower()=="q":
        break
    else:
        day=int(input(f"Enter no of days {name} present: "))
        total_day=int(input("Enter The Total Days: "))
        names.append(name)
        days.append(day)
        total_days.append(total_day)
for name,day,total_day in zip(names,days,total_days):
    percentage=(day/total_day)*100
    attendancep.append(percentage)
print("--------ATTANDANCE TABLE--------")
print(f"{'NAME':<10}{'NO.OF DAYS PRESENT':<20}{'TOTAL DAYS':<15}{'ATTANDANCE_PERCENTAGE':<10}%")
for name,day,total_day,percentage in zip(names,days,total_days,attendancep):
    print(f"{name:<10}{day:<20}{total_day:<15}{percentage:.2f}")
    if percentage<75:
            low_attendance.append(name)
for name in low_attendance:
    print(name)
        
    
