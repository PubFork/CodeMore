#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('square', help="display a square of a given number")
args = parser.parse_args()
print(args.echo**2)
