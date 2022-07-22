class SIM:
    def __init__(self,arr,dict):
        self.arr=arr
        self.n=len(arr)
        self.dict=dict
    def bintodec(self,bin):
        n=len(bin)
        sum=0
        bin=bin[::-1]
        for i in range(n):
            bin[i]=int(bin[i])
            sum=sum+(bin[i]*(2^n))
        return sum
    def dectobin(self,dec):
        j=""
        while dec>0:
            k=dec%2
            dec=dec//2
            k=str(k)
            j=j+k
        j=j[::-1]
        j=str(j)
        result=""
        result+="0"*(16-len(j))
        result+=j
        return result    
    def execute(self):
        if(arr[0]=='add'):
            a=self.bintodec(arr[1])
            b=self.bintodec(arr[2])
            c=""
            c=dectobin(a+b)
            self.dict[arr[3]]=c    
        
            
                        