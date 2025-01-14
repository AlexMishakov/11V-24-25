def prost(x):
    count = 0
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            count += 2
    return count == 0

for n in range(1, 20):
    s = ">" + "0" * 39 + "1" * n + "2" * 39

    while ">1" in s or ">2" in s or ">0" in s:
        if ">1" in s:
            s = s.replace(">1", "22>", 1)
        if ">2" in s:
            s = s.replace(">2", "2>", 1)
        if ">0" in s:
            s = s.replace(">0", "1>", 1)

    if prost(s.count("1") + s.count("2") * 2):
        print(n)
