class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == j or (j == len(mat)-1-i):
                    # print(mat[i][j])
                    s = mat[i][j]+s
        return s

