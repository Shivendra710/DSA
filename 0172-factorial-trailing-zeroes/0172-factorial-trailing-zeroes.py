class Solution:
    def trailingZeroes(self, n: int) -> int:
        count=0
        def Fac(y):
            if y==0 or y==1:
                return 1
            else:
                return y*Fac(y-1)
        # Trails =1
        # for i in range(n,1,-1):
        #     Trails *=i

         # main code       
        Trails=Fac(n)
        while (Trails >0):
            tempVal = Trails % 10
            if tempVal == 0:
                count +=1
            else:
                break
            Trails = Trails//10
        
        return count



            
         
        

        