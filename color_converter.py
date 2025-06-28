import argparse
import random
import sys


def hex_to_rgb(hex_value: str):
    hex_value = hex_value.lstrip('#')
    if len(hex_value) == 3:
        hex_value = ''.join(2 * c for c in hex_value)
    if len(hex_value) != 6:
        raise ValueError('Hex value must be 3 or 6 hex digits long')
    r = int(hex_value[0:2], 16)
    g = int(hex_value[2:4], 16)
    b = int(hex_value[4:6], 16)
    return r, g, b


def rgb_to_hex(rgb_value: str):
    parts = [int(p) for p in rgb_value.split(',')]
    if len(parts) != 3 or any(p < 0 or p > 255 for p in parts):
        raise ValueError('RGB must be three numbers between 0 and 255 separated by commas')
    return '#{0:02x}{1:02x}{2:02x}'.format(*parts)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def main():
    parser = argparse.ArgumentParser(description='Convert colors between hex and rgb.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--hex', dest='hex', help='Hex color (e.g. "#ff0000" or "fff")')
    group.add_argument('--rgb', dest='rgb', help='RGB color as "R,G,B" (0-255 values)')
    group.add_argument('--random', action='store_true', help='Generate a random color')
    args = parser.parse_args()

    if args.hex:
        r, g, b = hex_to_rgb(args.hex)
        print(f'RGB: {r}, {g}, {b}')
    elif args.rgb:
        hex_value = rgb_to_hex(args.rgb)
        print(f'Hex: {hex_value}')
    elif args.random:
        r, g, b = random_color()
        print(f'RGB: {r}, {g}, {b}')
        print(f'Hex: #{r:02x}{g:02x}{b:02x}')
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
