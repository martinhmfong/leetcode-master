def timeConversion(s):
    # Write your code here
    t, am_pm = s[:8], s[8:]
    if am_pm == 'AM':
        print(t)
    else:
        h, m, s = t.split(':')
        h = str(int(h) + 12)
        print(':'.join([h, m, s]))


def pangrams(s):
    # Write your code here
    count = {}
    for char in s.lower():
        print(count)
        if not char:
            continue
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return len(count.keys()) == 26


if __name__ == '__main__':
    pangrams('We promptly judged antique ivory buckles for the prize')
