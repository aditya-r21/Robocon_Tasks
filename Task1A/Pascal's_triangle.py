class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[[1]]
        for i in range(1,numRows):
            a=[1]
            for j in range(1,i):
                a.append(l[i-1][j-1]+l[i-1][j])
            a.append(1)
            l.append(a)
        return l
