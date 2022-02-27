import numpy as np
import copy

A = np.zeros((4,4), dtype=float)
A[0] = [1, 2, 4, 7]
A[1] = [0, 3, 5, 8]
A[2] = [0, 0, 6, 9]
A[3] = [0, 0, 0, 10]

l1 = 1
l2 = 3
l3 = 6
l4 = 10


def solve_eigenvector(A_, l_):
    # A - L(람다)I
    for i in range(4):
        A_[i][i] = A_[i][i] - l_

    # x, y, z, r중 0인 원소를 찾아서 행렬에 계산
    if A_[3][3] != 0:
        for i in range(4):
            A_[i][3] = 0

    if A_[2][2] != 0 and A_[2][3] == 0:
        for i in range(4):
            A_[i][2] = 0

    if A_[1][1] != 0 and A_[1][2] == 0 and A_[1][3] == 0:
        for i in range(4):
            A_[i][1] = 0

    temp = 0
    c = 0
    for i in range(4):
        count = 0
        for j in range(4):
            if A_[i][j] != 0:
                count = count + 1
        if count == 2:
            c = i
            break

    # eigenvector를 구하기 위한 과정
    for k in range(c+1):
        for i in range(4):
            count = 0
            for j in range(4):
                if A_[i][j] != 0.:
                    count = count + 1

            if count == 2:
                temp = i
                break

        for i in range(4):
            if A_[temp][i] != 0:
                a = abs(A_[temp][i+1] / A_[temp][i])
                A_[temp][i] = a
                A_[temp][i+1] = 0
                for z in range(temp):
                    A_[temp-1-z][i] = A_[temp-1-z][i]*a + A_[temp-1-z][i+1]
                    A_[temp-1-z][i+1] = 0
                break

    # eigenvector 구하기
    v = np.zeros((4, 1), dtype=float)
    for i in range(4):
        c_ = 0
        for j in range(4):
            if A_[i][j] == 0:
                c_ = c_ + 1
            else:
                v[i][0] = A_[i][j]

        if c_ == 4:
            v[i][0] = 1
            break

    return v


def solve_cof(V, x):

    V[3][3] = x[3][0]

    for i in range(3):
        V[i][3] = V[i][3]*V[3][3]

    V[2][2] = x[2][0] - V[2][3]
    V[2][3] = 0

    for i in range(2):
        V[i][2] = V[i][2]*V[2][2]

    V[1][1] = x[1][0] - V[1][2] - V[1][3]
    V[1][2] = 0
    V[1][3] = 0

    V[0][1] = V[0][1] * V[1][1]

    V[0][0] = x[0][0] - V[0][1] - V[0][2] - V[0][3]
    V[0][1] = 0
    V[0][2] = 0
    V[0][3] = 0

    c1 = V[0][0]
    c2 = V[1][1]
    c3 = V[2][2]
    c4 = V[3][3]
    return c1, c2, c3, c4

if __name__ == '__main__':
    # eigenvector 구하기
    v1 = solve_eigenvector(copy.deepcopy(A), l1)
    v2 = solve_eigenvector(copy.deepcopy(A), l2)
    v3 = solve_eigenvector(copy.deepcopy(A), l3)
    v4 = solve_eigenvector(copy.deepcopy(A), l4)

    # x 입력받기
    x = np.zeros((4, 1), dtype=float)
    for i in range(4):
        print("x의 " + str(i+1) + "번째 원소를입력하세요")
        a = input(">")
        x[i][0] = a
    # k 입력받기
    print("k를 입력하세요")
    k = input(">")

    # c를 구하기 위해 eigenvector를 합치기
    V = np.zeros((4, 4), dtype=float)
    for i in range(4):
        V[i][0] = v1[i][0]
    for i in range(4):
        V[i][1] = v2[i][0]
    for i in range(4):
        V[i][2] = v3[i][0]
    for i in range(4):
        V[i][3] = v4[i][0]
    # c 구하기
    c1, c2, c3, c4 = solve_cof(copy.deepcopy(V), copy.deepcopy(x))

    # eigenvalue에 k제곱해주기
    l1k = l1 ** int(k)
    l2k = l2 ** int(k)
    l3k = l3 ** int(k)
    l4k = l4 ** int(k)

    # A^kx계산하기
    Answer = np.zeros((4, 1), dtype=float)
    for i in range(4):
        Answer[i][0] = c1*l1k*v1[i][0] + c2*l2k*v2[i][0] + c3*l3k*v3[i][0] + c4*l4k*v4[i][0]

    print(Answer)





