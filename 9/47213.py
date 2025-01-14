f = open("47213.csv")
count = 0
for line in f.readlines():
    a = [int(i) for i in line.split(",")]
    povtor = []
    new_povtor = []
    for i in a:
        if a.count(i) > 1:
            povtor.append(i)
        if a.count(i) == 1:
            new_povtor.append(i)
    if len(povtor) == 2:
        if sum(new_povtor) / 4 <= sum(povtor):
           count += 1
print(count)

