#list

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(len(weekdays))
for day in range(len(weekdays)):
    print(weekdays[day])

weekdays.extend(["Saturday","Sunday"])

print("\n")

for day in range(len(weekdays)):
    print(weekdays[day])
