class solution:
    def letterscombinations(self,digits):
        if(len(digits)==0):
            return [ ]
        digit2char={'1':" ",  '2':"ABC",  '3':"DEF",   '4':"GHI",   '5':"JKL",  '6':"MNO",'7':"PQRS",'8':"TUV",'9':"WXYZ",'0':" "}
        result=[' ']
        for d in digits:
            tem= [ ]
            for c in digit2char[d]:
                tem=tem+[r+c for r in result]
                result=tem
            return result
            
ob=solution( )
print(ob.letterscombinations('23'))
