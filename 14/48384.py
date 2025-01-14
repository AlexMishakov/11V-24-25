a9 = "012345678"
for x in a9:
    for y in a9:
        s = int(f"88{x}4{y}", 9) + int(f"7{x}44{y}", 11)
        if s % 61 == 0:
            print(x, y, s, s // 61)