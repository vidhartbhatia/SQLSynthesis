from z3 import *
from itertools import *

# IO Pairs:
#   IN: (11, 6, 9, 4)    OUT:  35840
#   IN: (9, 12, 10, 1)   OUT:  46080
#   IN: (2, 4, 0, 4)     OUT:     12
#   IN: (14, 8, 10, 3)   OUT:  52224
#   IN: (1, 13, 9, 4)    OUT:   6656
#   IN: (4, 2, 8, 0)     OUT:   2048
#   IN: (15, 6, 12, 4)   OUT:  57344
#   IN: (7, 12, 6, 0)    OUT:   5376
#   IN: (2, 0, 6, 0)     OUT:      0
#   IN: (16, 4, 3, 1)    OUT:    520

io_pairs = [
    ((11, 6, 9, 4), 35840),
    ((9, 12, 10, 1), 46080),
    ((2, 4, 0, 4), 12),
    ((14, 8, 10, 3), 52224),
    ((1, 13, 9, 4), 6656),
    ((4, 2, 8, 0), 2048),
    ((15, 6, 12, 4), 57344),
    ((7, 12, 6, 0), 5376),
    ((2, 0, 6, 0), 0),
    ((16, 4, 3, 1), 520),
]

# Convenience functions for creating a constraint using a flag with identifier
# 'i' that toggles whether the operator is used for operands x1 and x2.
# Use is OPTIONAL.
def mul(b, x1, x2):
    return (b & 0x0001) * (x1 * x2)

def lor(b, x1, x2):
    return (b & 0x0001) * (x1 | x2)

def shl(b, x1, x2):
    return (b & 0x0001) * (x1 << x2)

def add(b, x1, x2):
    return (b & 0x0001) * (x1 + x2)

