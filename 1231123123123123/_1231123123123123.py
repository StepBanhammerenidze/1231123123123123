def sisseastumine(p):
    ab=[] #список а
    h=[] #список б
    for i in range(p):
        ab.append(str(input("Имя абитуриента: ")))
        h.append(int(input("Баллы данного абитуриента: ")))
    raw = ab.copy() #имена по алфавитному порядку
    raw.sort()
    b = [] #список баллов по порядку
    for j in range(p):
        b.append(h[ab.index(raw[j])]) 

    print(*ab, sep = ", ") #убирает лишние символы
    print()
    
    for f in range(p):
        print(raw[f], ": ", b[f])
    print()

    print("Минимальная оценка",h.count(min(h)))
    print()

    s=0
    for o in range(len(h)):
        s += h[o]
    print("Средняя оценка",round(s/len(h), 2))
    print()

    print("Высшая оценка",max(h))
    print()
sisseastumine(int(input("Кол-во абитуриентов: ")))

