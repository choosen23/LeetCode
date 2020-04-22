class Solution:

    def numTeams(self, rating: List[int]) -> int:
        def Reverse(lst):
            new_lst = lst[::-1]
            return new_lst

        def numOfIncSubseqOfSizeK(arr, n, k):
            import math as mt
            dp = [[0 for i in range(n)]
                  for i in range(k)]

            # count of increasing subsequences
            # of size 1 ending at each arr[i]
            for i in range(n):
                dp[0][i] = 1

            # building up the matrix dp[][]
            # Here 'l' signifies the size of
            # increassing subsequence of size (l+1).
            for l in range(1, k):

                # for each increasing subsequence of
                # size 'l' ending with element arr[i]
                for i in range(l, n):

                    # count of increasing subsequences of
                    # size 'l' ending with element arr[i]
                    dp[l][i] = 0
                    for j in range(l - 1, i):
                        if (arr):
                            if (arr[j] < arr[i]):
                                dp[l][i] += dp[l - 1][j]

            # Sum up the count of increasing subsequences
            # of size 'k' ending at each element arr[i]
            Sum = 0
            for i in range(k - 1, n):
                Sum += dp[k - 1][i]

            # required number of increasing
            # subsequences of size k
            return Sum

        sum1 = numOfIncSubseqOfSizeK(rating, len(rating), 3)
        sum2 = numOfIncSubseqOfSizeK(Reverse(rating), len(rating), 3)

        return sum1 + sum2
