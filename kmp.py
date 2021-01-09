def kmp(text: str, pattern: str) -> int:
    next = gen_next(pattern)
    # next[0] = 0
    it = ip = 0
    while it < len(text):
        if ip == len(pattern):
            return it - len(pattern), it
        if text[it] == pattern[ip]:
            it += 1
            ip += 1
        else:
            ip = next[ip]
       
    return -1


def gen_next(pattern: str) -> list:
    next = [0]
    j = 0
    for i in range(1, len(pattern)):
        next.append(j)
        j = j + 1 if pattern[i] == pattern[j] else 0
    return next


if __name__ == '__main__':
    text = 'ababababcabaab'
    pattern = 'ababcabaa'
    # pattern= 'agctagcagctagct'
    print(gen_next(pattern))
    print(kmp(text, pattern))
