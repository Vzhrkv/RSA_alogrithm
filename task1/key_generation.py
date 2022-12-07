from task1.primitive_number_generator import PrimeNumberGenerator
from task1.main_algorithms import *

L = 2048
e = 65537

png = PrimeNumberGenerator(number=0, k=10, length=L)
p = png()
g = png()

phi = calculate_euler_function(p, g)

prod = p * g

if euclid_algo(phi, e) != 1:
    raise ValueError

write_file('/home/vdmr/edu/crypto/lab3/task2/public.txt', keys=(e, prod))


d = expanded_euclid_algo(phi, e)[2]


while d < 0:
    d += phi

while d > phi:
    d -= phi

write_file('/home/vdmr/edu/crypto/lab3/task2/private.txt', keys=(d, prod))
