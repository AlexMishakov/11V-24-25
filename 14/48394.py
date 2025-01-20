a = "0123456789abc"
for x in a:
    s = int(f"4c{x}4", 15) + int(f"{x}62a", 13)
    if s % 121 == 0:
        print(s // 121)
        break