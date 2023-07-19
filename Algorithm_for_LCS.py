def LCS(A, B):
    n = length(A)
    m = length(B)
    
    # Create a 2D array to store the lengths of LCS
    LCS = newArray(n+1, m+1)
    
    # Initialize the first row and column of the LCS array to 0
    for i in range (0,n):
        LCS[i][0] = 0
    for j in range (0 ,m):
        LCS[0][j] = 0
    
    # Compute the lengths of LCS for all subproblems
    for i in range (1,n):
        for j in range (1,m):
            if A[i-1] == B[j-1]:
                LCS[i][j] = LCS[i-1][j-1] + 1
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
    
    #Retrieve the longest common subsequence by backtracking
    lcs = newArray()
    i = n
    j = m
    while i > 0 and j > 0:
        if A[i-1] == B[j-1]:
            lcs.prepend(A[i-1])
            i = i - 1
            j = j - 1
        elif LCS[i-1][j] > LCS[i][j-1]:
            i = i - 1
        else:
            j = j - 1
    return lcs
print(len(A
