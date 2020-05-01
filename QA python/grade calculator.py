#learning python
#grade calculator code 

physics =int(input("enter your physics mark"))
chemistry =int(input("enter your chemistry mark"))
maths =int(input("enter your maths mark")) 
total = (physics + chemistry + maths)
percentage =(total/300 * 100)
print ("you got", percentage)
if percentage < 40:
    print("try again")
if percentage >= 40 and percentage <50:
    print("you got a D")
if percentage >= 50 and percentage <60:
    print("you got a c")
if percentage >= 60 and percentage <70:
    print("you got a b")
if percentage >= 70:
    print ("you got an a, well done!")
