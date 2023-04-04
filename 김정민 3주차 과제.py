#1
def grade(x):
    #return "FFFFFFDCBAA"[x//10]
    if 100 >= x >= 90:
        return 'A'
    elif x >=80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    else:
        return 'F'
print(grade(94))
print(grade(64))
print(grade(34))


#2
def quadrant():
    x = input()
    y = input()

    #return [[2, 1], [3, 4]] [y<0][x>0]  
    return [[1, 3], [4, 2]] [x*y<0][x<0]

#3
def distribution():
    x = int(input('입력: '))
    if x%4 != 0:
    #if str(bin(x&4))[-2:] != '00':
        return '윤년입니다'
    if x%100 == 0:
        return '윤년아님'
    elif x%400 == 0:
        return '윤년'
distribution()

#4
def dice(x, y, z):
    a = set(sorted(list(x, y, z)))
    if len(a) == 1:
        return 10000 + 100*x
    elif len(a) == 3: 
        return max(x, y, z)*100+1000
    elif a == 2:
        return y*100
    
print(dice(2, 2, 3))


#5
def alarm():
    x = input('00시00분:')

    y = int((x)[:2])
    z = int((x)[2:4])-45
    
   
    if z < 45:
        y -= 1
        z += 60
        
    if y < 0:
        y += 24
        
    
    return f'{y}시 {z}분'
    
print(alarm())






















