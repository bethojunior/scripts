import itertools
import argparse


def generate_variations_name(name):
    results = list(map(''.join, itertools.product(*zip(name.upper(), name.lower()))))
    return results


def generate_txt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name')
    parser.add_argument('--add')
    args = parser.parse_args()

    name = args.name
    add = args.add

    variations = generate_variations_name(name)
    with open(f'{name}-variations', 'w', buffering=-1, encoding='utf-8') as f:
        for variation in variations:
            data = f'{add}{variation}\n{variation}{add}\n'
            f.write(data)


if __name__ == '__main__':
    generate_txt()