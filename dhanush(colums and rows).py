def ismatch(s:str,p:str)->bool:
            rows,columns=(len(s),len(p))
            if rows ==0 and columns==0:
                return true
if columns==0:
            return false
        dp=[[false for]in range(columns+1)]
        for i in range(rows+1)
        dp[0][0]=true
        for i in  range (2,columns+1):
            if p[i-1]=='*'
            dp[0][1]=dp[0][i-2]

            for i in range(1,rows+1):
                for j in range (1,columns+1):
                    if s[i-1]==p[j-1] or p[i-1]=='.':
                        dp[i][j]=dp[i-1][j-1]
                    elif j and p[i-1]=='*':
                        dp[i][j]=dp[i][j-2]
                        if p[j-2]=='.' or p[j-2]==s[i-1]:
                            dp[i][j]=dp[i][j] or dp[i-1][j]
    return dp[rows][columns]

print(ismatch("a","aa"))
