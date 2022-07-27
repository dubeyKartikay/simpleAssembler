class SIM:
    def __init__(self,reg_in,mem,arr=[]):
        self.arr=arr
        self.n=len(arr)
        self.halted=0
        self.reg_in=reg_in
        self.mem = mem
    def decodeNum(self,formatted_num):
        n = len(formatted_num)
        s = 0
        formatted_num = formatted_num[::-1]
        for i in range(n):

            s += (int(formatted_num[i])*(2**i))
        return s
    def bin2dec(self,formatted_num):
        n = len(formatted_num)
        s = 0
        formatted_num = formatted_num[::-1]
        for i in range(n):

            s += (int(formatted_num[i])*(2**i))
        return s
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
        if(self.arr[0]=='add'):
            a=self.arr[1]
            b=self.arr[2]
            c=""
            c=self.dectobin(a+b)
            self.reg_in[self.arr[3]]=c    
            PC+=1
            
        elif(self.arr[0]=='sub'):
            a=self.arr[1]
            b=self.arr[2]
            c=""
            c=self.dectobin(a-b)
            self.reg_in[self.arr[3]]=c 
            PC+=1
        elif(self.arr[0]=='mov'):                 
            if(type(self.arr[2]==int)):
                b=""
                b=self.dectobin(self.arr[2])
                self.reg_in[self.arr[1]]=b
                PC+=1
            elif(type(self.arr[2]!=int)):
                b=self.arr[1]
                c=""
                c=self.dectobin(b)
                self.reg_in[self.arr[1]]=c   
                PC+=1 
        elif(self.arr[0]=='ld'):                 #mem adress data do in binary
            self.reg_in[self.arr[1]] = self.mem[self.bin2dec(self.arr[2])]
            PC+=1
        elif(self.arr[0]=='st'):
            self.mem[self.bin2dec(self.arr[2])]= self.reg_in[self.arr[1]]
            PC+=1
            
        elif(self.arr[0]=='mul'):
            a=self.arr[1]
            b=self.arr[2]
            c=""
            c=self.dectobin(a*b)
            self.reg_in[self.arr[3]]=c
            PC+=1
        elif(self.arr[0]=='div'):
            a=self.arr[1]
            b=self.arr[2]
            c=""
            d=""
            c=self.dectobin(a/b)
            d=self.dectobin(a%b)
            self.reg_in['000']=c
            self.reg_in['001']=d
            PC+=1
        elif(self.arr[0]=='rs'):         #imm in dec
            a=""
            a=self.reg_in[self.arr[1]]
            a=self.decodeNum(a)         
            b=self.arr[2]
            a=a>>b
            a=self.dectobin(a)
            self.reg_in[self.arr[1]]=a
            PC+=1
        elif(self.arr[0]=='ls'):          #imm in dec
            a=""
            a=self.reg_in[self.arr[1]]
            a=self.decodeNum(a)         
            b=self.arr[2]
            a=a<<b
            a=self.dectobin(a)
            self.reg_in[self.arr[1]]=a
            PC+=1
        elif(self.arr[0]=='xor'):
            a=self.arr[1]
            b=self.arr[2]
            c=""
            c=self.dectobin(a^b)
            self.reg_in[self.arr[3]]=c 
            PC+=1
        elif(self.arr[0]=='or'):
            a=self.arr[1]
            b=self.arr[2]
            c=""
            c=self.dectobin(a|b)
            self.reg_in[self.arr[3]]=c 
            PC+=1
        elif(self.arr[0]=='and'):
            a=self.arr[1]
            b=self.arr[2]
            c=""
            c=self.dectobin(a&b)
            self.reg_in[self.arr[3]]=c 
            PC+=1  
        elif(self.arr[0]=='not'):
            a=self.arr[1]
            c=""
            c=self.dectobin(~a)
            self.reg_in[self.arr[2]]=c
            PC+=1
        elif(self.arr[0]=='cmp'):
            a=self.arr[1]
            b=self.arr[2]
            flags = self.reg_in['111'].split("")
            if(a>b):
                flags[-3] = "0"
                flags[-2] = "1"
                flags[-1] = "0"
                PC+=1
            elif(a<b):
                flags[-3] = "1"
                flags[-2] = "0"
                flags[-1] = "0"
                PC+=1           
            elif(a==b):
                flags[-3] = "0"
                flags[-2] = "0"
                flags[-1] = "1"
                PC+=1
        elif(self.arr[0]=='jmp'):
            pcnew=int(self.arr[1])
            PC=pcnew
        elif(self.arr[0]=='jlt'):
            pcnew=int(self.arr[1])
            if(self.reg_in['111'][13]==1):
                PC=pcnew
            else:
                PC=PC+1
        elif(self.arr[0]=='jgt'):
            pcnew=int(self.arr[1])
            if(self.reg_in['111'][-2]=='1'):
                PC=pcnew
            else:
                PC=PC+1
        elif(self.arr[0]=='je'):
            pcnew=int(self.arr[1])
            if(self.reg_in['111'][-1]=='1'):
                PC=pcnew
            else:
                PC=PC+1            
        elif(self.arr[0]=='hlt'):
            self.halted=1       
        return PC                   