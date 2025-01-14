a = "ЯНВАРЬ"
a = sorted(a)
i = 0
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    i += 1
                    s = a1 + a2 + a3 + a4 + a5
                    if a1 != "Я" and s.count("Ь") <= 1 and s.count("ЯЯ") == 0:
                        print(i, s)

