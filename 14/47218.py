a = "0123456789abcde"
for x in a:
    s = int(f"123{x}5", 15) + int(f"1{x}233", 15)
    if s % 14 == 0:
        print(s // 14)
        break