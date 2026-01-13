student = (2, "Enrico", "coding")
print(student)
print(student[1])
print(len(student))
print(student[0:2])

pair1 = ("Ryan", "Enrico")
pair2 = ("Bienve", "Robin")
group = pair1 + pair2
print(group)

random = {11, 25, 32, 49}
print(random)
random.add(53)
random.remove(32)
print(random)

Set1 = {"green", "blue"}
Set2 = {"blue", "yellow"}
print(Set1 & Set2)
print(Set1 | Set2)

details = ("Enrico", "Efendi", 14, "54kg", "Mathematics")
list = list(details)
print(list)