# Your Synthesizer: construct a Z3 formula using input/output pairs.
def formula(pairs):
    n = len(pairs)

    # indicator variables for mapping inputs to W, X, Y, Z
    a_vars = [BitVec(f'a{i}', 16) for i in range(4)]
    b_vars = [BitVec(f'b{i}', 16) for i in range(4)]
    c_vars = [BitVec(f'c{i}', 16) for i in range(4)]
    d_vars = [BitVec(f'd{i}', 16) for i in range(4)]

    # W, X, Y, Z for each A, B, C, D (probably didn't need a new variable for
    # each input)
    W_vars = [BitVec(f'W{i}', 16) for i in range(n)]
    X_vars = [BitVec(f'X{i}', 16) for i in range(n)]
    Y_vars = [BitVec(f'Y{i}', 16) for i in range(n)]
    Z_vars = [BitVec(f'Z{i}', 16) for i in range(n)]

    # operator indicator variables
    o_vars = [BitVec(f'o{i}', 16) for i in range(12)]

    # inner nodes
    N_vars = [BitVec(f'N{i}', 16) for i in range(3)]

    # all indicator variables should be >= 0 and <= 1
    bit_vars = a_vars + b_vars + c_vars + d_vars + o_vars
    constraints = [And(0 <= i, i <= 1) for i in bit_vars]

    # for a one-to-one mapping
    constraints += [a_vars[i] + b_vars[i] + c_vars[i] + d_vars[i] == 1 for i in range(4)]
    constraints.append(a_vars[0] + a_vars[1] + a_vars[2] + a_vars[3] == 1)
    constraints.append(b_vars[0] + b_vars[1] + b_vars[2] + b_vars[3] == 1)
    constraints.append(c_vars[0] + c_vars[1] + c_vars[2] + c_vars[3] == 1)
    constraints.append(d_vars[0] + d_vars[1] + d_vars[2] + d_vars[3] == 1)

    # so that only one operator is used in a subexpression
    constraints.append(o_vars[0] + o_vars[1] + o_vars[2] + o_vars[3] == 1)
    constraints.append(o_vars[4] + o_vars[5] + o_vars[6] + o_vars[7] == 1)
    constraints.append(o_vars[8] + o_vars[9] + o_vars[10] + o_vars[11] == 1)

    for i in range(n):
        ith_input = pairs[i][0]
        W_vars[i] = (a_vars[0] & 0x0001) * ith_input[0] + (b_vars[0] & 0x0001) * ith_input[1] + (c_vars[0] & 0x0001) * ith_input[2] + (d_vars[0] & 0x0001) * ith_input[3]
        X_vars[i] = (a_vars[1] & 0x0001) * ith_input[0] + (b_vars[1] & 0x0001) * ith_input[1] + (c_vars[1] & 0x0001) * ith_input[2] + (d_vars[1] & 0x0001) * ith_input[3]
        Y_vars[i] = (a_vars[2] & 0x0001) * ith_input[0] + (b_vars[2] & 0x0001) * ith_input[1] + (c_vars[2] & 0x0001) * ith_input[2] + (d_vars[2] & 0x0001) * ith_input[3]
        Z_vars[i] = (a_vars[3] & 0x0001) * ith_input[0] + (b_vars[3] & 0x0001) * ith_input[1] + (c_vars[3] & 0x0001) * ith_input[2] + (d_vars[3] & 0x0001) * ith_input[3]

    # trees 1 and 2 produce solutions

    # Tree #1: 
    #   /\
    #  /\
    # /\

    for i in range(n):
        N_vars[0] = mul(o_vars[0], W_vars[i], X_vars[i]) + lor(o_vars[1], W_vars[i], X_vars[i]) + shl(o_vars[2], W_vars[i], X_vars[i]) + add(o_vars[3], W_vars[i], X_vars[i])
        N_vars[1] = mul(o_vars[4], N_vars[0], Y_vars[i]) + lor(o_vars[5], N_vars[0], Y_vars[i]) + shl(o_vars[6], N_vars[0], Y_vars[i]) + add(o_vars[7], N_vars[0], Y_vars[i])
        N_vars[2] = mul(o_vars[8], N_vars[1], Z_vars[i]) + lor(o_vars[9], N_vars[1], Z_vars[i]) + shl(o_vars[10], N_vars[1], Z_vars[i]) + add(o_vars[11], N_vars[1], Z_vars[i])
        constraints.append(N_vars[2] == pairs[i][1])

    # Tree #2: 
    #   /\
    #  /\
    #   /\

    # for i in range(n):
    #     N_vars[0] = mul(o_vars[0], W_vars[i], X_vars[i]) + lor(o_vars[1], W_vars[i], X_vars[i]) + shl(o_vars[2], W_vars[i], X_vars[i]) + add(o_vars[3], W_vars[i], X_vars[i])
    #     N_vars[1] = mul(o_vars[4], Y_vars[i], N_vars[0]) + lor(o_vars[5], Y_vars[i], N_vars[0]) + shl(o_vars[6], Y_vars[i], N_vars[0]) + add(o_vars[7], Y_vars[i], N_vars[0])
    #     N_vars[2] = mul(o_vars[8], N_vars[1], Z_vars[i]) + lor(o_vars[9], N_vars[1], Z_vars[i]) + shl(o_vars[10], N_vars[1], Z_vars[i]) + add(o_vars[11], N_vars[1], Z_vars[i])
    #     constraints.append(N_vars[2] == pairs[i][1])

    # Tree #3: 
    #   /\
    #  /\/\ 

    # for i in range(n):
    #     N_vars[0] = mul(o_vars[0], W_vars[i], X_vars[i]) + lor(o_vars[1], W_vars[i], X_vars[i]) + shl(o_vars[2], W_vars[i], X_vars[i]) + add(o_vars[3], W_vars[i], X_vars[i])
    #     N_vars[1] = mul(o_vars[4], Y_vars[i], Z_vars[i]) + lor(o_vars[5], Y_vars[i], Z_vars[i]) + shl(o_vars[6], Y_vars[i], Z_vars[i]) + add(o_vars[7], Y_vars[i], Z_vars[i])
    #     N_vars[2] = mul(o_vars[8], N_vars[0], N_vars[1]) + lor(o_vars[9], N_vars[0], N_vars[1]) + shl(o_vars[10], N_vars[0], N_vars[1]) + add(o_vars[11], N_vars[0], N_vars[1])
    #     constraints.append(N_vars[2] == pairs[i][1])

    # Tree #4:
    #   /\
    #    /\
    #   /\

    # for i in range(n):
    #     N_vars[0] = mul(o_vars[0], W_vars[i], X_vars[i]) + lor(o_vars[1], W_vars[i], X_vars[i]) + shl(o_vars[2], W_vars[i], X_vars[i]) + add(o_vars[3], W_vars[i], X_vars[i])
    #     N_vars[1] = mul(o_vars[4], N_vars[0], Y_vars[i]) + lor(o_vars[5], N_vars[0], Y_vars[i]) + shl(o_vars[6], N_vars[0], Y_vars[i]) + add(o_vars[7], N_vars[0], Y_vars[i])
    #     N_vars[2] = mul(o_vars[8], Z_vars[i], N_vars[1]) + lor(o_vars[9], Z_vars[i], N_vars[1]) + shl(o_vars[10], Z_vars[i], N_vars[1]) + add(o_vars[11], Z_vars[i], N_vars[1])
    #     constraints.append(N_vars[2] == pairs[i][1])

    # Tree #5: 
    #   /\
    #    /\
    #     /\

    # for i in range(n):
    #     N_vars[0] = mul(o_vars[0], W_vars[i], X_vars[i]) + lor(o_vars[1], W_vars[i], X_vars[i]) + shl(o_vars[2], W_vars[i], X_vars[i]) + add(o_vars[3], W_vars[i], X_vars[i])
    #     N_vars[1] = mul(o_vars[4], Y_vars[i], N_vars[0]) + lor(o_vars[5], Y_vars[i], N_vars[0]) + shl(o_vars[6], Y_vars[i], N_vars[0]) + add(o_vars[7], Y_vars[i], N_vars[0])
    #     N_vars[2] = mul(o_vars[8], Z_vars[i], N_vars[1]) + lor(o_vars[9], Z_vars[i], N_vars[1]) + shl(o_vars[10], Z_vars[i], N_vars[1]) + add(o_vars[11], Z_vars[i], N_vars[1])
    #     constraints.append(N_vars[2] == pairs[i][1])

    return constraints

if __name__ == '__main__':
    s = formula(io_pairs)
    print(f'Z3 formula: {s}')
    print('Z3 Solution:')
    solve(s)