print("-" * 39)
print(f"| {'decimal':^10}|{'octal':^9}|{'Hexadecimal':^15}|")
print("-" * 39)
for i in range(16):
    print(f"|  {i:^9}|{i:^9o}|{i:^15X}|")
print("-" * 39)