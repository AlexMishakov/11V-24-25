a = "ЕГЭ"
c = 0
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    s = a1 + a2 + a3 + a4 + a5
                    if a1 in ("Э", "Е"):
                        print(s)
                        c += 1
print(c)













