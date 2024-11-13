X,Y,Z = map(int, input().split())
Max_Mangoes_Weight = Z - Y
if Max_Mangoes_Weight <= 0 :
    Max_Mangoes = 0
else:
    Max_Mangoes = Max_Mangoes_Weight // X
print(Max_Mangoes)
