"""
def check_winner():
    if area[0][0] == "x" and area[0][2] == "x":
        return "x"
    if area[1][1] == "x" and area[1][2] == "x":
        return "x"
    if area[2][1] == "x" and area[2][2] == "x":
        return "x"
    if area[1][0] == "x" and area[2][0] == "x":
        return "x"
    if area[1][1] == "x" and area[2][1] == "x":
        return "x"
    if area[1][2] == "x" and area[2][2] == "x":
        return "x"
    if area[1][1] == "x" and area[2][2] == "x":
        return "x"
    if area[1][1] == "x" and area[2][0] == "x":
        return "x"
    if area[0][0] == "0" and area[0][2] == "0":
        return "x"
    if area[1][1] == "0" and area[1][2] == "0":
        return "x"
    if area[2][1] == "0" and area[2][2] == "0":
        return "x"
    if area[1][0] == "0" and area[2][0] == "0":
        return "x"
    if area[1][1] == "0" and area[2][1] == "0":
        return "x"
    if area[1][2] == "0" and area[2][2] == "0":
        return "x"
    if area[1][1] == "0" and area[2][2] == "0":
        return "x"
    if area[1][1] == "0" and area[2][0] == "0":
        return "x"
    return "*"
"""
def draw_area():
    for i in area:
        print(*i)

area = [['*', '*', '*'],['*', '*', '*'],['*', '*', '*']]
print('Добро пожаловать в крестики-нолики!')
print(---------------------------------------)
draw_area()
area([0][0]) = 'x'
draw_area()
