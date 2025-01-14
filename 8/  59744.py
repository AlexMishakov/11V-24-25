

a = "МУЖЧИНА"
c = 1
count = 0
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    for a6 in a:
                        s = a1 + a2 + a3 + a4 + a5 + a6
                        if a1 != "Ч":
                            if ((s.count("М") == 1 or s.count("М") == 0) and
                                (s.count("У") == 1 or s.count("У") == 0) and
                                (s.count("Ж") == 1) and
                                (s.count("Ч") == 1 or s.count("Ч") == 0) and
                                (s.count("И") == 1 or s.count("И") == 0) and
                                (s.count("Н") == 1 or s.count("Н") == 0) and
                                (s.count("А") == 1 or s.count("А") == 0)):
                                if c % 2 != 0:
                                    print(c, s)
                                    count += 1
                                c += 1
print(count)
