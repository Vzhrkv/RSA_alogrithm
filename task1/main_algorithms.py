from typing import Tuple


def euclid_algo(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError(f"Pairs of numbers must be integer not float {a} -  {type(a)}; {b} - {type(b)}")
    while b != 0:
        t = a % b
        a = b
        b = t
    return a


def expanded_euclid_algo(m: int, n: int) -> Tuple[int, int, int]:
    a, b = m, n
    u1, v1 = 1, 0
    u2, v2 = 0, 1
    while b != 0:
        q = a // b
        r = a % b
        a = b
        b = r
        r = u2
        u2 = u1 - q * u2
        u1 = r
        r = v2
        v2 = v1 - q * v2
        v1 = r

    if v1 < 0:
        while v1 < 0:
            v1 += m
    return a, u1, v1


def calculate_euler_function(p: int, g: int) -> int:
    return (p - 1) * (g - 1)


def get_prime_number(p: int, g: int, e: int):
    """Function to get prime number that less than n and euler's function of n"""
    phi = calculate_euler_function(p, g)
    return expanded_euclid_algo(phi, e)[2]


def write_file(file: str, keys: Tuple[int, int]):
    keys = [str(key) for key in keys]
    with open(file, 'w+') as f:
        for key in keys:
            f.write(f'{key}\n')


def read_file(file: str) -> str:
    t = []
    with open(file) as f:
        for line in f:
            t += [line.rstrip()]
    return " ".join(t)


if __name__ == "__main__":
    print(euclid_algo(31, 13))
    # print(euclid_algo(12.1, 2))
    print(euclid_algo(2 << 136, 2 << 128))
    print(expanded_euclid_algo(7, 76))
    print(expanded_euclid_algo(4, 62))
    print(expanded_euclid_algo(157, 3))
