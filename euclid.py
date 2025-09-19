def f(a,b):
    if a<b:
        a,b=b,a

    A, B=abs(a),abs(b)
    x0, y0 = 1, 0
    x1, y1 = 0, 1

    while B!=0:
        q=A//B
        A,B=B,A%B
        x2 = x0-q*x1
        y2 = y0-q*y1
        x0, y0 = x1, y1
        x1, y1 == x2, y2

    print(a, '*', x0, '+', b, '*', y0, '=', A)

a=int(input())
b=int(input())

f(a,b)