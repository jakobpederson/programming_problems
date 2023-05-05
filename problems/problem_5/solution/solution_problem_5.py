def simplifyPath(path):
    ans = []

    for i in path.split('/'):
        match i:
            case '' | '.':
                continue
            case '..':
                ans = ans[:-1]
                continue
            case _:
                ans.append(i)
    return "/" + "/".join(ans)


def largest_difference(lst):
    p1 = 0
    p2 = len(lst) - 1
    diff = 0

    for i in range(len(lst)):
        x = max(lst[p1], lst[p2])
        y = min(lst[p1], lst[p2])
        diff = max(diff, x - y)
        if x > y:
            p2 -= 1
        else:
            p1 += 1

    return diff


def is_palindrome(value: str):
    return value == ''.join(reversed(list(value)))
