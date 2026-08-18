print(10 > 5)
print(10 > 15)
p1 = 10
p2 = 20
print(p1 > p2)
print(p1 < p2)

p3 = 30
p4 = 30
print(p3 >= p4)
print(p3 <= p4)
result = p3 >= p4
print(result)
print(type(result))

s5 = "qwer"
p6 = 4 + 4
print(s5 == p6)
print(8 == 4 + 4)
print(s5 != p6)

p7 = 90
print(p7 % 2 == 0)
print(p7 % 2 == 6)

p8 = 2.58
print(p8 >= 2 and p8 <= 3)
print(2 <= p8 <= 3)

name = "Sandra"
print("S" in name or "m" in name)

p9 = 7
print(not(p9 % 3 == 0 or p9 % 5 == 0))

print(bool(1))
print(bool("Sandra"))
print(bool(-78))
print(bool(0))
print(bool(name))
print(bool(""))
print(bool(" "))

# 0 и "" - в языке являютмя ничем, соответственно, не определяются за true,
# в отличии от пробела " ", который является чем-то.
# not - инвертирует результат
# При использовании or должно соответствовать одно из условий.
# Булевые значения