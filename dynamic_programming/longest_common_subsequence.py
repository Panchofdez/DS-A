#dynamic programming algorithm to find the longest_common_subsequence

def longest_common_subsequence(word1, word2):
    m = len(word1)
    n = len(word2)
    K= [[0 for x in range(n + 1)] for y in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            
            if i == 0  or j == 0:
                K[i][j] = 0

            elif word1[i-1] == word2[j-1]:
                K[i][j] = K[i-1][j-1] + 1

            else:
                K[i][j] =  max(K[i-1][j], K[i][j-1])         
    return K[m][n]


w1 = "AGGTAB"
w2 = "GXTXAYH"
print(longest_common_subsequence(w1, w2))