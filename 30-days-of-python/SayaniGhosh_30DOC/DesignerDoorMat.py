n, m = map(int, input().split())
pat = [(".|." * (2 * i + 1)).center(m, "-") for i in range(n // 2)]
print("\n".join(pat + ["WELCOME".center(m, "-")] + pat[::-1]))