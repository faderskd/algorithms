def make_largest_palindrome(input_string, k):
    string = input_string[:]
    string = list(map(int, string))
    i = 0
    j = len(string) - 1
    while i < j:
        if string[i] != string[j]:
            if k <= 0:
                return "Not possible"
            if string[i] > string[j]:
                string[j] = string[i]
            else:
                string[i] = string[j]
            k -= 1
        i += 1
        j -= 1

    i = 0
    j = len(string) - 1
    while i < j and k > 0:
        if string[i] != 9:
            if input_string[i] != input_string[j]:
                k -= 1
                string[i] = string[j] = 9
            elif k > 1:
                k -= 2
                string[i] = string[j] = 9
        i += 1
        j -= 1

    if k > 0 and len(string) % 2 != 0:
        string[len(string) // 2] = 9
    return "".join(list(map(str, string)))


def rearange_same_chars(string):
    if not string:
        return ""
    new_string = string[0]
    indexes = [False] * len(string)
    indexes[0] = True

    c = 1
    while c < len(string):
        i = 0
        while i < len(string):
            if new_string[c - 1] != string[i] and not indexes[i]:
                new_string = new_string + string[i]
                indexes[i] = True
                c += 1
                break
            i += 1
        else:
            return "Not possible"
    return new_string


def replace_in_place(string):
    i = j = 0
    string = list(string)
    while j < len(string) - 1:
        if string[j] == 'A' and string[j + 1] == 'B':
            string[i] = 'C'
            j += 2
        else:
            string[i] = string[j]
            j += 1
        i += 1

    if j == len(string) - 1:
        string[i] = string[j]
        i += 1
    return "".join(string[:i])


def reverse(string):
    s = list(string)
    i = 0
    j = len(string) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return "".join(s)


def remove_duplicates(string):
    unique_index = 0
    s = list(string)
    chars = [False] * 256
    for i in range(len(string)):
        if not chars[ord(string[i])]:
            s[unique_index] = string[i]
            unique_index += 1
            chars[ord(string[i])] = True
    return "".join(s[:unique_index])


def strings_are_anagrams(string1, string2):
    chars = [0] * 256
    if len(string1) != len(string2):
        return False

    for i in range(len(string1)):
        chars[ord(string1[i])] += 1
    for i in range(len(string2)):
        chars[ord(string2[i])] -= 1
    return all([True if not chars[i] else False for i in range(256)])

print(strings_are_anagrams('abcd', 'bcad'))