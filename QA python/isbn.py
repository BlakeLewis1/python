#learning python
#ISBN

num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
num4=int(input("enter the fourth number"))
num5=int(input("enter the fifth number"))
num6=int(input("enter the sixth number"))
num7=int(input("enter the seventh number"))
num8=int(input("enter the eighth number"))
num9=int(input("enter the ninth number"))
num10=int(input("enter the tenth number"))
num11=int(input("enter the eleventh number"))
num12=int(input("enter the twelth number"))     


if num1 % 2 != 0:
    odd = (num1 + 3*num2 + num3 + 3*num4 + num5 + 3*num6 + num7 + 3*num8 + num9 + 3*num10 + num11 + 3*num12)
    ans1 = (odd%10)
    ans = (ans1-10)
    num13=round(ans)
    print(num1,num2,num3,num4,num5,num6,num8,num9,num10,num11,num12,num13)
if num1 % 2 == 0:
    even = (num1*3 + 3*num2 + num3 + 3*num4 + num5 + 3*num6 + num7 + 3*num8 + num9 + 3*num10 + num11 + 3*num12)
    ans2 = (even%10)
    ans = (ans2-10)
    num13e=round(ans)
    print(num1,num2,num3,num4,num5,num6,num8,num9,num10,num11,num12,num13e)
    

#( 10 – (( x1 + 3^2 + *3 + 3^4 + *5 + 3^6 + *7 + 3^8 + *9 + 3^10 + *11 + 3^12 ) % 10))

#odd = num1 + 3*num2 + num3 + 3*num4+ num5+ 3*num6+ num7 + 3*num8
