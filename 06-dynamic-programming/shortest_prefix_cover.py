
string = list(map(int, input().split()))
text = ''.join(str(num) for num in string)
n = len(text)

# For each possible prefix length k
for k in range(1, n + 1):
    prefix = text[:k]
    
    # dp[i] = whether position i is covered (0-indexed, position means covered up to i-1)
    dp = [False] * (n + 1)
    dp[0] = True  # Start is covered
    
    for i in range(n + 1):
        if dp[i]:
            # We can try to place the prefix starting at position i
            if i + k <= n and text[i:i+k] == prefix:
                # This covers up to i+k
                for j in range(i + 1, i + k + 1):
                    if j <= n:
                        dp[j] = True
    
    if dp[n]:
        print(k)
        break
else:
    print(n)