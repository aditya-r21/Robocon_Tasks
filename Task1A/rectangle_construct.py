class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l1=[]
        for i in range(1,area+1):
            if area%i==0:
                l1.append(i)
        l2=[]
        if len(l1)%2==0:
            L=l1[int(len(l1)/2)]
            W=l1[int((len(l1)/2)-1)]
            l2.append(L)
            l2.append(W)
        else:
            L=l1[int(len(l1)/2)]
            l2.append(L)
            l2.append(L)
        return l2      
