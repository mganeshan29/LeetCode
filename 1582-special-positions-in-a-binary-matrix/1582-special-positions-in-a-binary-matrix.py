class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        for r in mat:

            #If sum of the row is 1, then only a single 1 is in the row.
            if sum(r) == 1:
                c = r.index(1)
                summ = 0

                #If sum of that column is 1, then only a single 1 is in that column
                for rw in range(len(mat)):
                    summ += mat[rw][c]

                if summ == 1:
                    ans += 1

        return ans
