import argparse
from itertools import combinations

parser = argparse.ArgumentParser()
parser.add_argument("--params", type=int, nargs="+", help="List of parameters", required=True)
parser.add_argument("--output", type=str, help="Output file", required=True)
parser.add_argument("--values", type=float, nargs="+", help="List of values", required=True)
parser.add_argument("--values2d", type=float, nargs="+", help="List of values", required=True)
args = parser.parse_args()

output = open(args.output, "w")
output.write("change helicity False\nchange rwgt_dir rwgt\n")

N_param = len(args.params)
N_values = len(args.values)
N_values2d = len(args.values2d)

nrgwt = 0

output.write(f"\nlaunch --rwgt_name=rw{nrgwt}\n")
nrgwt += 1
for par in args.params:
    output.write(f"set smeft {par} 0\n")

# Single op
for i in range(N_param):
    # Add all the single weight lines
    for value in args.values:
        output.write(f"\nlaunch --rwgt_name=rw{nrgwt}\n")
        nrgwt+=1
        for j in range(N_param):
            if i == j:
                output.write(f"set smeft {args.params[j]} {value}\n")
            else:
                output.write(f"set smeft {args.params[j]} 0\n")


# Multiple ops
for value1_ in range(N_values2d):
    value1 = args.values2d[value1_]
    for value2_ in range(N_values2d):
        value2 = args.values2d[value2_]

        comb = combinations(list(range(N_param)), 2)
        for i,j in comb:
            output.write(f"\nlaunch --rwgt_name=rw{nrgwt}\n")
            nrgwt+=1
            for z in range(N_param):
                if z == i:
                    output.write(f"set smeft {args.params[z]} {value1}\n")
                elif z == j:
                    output.write(f"set smeft {args.params[z]} {value2}\n")
                else:
                    output.write(f"set smeft {args.params[z]} 0\n")

output.close()
    
    # for j in range(N_param):
    #     print(f"param {args.params[i]} = {args.values[j]}")-
