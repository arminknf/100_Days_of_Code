# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#inti_postion = int(position)
#position_row = (inti_postion / 10)
#position_column = (inti_postion % 10)
#print(type(position))
'''
if position == "11":
    row1 = ['X','️⬜️','️⬜️']
elif position == "12":
    row2 = ['X','⬜️','️⬜️']
elif position == "13":
    row3 = ['X','⬜️','️⬜️']
elif position == "21":
    row1 = ['⬜️','️X','️⬜️']
elif position == "22":
    row2 = ['⬜️','️X','️⬜️']
elif position == "23":
    row3 = ['⬜️','️X','️⬜️']
elif position == "31":
    row1 = ['⬜️','️⬜️','️X']
elif position == "32":
    row2 = ['⬜️','️⬜️','️X']
elif position == "33":
    row3 = ['⬜️','️⬜️','️X']
'''
horizontal = int (position[0])#2
vertical = int (position[1])#3

select_row = map[vertical -1]
select_row[horizontal - 1] = "X"

#map[vertical -1][horizontal -1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

