import numpy as np


def make_Upper(matrix, m_Size):
    for i in range(m_Size-1):
        for j in range(m_Size-1-i):
            # adding a multiple of one equation to another
            if matrix[i][i] != 0:
                temp = matrix[j+1+i][i]/matrix[i][i]
                temp = -1 * temp
                for k in range(m_Size):
                    matrix[j+1+i][k] = matrix[j+1+i][k] + temp*matrix[i][k]

        # Interchanging any two equations
        for m in range(m_Size):
            for n in range(m_Size - 1):
                if matrix[n][m] == 0:
                    if matrix[n + 1][m] != 0:
                        for p in range(m_Size - m):
                            temp_ = matrix[n][m + p]
                            matrix[n][m + p] = matrix[n + 1][m + p]
                            matrix[n + 1][m + p] = temp_

    print(matrix)



if __name__ == "__main__":
    m_Size = input("n x n square matrix에서 n을 입력하세요 : ")
    print("--------------------------------------------")

    m_Size = int(m_Size)
    matrix = np.zeros((m_Size, m_Size), dtype=int)

    for i in range(m_Size):
        print(str(i+1) + "번째 열의 원소를 공백으로 구분해서 입력하세요")
        row = list(map(int, input("> ").split()))

        matrix[i] = row

    print("--------------------------------------------")
    print("입력으로 받은 matrix : ")
    print(matrix)

    print("--------------------------------------------")
    print("row operation 결과 : ")
    make_Upper(matrix, m_Size)
