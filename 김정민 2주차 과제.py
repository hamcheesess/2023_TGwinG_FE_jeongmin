#1 
def sum(a, b):
    f = a + b #side effect
    return f 
#함수를 실행 - a, b 를 입력값으로 바꾸고(프레임에서 함수명과 변수 저장), 명령어 하나씩 해석해감.
#return은 '식(여기선 f)의 계산 결과'를 함수의 결과값으로 치환하고 함수를 종료

#2
def sub(a, b):
    return a - b #순수함수


#3
def mul(a, b):
    return a * b


#4
def div(a, b):
    return a / b


#5
def dis(w, x, y, z):
    d = ((w-x)**2 + (y-z)**2)**1/2
    return d

#6
def title():
    lyrics = "switch sides and I'm beside you.- don't look back in anger"
    a =  lyrics.find("beside you")
    if a == -1:
        pass
    else:
        print("beside you")
    return 

'''a = lyrics[21:31]
   return a
print(title()) #방법2
'''
    

#7
def reverseString(string):
    a = string
    return a[::-1]


#8
def introduce():
    x = input('이름')
    y = input('취미')
    w = input('재학중인 학교')
    z = input('생일yymmdd')
    a = f'제 이름은 {x}입니다. 취미는{y}입니다. 저는{w}를 다니고 있습니다. 제 생일은 {z[2:4]}월 {z[4:6]}일 입니다. '
    return x, w, y, z, a


#9
def calc():
    x = input('첫 번째 수')
    y = input('두 번째 수')
    a = int(x) + int(y)
    b = int(x) - int(y)
    c = int(x) * int(y)
    d = int(x) % int(y)

    return a, b, c, d


   




