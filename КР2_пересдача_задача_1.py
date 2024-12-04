def long(s: str) -> int:
    if not s:
        return 0

    dp = [1] * len(s)

    for i in range(1, len(s)):
        for j in range(i):
            if s[i] > s[j]: 
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


input_string = "abacbad"
print("Длина наибольшей возрастающей подпоследовательности:", long(input_string))
