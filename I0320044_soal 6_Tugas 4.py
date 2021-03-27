#soal no 6

a = 4        # 4  = 100
b = 11       # 11 = 1001
c = 0

c = a | b;      # 100 = 0110 0100
print("nilai : ", c, ", binary : ", format(c, "08b"))

c = a >> b;     # 0 = 0000 0000
print("nilai : ", c, ", binary : ", format(c, "08b"))

c = a ^ b;      # 96 = 0110 0000
print("nilai : ", c, ", binary : ", format(c, "08b"))

c = ~a;         # -5 = -101
print("nilai : ", c, ", binary : ", format(c, "08b"))

c = b & a;      # 4 = 100
print("nilai : ", c, ", binary : ", format(c, "08b"))