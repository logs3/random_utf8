import random

def random_symbols(length):
    random_unicodes = [chr(random.randrange(0x1F680, 0x1F6C0)) for _ in range(0, length)]
    return u"".join(random_unicodes)