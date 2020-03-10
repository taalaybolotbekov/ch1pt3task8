def number():
    num = [1,2,3,-4,5,-6,7,-8,9,10,0,0]
    positive = []
    negative = []
    a=[]
    for i in num:
        if i > 0 :
            positive.append(i)
        elif i < 0:
            negative.append(i)
        elif i == 0:
            a.append(i)
    return('Положительные числа %s , отрицательные числа %s,нули %s' % (positive,negative,a))
print(number())