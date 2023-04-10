#1
a = [1, 6, 9, 8, 7, 6, 4, 3]
# def double(a):
#     l = []
#     for i in range(0, len(a)):
#         if (a[i]*2 in a):
#             l.append(a[i])
#     return len(l)
def double(a):
    b = {u//2 for u in a if u%2 == 0}
    return len(b.intersection(a))
print(double(a))

#2
def pascal(n): 
    def factorial(a):
        li= []
        k = 1
        for i in range(1, a+1):
            li.append(i)
        for j in range(0, len(li)-1):       
            k *= li[j]
        return k
    
    g = []
    for r in range(1, n+1): 
        f = int(factorial(n)/(factorial(r)*factorial(n-r+1)))
        g.append(f)
    return g

 
#3
def beerRefrigerator(x):
    a = []

    for i in range(1, x):
        if x%i == 0:
            for j in range(1, x):
                if (x//i)%j == 0:
                    a.append((i, j, x//i//j))

    y = int(a[0][0]*a[0][1] + a[0][2]*a[0][1]+ a[0][0]*a[0][2]) 
    l = 0
    for k in range(1, len(a)):
        t = int(a[k][0]*a[k][1] + a[k][2]*a[k][1]+ a[k][0]*a[k][2]) 
        if y > t:
            y = t
            l = k
    return f'{a[l][0]} x {a[l][1]} x {a[l][2]}'        

#5
def matrixMul(a, b):
    l = []
    for i in range(0, len(a)):
        l.append([])        
        for u in range(0, len(b[0])):
            k = 0
            for t in range(0, len(a[0])):
                k += a[i][t]*b[t][u] 
            l[i].append(k)
    return l

a = [[1, 2], [3, 4], [5, 6]]
b = [[-1, -2, 0], [0, 0, 3]]
print(matrixMul(a, b)) 

    











                


               

               
