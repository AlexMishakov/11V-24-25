

a = "012345678"
c = 0
for a1 in "2468":
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    for a6 in "0145678":
                        s = a1 + a2 + a3 + a4 + a5 + a6
                        if s.count("1") >= 2:
                            print(s)
                            c += 1

print(c)