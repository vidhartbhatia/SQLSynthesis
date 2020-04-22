from z3 import *
from itertools import *
import copy

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

# Convenience functions for creating b constraint using b flag with identifier
# 'i' that toggles whether the operator is used for operands x1 and x2.
# Use is OPTIONAL.


# def mul(i, x1, x2):
#     return (BitVec(f'B{i}', 16) & 0x0001) * (x1 * x2)


# def lor(i, x1, x2):
#     return (BitVec(f'B{i}', 16) & 0x0001) * (x1 | x2)


# def shl(i, x1, x2):
#     return (BitVec(f'B{i}', 16) & 0x0001) * (x1 << x2)


# def add(i, x1, x2):
#     return (BitVec(f'B{i}', 16) & 0x0001) * (x1 + x2)

def mul(i, x1, x2):
    return (i & 0x0001) * (x1 * x2)


def lor(i, x1, x2):
    return (i & 0x0001) * (x1 | x2)


def shl(i, x1, x2):
    return (i & 0x0001) * (x1 << x2)


def add(i, x1, x2):
    return (i & 0x0001) * (x1 + x2)

# Your Synthesizer: construct b Z3 formula using input/output pairs.


def formula(pairs):
    constraints = []

    # create variables and constraints that will be common across each input/output pair
    a1, a2, a3, a4 = BitVecs('a1 a2 a3 a4', 16)
    b1, b2, b3, b4 = BitVecs('b1 b2 b3 b4', 16)
    c1, c2, c3, c4 = BitVecs('c1 c2 c3 c4', 16)
    d1, d2, d3, d4 = BitVecs('d1 d2 d3 d4', 16)
    p1, p2, p3, p4 = BitVecs('p1 p2 p3 p4', 16)
    q1, q2, q3, q4 = BitVecs('q1 q2 q3 q4', 16)
    r1, r2, r3, r4 = BitVecs('r1 r2 r3 r4', 16)

    # yes i realized after that i can do it in a for loop :(
    constraints.append(a1 + a2 + a3 + a4 == 1)
    constraints.append(a1 >= 0)
    constraints.append(a2 >= 0)
    constraints.append(a3 >= 0)
    constraints.append(a4 >= 0)
    constraints.append(a1 <= 1)
    constraints.append(a2 <= 1)
    constraints.append(a3 <= 1)
    constraints.append(a4 <= 1)
    constraints.append(b1 + b2 + b3 + b4 == 1)
    constraints.append(b1 >= 0)
    constraints.append(b2 >= 0)
    constraints.append(b3 >= 0)
    constraints.append(b4 >= 0)
    constraints.append(b1 <= 1)
    constraints.append(b2 <= 1)
    constraints.append(b3 <= 1)
    constraints.append(b4 <= 1)
    constraints.append(c1 + c2 + c3 + c4 == 1)
    constraints.append(c1 >= 0)
    constraints.append(c2 >= 0)
    constraints.append(c3 >= 0)
    constraints.append(c4 >= 0)
    constraints.append(c1 <= 1)
    constraints.append(c2 <= 1)
    constraints.append(c3 <= 1)
    constraints.append(c4 <= 1)
    constraints.append(d1 + d2 + d3 + d4 == 1)
    constraints.append(d1 >= 0)
    constraints.append(d2 >= 0)
    constraints.append(d3 >= 0)
    constraints.append(d4 >= 0)
    constraints.append(d1 <= 1)
    constraints.append(d2 <= 1)
    constraints.append(d3 <= 1)
    constraints.append(d4 <= 1)
    constraints.append(p1 + p2 + p3 + p4 == 1)
    constraints.append(p1 >= 0)
    constraints.append(p2 >= 0)
    constraints.append(p3 >= 0)
    constraints.append(p4 >= 0)
    constraints.append(p1 <= 1)
    constraints.append(p2 <= 1)
    constraints.append(p3 <= 1)
    constraints.append(p4 <= 1)
    constraints.append(q1 + q2 + q3 + q4 == 1)
    constraints.append(q1 >= 0)
    constraints.append(q2 >= 0)
    constraints.append(q3 >= 0)
    constraints.append(q4 >= 0)
    constraints.append(q1 <= 1)
    constraints.append(q2 <= 1)
    constraints.append(q3 <= 1)
    constraints.append(q4 <= 1)
    constraints.append(r1 + r2 + r3 + r4 == 1)
    constraints.append(r1 >= 0)
    constraints.append(r2 >= 0)
    constraints.append(r3 >= 0)
    constraints.append(r4 >= 0)
    constraints.append(r1 <= 1)
    constraints.append(r2 <= 1)
    constraints.append(r3 <= 1)
    constraints.append(r4 <= 1)

    constraints.append(a1 + b1 + c1 + d1 == 1)
    constraints.append(a2 + b2 + c2 + d2 == 1)
    constraints.append(a3 + b3 + c3 + d3 == 1)
    constraints.append(a4 + b4 + c4 + d4 == 1)


    for i, pair in enumerate(pairs):
        ans = pair[1]
        inputs = pair[0]
        constraint_for_pair = []

        # create constraints for picking the bijection from input to leaf nodes
        W, X, Y, Z = inputs
        A, B, C, D, P, Q = BitVecs(f'A{i} B{i} C{i} D{i} P{i} Q{i}', 16)
        constraint_for_pair.append((A == (W * (a1 & 0x0001)) + (X * (a2 & 0x0001)) +
                                    (Y * (a3 & 0x0001)) + (Z * (a4 & 0x0001))))
        constraint_for_pair.append((B == (W * (b1 & 0x0001)) + (X * (b2 & 0x0001)) +
                                    (Y * (b3 & 0x0001)) + (Z * (b4 & 0x0001))))
        constraint_for_pair.append((C == (W * (c1 & 0x0001)) + (X * (c2 & 0x0001)) +
                                    (Y * (c3 & 0x0001)) + (Z * (c4 & 0x0001))))
        constraint_for_pair.append((D == (W * (d1 & 0x0001)) + (X * (d2 & 0x0001)) +
                                    (Y * (d3 & 0x0001)) + (Z * (d4 & 0x0001))))

        # for each tree form create constraints to pick operators

        # ((A B)(C D))
        # constraint_for_pair.append(
        #     P == mul(p1, A, B) + lor(p2, A, B) + shl(p3, A, B) + add(p4, A, B))
        # constraint_for_pair.append(
        #     Q == mul(q1, C, D) + lor(q2, C, D) + shl(q3, C, D) + add(q4, C, D))
        # constraint_for_pair.append(
        #     ans == mul(r1, P, Q) + lor(r2, P, Q) + shl(r3, P, Q) + add(r4, P, Q))

        # # (A (B (C D)))
        # constraint_for_pair.append(
        #     Q == mul(q1, C, D) + lor(q2, C, D) + shl(q3, C, D) + add(q4, C, D))
        # constraint_for_pair.append(
        #     P == mul(p1, B, Q) + lor(p2, B, Q) + shl(p3, B, Q) + add(p4, B, Q))
        # constraint_for_pair.append(
        #     ans == mul(r1, A, P) + lor(r2, A, P) + shl(r3, A, P) + add(r4, A, P))

        # # (A ((B C) D))
        # constraint_for_pair.append(
        #     P == mul(p1, B, C) + lor(p2, B, C) + shl(p3, B, C) + add(p4, B, C))
        # constraint_for_pair.append(
        #     Q == mul(q1,P , D) + lor(q2, P, D) + shl(q3, P, D) + add(q4, P, D))
        # constraint_for_pair.append(
        #     ans == mul(r1, A, Q) + lor(r2, A, Q) + shl(r3, A, Q) + add(r4, A, Q))

        # constraints.extend(constraint_for_pair)

        # ((A (B C)) D)
        constraint_for_pair.append(
            P == mul(p1, B, C) + lor(p2, B, C) + shl(p3, B, C) + add(p4, B, C))
        constraint_for_pair.append(
            Q == mul(q1, A, P) + lor(q2, A, P) + shl(q3, A, P) + add(q4, A, P))
        constraint_for_pair.append(
            ans == mul(r1, Q, D) + lor(r2, Q, D) + shl(r3, Q, D) + add(r4, Q, D))

        constraints.extend(constraint_for_pair)

        # SOLUTION found!!!! - order: D B A C - operations  (D | (B * A)) << C

    return constraints


if __name__ == '__main__':
    s = tuple(formula(io_pairs))
    print(f'Z3 formula: {s}')
    # solve(*s)

    s = Solver()
    for x in formula(io_pairs):
        s.add(x)
    if s.check() == sat:
        print('Z3 Solution:')

        m = s.model()
        print(sorted([(d, m[d]) for d in m], key=lambda x: str(x[0])))

    else:
        print("no solution ")
