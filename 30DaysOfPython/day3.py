age=22
height=1.85
num1=2+2j
base=int(input('Enter the Base: '))
height=int(input('Enter the height: '))
area=0.5*base*height
print('the area of the triangle is ',area)

# side_a=int(input('Enter side a: '))
# side_b=int(input('Enter side b: '))
# side_c=int(input('Enter side c: '))
# perimeter=side_a+side_b+side_c
# print('the perimeter of the triangle is',perimeter)

# length=int(input('Enter the lenght: '))
# width=int(input('Enter the width: '))
# area=length*width
# perimeter=2*(length+width)
# print('the area of the rectangle is',area)
# print('the perimeter of the rectangle is',perimeter)

# radius=int(input('Enter the radius'))
# pi=3.14
# area=pi*radius**2
# print('the area of the circle is ',area)

#y-intercept
# x=0
# y=2*x+-2
# print(y)

# #x-intercept
# y=0
# x=(y-2)/2
# print(x)

#slope
x_difference=0+1
y_difference=-2-0
slope=y_difference/x_difference
print(slope)

y1=2
y2=10
x1=2
x2=6

slope_2=(y2-y1)/(x2-x1)
print(slope_2)

#euclidean distance
#d=sqrt((x2-x1)**2+(y2-y1)**2)
import math
distance=math.sqrt((6-2)**2+(10-2)**2)
print(distance)

#comparing slopes
print(slope<=slope_2)

x=0
y=0**2+6*0+9
x_2=-3
y_2=x_2**2+6*x_2+9
print(y_2)
#answer of x when y=0 is -3

print(len('python')>len('dragon'))
print('on' in 'python' and 'on'in'dragon')
print('jargon' in 'i hope this course is not full of jargon')
print('on'not in 'dragon'and 'on 'not in 'python')
tofloat=len('python')
print(type(str(float(tofloat))))

# number=(int(input('Enter any number: ')))
# if(number%2==0):
#     print('even')
# else:
#     print('odd')


print(7//3 is 2.7 )
print('10' is 10)
print(int(9.8) is 10)

# hours=int(input('enter the hours: '))
# rate=int(input('enter the rate: '))
# weekly_earnings=hours*rate
# print('your weekly earnings is ',weekly_earnings)

years=int(input('Enter the number of years you have lived: '))
seconds=years*365*24*60*60
print(f'you have lived {seconds} seconds')



