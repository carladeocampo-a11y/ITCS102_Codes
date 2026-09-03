money = 1554


one_t = money // 1000
one_t_sukli = money % 1000

five_h = one_t_sukli // 500
five_h_sukli = one_t_sukli % 500

two_h = five_h_sukli // 200
two_h_sukli = five_h_sukli % 200

one_h = two_h_sukli // 100
one_h_sukli = two_h_sukli % 100

fifty = one_h_sukli // 50
fifty_sukli = one_h_sukli % 50

ten = fifty_sukli // 10
ten_sukli = fifty_sukli % 10

lima = ten_sukli // 5
lima_sukli = ten_sukli % 5

piso = lima_sukli // 1
piso_sukli = lima_sukli % 1

print("1000 =", one_t)
print("500 =", five_h)
print("200 =", two_h)
print("100 =", one_h)
print("50 =", fifty)
print("10 =", ten)
print("1 =", piso)