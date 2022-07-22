class SIM:
    def __init__(self,arr,dict):
        self.arr=arr
        self.n=len(arr)
        self.dict=dict
        self.halted=0
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
    def execute(self,PC):
        if(arr[0]=='add'):
            a=self.bintodec(arr[1])
            b=self.bintodec(arr[2])
            c=""
            c=dectobin(a+b)
            self.dict[arr[3]]=c    
            PC+=1
        elif(arr[0]=='sub'):
            a=self.bintodec(arr[1])
            b=self.bintodec(arr[2])
            c=""
            c=dectobin(a-b)
            self.dict[arr[3]]=c 
            PC+=1
        elif(arr[0]=='mov'):                  #imm value int me dio naki string!!!
            if(type(arr[2]==int)):
                b=""
                b=self.dectobin(arr[2])
                self.dict[arr[2]]=b
                PC+=1
        elif(arr[0]=='mov'):
            if(type(arr[2]!=int)):
                b=self.bintodec(arr[1])
                c=""
                c=self.dectobin(b)
                self.dict[arr[2]]=c   
                PC+=1 
        # elif(arr[0]=='ld'):
        # elif(arr[0]=='st'):
        elif(arr[0]=='mul'):
            a=self.bintodec(arr[1])
            b=self.bintodec(arr[2])
            c=""
            c=dectobin(a*b)
            self.dict[arr[3]]=c
            PC+=1
        elif(arr[0]=='div'):
            a=self.bintodec(arr[1])
            b=self.bintodec(arr[2])
            c=""
            d=""
            c=dectobin(a/b)
            d=dectobin(a%b)
            self.dict['000']=c
            self.dict['001']=d
            PC+=1
        # elif(arr[0]=='rs'):
        # elif(arr[0]=='ls'):
        elif(arr[0]=='xor'):
            a=self.bintodec(arr[1])
            b=self.bintodec(arr[2])
            c=""
            c=dectobin(a^b)
            self.dict[arr[3]]=c 
            PC+=1
        elif(arr[0]=='or'):
            a=self.bintodec(arr[1])
            b=self.bintodec(arr[2])
            c=""
            c=dectobin(a|b)
            self.dict[arr[3]]=c 
            PC+=1
        elif(arr[0]=='and'):
            a=self.bintodec(arr[1])
            b=self.bintodec(arr[2])
            c=""
            c=dectobin(a&b)
            self.dict[arr[3]]=c 
            PC+=1  
        elif(arr[0]=='not'):
            a=self.bintodec(arr[1])
            c=""
            c=dectobin(~a)
            self.dict[arr[3]]=c
            PC+=1
        elif(arr[0]=='cmp'):
            a=self.bintodec(arr[1])
            b=self.bintodec(arr[2])
            if(a>b):
                self.dict['111'][14]='1'
                PC+=1
            elif(a<b):
                self.dict['111'][13]='1' 
                PC+=1           
            elif(a==b):
                self.dict['111'][15]='1'
                PC+=1
        elif(arr[0]=='jmp'):
            pcnew=int(arr[1])
            PC=pcnew
        elif(arr[0]=='jlt'):
            pcnew=int(arr[1])
            if(self.dict['111'][13]==1):
                PC=pcnew
            else:
                PC=PC+1
        elif(arr[0]=='jgt'):
            pcnew=int(arr[1])
            if(self.dict['111'][14]==1):
                PC=pcnew
            else:
                PC=PC+1
        elif(arr[0]=='je'):
            pcnew=int(arr[1])
            if(self.dict['111'][15]==1):
                PC=pcnew
            else:
                PC=PC+1            
        elif(arr[0]=='hlt'):
            self.halted=1                          