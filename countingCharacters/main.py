# Connor Pavicic, countingCharacters

list1 = list(input('Type a list: ').lower())
list2 = list(input('Type another list: ').lower())
list3 = list(input('Type another list: ').lower())
list4 = list(input('Type another list: ').lower())
list5 = list(input('Type another list: ').lower())

grid = [list1, list2, list3, list4, list5]

A_count = 0
B_count = 0
C_count = 0
D_count = 0
E_count = 0
F_count = 0
G_count = 0
H_count = 0
I_count = 0
J_count = 0
K_count = 0
L_count = 0
M_count = 0
N_count = 0
O_count = 0
P_count = 0
Q_count = 0
R_count = 0
S_count = 0
T_count = 0
U_count = 0
V_count = 0
W_count = 0
X_count = 0
Y_count = 0
Z_count = 0

for A in grid:
    for a in A:
        if a == 'a':
            A_count += 1

for B in grid:
    for b in B:
        if b == 'b':
            B_count += 1

for C in grid:
    for c in C:
        if c == 'c':
            C_count += 1

for D in grid:
    for d in D:
        if d == 'd':
            D_count += 1

for E in grid:
    for e in E:
        if e == 'e':
            E_count += 1

for F in grid:
    for f in F:
        if f == 'f':
            F_count += 1

for G in grid:
    for g in G:
        if g == 'g':
            G_count += 1

for H in grid:
    for h in H:
        if h == 'h':
            H_count += 1

for I in grid:
    for i in I:
        if i == 'i':
            I_count += 1

for J in grid:
    for j in J:
        if j == 'j':
            J_count += 1

for K in grid:
    for k in K:
        if k == 'k':
            K_count += 1

for L in grid:
    for l in L:
        if l == 'l':
            L_count += 1

for M in grid:
    for m in M:
        if m == 'm':
            M_count += 1

for N in grid:
    for n in N:
        if n == 'n':
            N_count += 1

for O in grid:
    for o in O:
        if o == 'o':
            O_count += 1

for P in grid:
    for p in P:
        if p == 'p':
            P_count += 1

for Q in grid:
    for q in Q:
        if q == 'q':
            Q_count += 1

for R in grid:
    for r in R:
        if r == 'r':
            R_count += 1

for S in grid:
    for s in S:
        if s == 's':
            S_count += 1

for T in grid:
    for t in T:
        if t == 't':
            T_count += 1

for U in grid:
    for u in U:
        if u == 'u':
            U_count += 1

for V in grid:
    for v in V:
        if v == 'v':
            V_count += 1

for W in grid:
    for w in W:
        if w == 'w':
            W_count += 1

for X in grid:
    for x in X:
        if x == 'x':
            X_count += 1

for Y in grid:
    for y in Y:
        if y == 'y':
            Y_count += 1

for Z in grid:
    for z in Z:
        if z == 'z':
            Z_count += 1

print(f'A: {A_count} B: {B_count} C: {C_count} D: {D_count} E: {E_count} F: {F_count} G: {G_count} H: {H_count} I: {I_count} J: {J_count} K: {K_count} L: {L_count} M: {M_count} N: {N_count} O: {O_count} P: {P_count} Q: {Q_count} R: {R_count} S: {S_count} T: {T_count} U: {U_count} V: {V_count} W: {W_count} X: {X_count} Y: {Y_count} Z: {Z_count}')