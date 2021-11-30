#!/usr/bin/env python

from svgpath2mpl import parse_path
import argparse, numpy as np, matplotlib.pyplot as plt, pandas as pd
from xml.dom import minidom

def getopts():
    parser = argparse.ArgumentParser(description='Grade an input pattern.')
    subparsers = parser.add_subparsers(help='TODO: Add help statement here.')
    parser_read = subparsers.add_parser('convert_sample', help='Read sample pattern from SVG file.')
    parser_read.add_argument('input', type=str, help='Path to the input pattern.')
    parser_read.add_argument('output', type=str, help='Path to the excel file (a ".dat" file will also be created in the same location).')
    parser_show = subparsers.add_parser('show_grades', help='Show the current graded versions of the sample pattern.')
    parser_show.add_argument('input', type=str, help='Path to the excel file containing the graded patterns.')
    parser_save = subparsers.add_parser('save_grades', help='Save graded patterns to a directory.')
    parser_save.add_argument('input', type=str, help='Path to the excel file that contains the graded patterns. There must also be a ".dat" file in the same location.')
    parser_save.add_argument('output', type=str, help='Path to a directory (must not exist yet) where to save the graded patterns.')
    parsed = parser.parse_args()
    if len(vars(parsed)) == 0:
        parser.print_help()
    else:
        df = pd.DataFrame.from_dict(vars(parsed))
        print(df)
    return parsed

def main():
    args = getopts()

if __name__ == "__main__":
    main()
