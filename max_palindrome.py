def max_palindrome_substring(li):
    max_length = 1
    max_l = max_r = li[0]

    for i in range(1, len(li)):
        l = i - 1
        r = i + 1
        tmp_length = 1

        while l >= 0 and li[l] == li[i]:
            l -= 1
            tmp_length += 1

        while r < len(li) and li[r] == li[i]:
            r += 1
            tmp_length += 1

        while l >= 0 and r < len(li) and li[l] == li[r]:
            l -= 1
            r += 1
            tmp_length += 2

        if tmp_length > max_length:
            max_length = tmp_length
            max_l = l + 1
            max_r = r - 1

    return li[max_l: max_r + 1]