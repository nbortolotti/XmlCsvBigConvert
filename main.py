__author__ = 'nickbortolotti'

import argparse
from bigxmlcsv import xmlcsv

if __name__ == '__main__':
    pa = argparse.ArgumentParser(description='convert big xml to csv')
    pa.add_argument('--input', dest='input_file', required=True, help='input xml filename')
    pa.add_argument('--output', dest='output_file', required=True, help='output csv filename')
    pa.add_argument('--row', dest='row', required=True, help='xml initial node. iterative node')
    pa.add_argument('--schema', dest='schema', required=True, help='schema to transform')

    args = pa.parse_args()
    lista = args.schema.split(",")
    demo = list(lista)

    result = xmlcsv(args.input_file, args.output_file, args.row, demo)

