inpt1 = int(input('enter base: '))
inpt2 = int(input('enter height: '))
inpt3 = int(input('enter hypotenus: '))


def get_area(base, height):
   return 0.5 * base * height

def get_per(base, height, hypo):
    return base + height + hypo

print("area of the triangle is: ")
print(get_area(inpt1, inpt2))
print()
print('the perimeter of the triangle is')
print(get_per(inpt1, inpt2, inpt3))
