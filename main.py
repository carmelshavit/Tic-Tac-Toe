x = 1
print(x)


if False:
    print("False!")
elif x < 0:
    print("x is negative")
else:
    print("weeee")


s0 = ''
s9 = 'a'
s1 = 'abc'
s2 = "abc"
s3 = """abc"""

if s1 == s2 and s2 == s3 or s0:
    print("Equals stuff")

my_none = None

if my_none:
    pass

if 0:
    pass

if my_none is None:
    # This is true.
    pass

if my_none is not None:
    # This is False.
    pass

if my_none == None:
    # This is true.
    pass

my_bool = True

if my_bool is False:
    print("my bool is false")

if 5 == "5":
    # This is false...
    pass

a = 5

while a > 0:
    print("Value of a is", a)
    a -= 1

#####################

l0 = []
l2 = list()

l = [0, -1, "wee"]

l.append(1)
l.append("2")
l.append(True)

print(l[0])

d0 = {}
d2 = dict()  # object in JS

d = {0: 0, -1: "-1"}

d['a'] = 1
d['b'] = 2
d.update(b=3, c=4)

print(d["a"])


#############################

def f():
    pass


def add_numbers(a: int, b: int):
    return a + b


my_sum = add_numbers(1, 2)
print("my sum is", my_sum)

my_longer_str = add_numbers("abc", "def")
print("my str is", my_longer_str)

my_longer_arr = add_numbers([1, 2, 3], [4, 5, 6])
print("my arr is", my_longer_arr)


#####################


try:
    raise Exception("Weeee")
except Exception as e:
    print(e)
finally:
    print("finally...")


mylist = [1, 2, 3, 4, 5]
for item in mylist:
    print(item)

for i in range(10):
    print(i)

###################


class Cat:

    def __init__(self, name: str = None):
        # self is an object
        self.name: str | None = name

    def meow(self):
        print("Meowwwwwwwwwwww")

    def say_my_name(self):
        if self.name is None:
            print("I have no name")
        else:
            # print("My name is", self.name)
            print(f"My name is {self.name}")


my_cat = Cat("Kelev")
my_nameless_cat = Cat()

my_cat.meow()
Cat.meow(my_cat)

my_cat.say_my_name()

print(my_cat.name)

###########################
