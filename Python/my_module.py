# Using a module and packages in Pytthon
import salute
from salute import fruits
import random
import platform
from healthy import foo

salute.say_hello("Ben")
print(fruits["name"])

x = random.random()
print(x)

y = random.randint(0,50)
print(y)

j = platform.system()
print(j)

foo.fruits("Apple")

m = dir(random)
print(m)