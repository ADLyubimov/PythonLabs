a = 7
b = 2
c = 8

#Периметр
def triangle_perimeter(default_a=a, default_b=b, default_c=c):
    return (default_a + default_b + default_c)

#Площадь
def triangle_area(default_a=a, default_b=b, default_c=c):
    p = (default_a + default_b + default_c)/2
    return ((p * (p - default_a) * (p - default_b) * (p - default_c))**0,5)
