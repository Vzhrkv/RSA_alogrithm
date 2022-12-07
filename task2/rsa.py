def bits_to_ascii_text(m: str) -> str:
    decrypted_msg = ''
    byte_size = 8
    i = 0
    while i < len(m):
        symbol = m[i:i + byte_size]
        ascii_symbol_num = int(symbol, 2)
        decrypted_msg += chr(ascii_symbol_num)
        i += byte_size

    return decrypted_msg


def decrypt_text(c: str, d: int, n: int):
    x = int(c, 2)
    decrypted_text = pow(x, d, n)
    bits = to_bits(decrypted_text)
    while len(bits) % 8 != 0:
        bits = '0' + bits
    return bits


def encryption(m: str, e: int, n: int) -> str:
    x = int(m, 2)
    encrypted_msg = pow(x, e, n)
    return to_bits(encrypted_msg)


def get_string_in_bits(a: str):
    b = ''
    for char in a:
        b += get_ascii_num_in_bits(char)
    return b


def get_ascii_num_in_bits(a) -> str:
    x = ord(a)
    return to_bits(x)


def to_bits(a: int) -> str:
    x = f'{a:b}'
    while len(x) < 8:
        x = '0' + x
    return x


def main():
    msg = input('Enter a message:')

    with open('public.txt') as f:
        e, n = f.read().split('\n')[:2]

    e, n = int(e), int(n)
    with open('private.txt') as f:
        d = int(f.readline())

    bits_string = get_string_in_bits(msg)
    encrypted = encryption(bits_string, e, n)

    print(bits_to_ascii_text(encrypted))

    with open('encrypted.txt', 'w+') as f:
        f.write(encrypted)

    decrypted = decrypt_text(encrypted, d, n)

    dec_ascii_text = bits_to_ascii_text(decrypted)

    with open('decrypted.txt', 'w+') as f:
        f.write(dec_ascii_text)


if __name__ == "__main__":
    main()
