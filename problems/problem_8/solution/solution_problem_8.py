def encode_this_string(s):
    ans = []
    prev = None
    count = 0
    for i in range(len(s)):
        n = s[i]
        if n == prev:
            count += 1
        else:
            if prev:
                ans.append((count, prev))
            count = 1
        prev = n
    ans.append((count, prev))

    return ''.join(f"{x[0]}{x[1]}" for x in ans)
