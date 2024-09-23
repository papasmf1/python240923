# function2.py 
#일반 함수
def times(a,b):
    return a*b

#람다 함수 정의 
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))

print( (lambda x:x*x)(3) )

print(globals())


