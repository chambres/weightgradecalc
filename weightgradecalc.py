weight = input("Enter weight of major grades, minor grades, and other grades, with a space between the numbers. \nType def for the default: ")

if weight == "def":
    major_weight = 60
    minor_weight = 30
    other_weight = 10
    
else: 
    w = weight.split()
    major_weight = w[0]
    minor_weight = w[1]
    other_weight = w[2]


print("Major weight: " + str(major_weight) + ", minor weight: " + str(minor_weight) + ", other weight: " + str(other_weight))

m1 = input("Number of majors? ")
n1 = input("Number of minors? ")
o1 = input("Number of others? ")


major = int(m1)
minor = int(n1)
other = int(o1)



#major grades
maj = []
for i in range(1, major + 1):
        grade = input("Major Grade: ")
        maj.append(grade)
print("-------------------------------------------")
#minor grades
min = []
for i in range(1, minor + 1):
        grade = input("Minor Grade: ")
        min.append(grade)
print("-------------------------------------------")
#other grades
oth = []
for i in range(1, other + 1):
        grade = input("Other Grade: ")
        oth.append(grade)
print("-------------------------------------------")

totalmaj = 0.0


w1 = 60.0
w2 = 30.0
w3 = 10.0

m = 0.0
n = 0.0
o = 0.0

a = 0.0
b = 0.0
c = 0.0
for thing in maj:
	a1 = float(thing) * w1
	a = a + a1
	m = m + 60
for thing in min:
	b1 = float(thing) * w2
	b = b + b1
	n = n + 30
for thing in oth:
	c1 = float(thing) * w3
	c = c + c1
	o = o + 10
a = a + c + b



w1 = 60.0
w2 = 30.0
w3 = 10.0


c = m + n + o 


print(round(a / c, 2))
