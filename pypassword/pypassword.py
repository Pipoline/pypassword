import string
import random
import argparse


def password_generator(size=6,
                       chars=string.ascii_letters + string.digits,
                       special=False):
    """
    Generate password
    :param size: Size is number of chars
    :param chars: Charset
    :param special: Boolean, us special characters or not
    :return: Random string
    """
    if special:
        chars += string.punctuation
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))


if __name__ == "__main__":
    size = 14
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--size", help="Random string size", type=int)
    parser.add_argument("-x", help="Use special characters", action="store_true")

    args = parser.parse_args()
    if args.size:
        size = args.size

    print(password_generator(size=size,
                             special=args.x))
