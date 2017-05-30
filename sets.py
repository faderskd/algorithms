def arrays_insersection(li1, li2):
    i = j = 0
    intersection = []
    while i < len(li1) and j < len(li2):
        if li1[i] < li2[j]:
            i += 1
        elif li1[i] > li2[j]:
            j += 1
        else:
            intersection.append(li1[i])
            i += 1
            j += 1
    return intersection


def three_arrays_intersection(li1, li2, li3):
    i = j = k = 0
    intersection = []
    while i < len(li1) and j < len(li2) and k < len(li3):
        if li1[i] == li2[j] == li3[k]:
            intersection.append(li1[i])
            i += 1
            j += 1
            k += 1
        elif li1[i] < li2[j]:
            i += 1
        elif li2[j] < li3[k]:
            j += 1
        else:
            k += 1
    return intersection

print(three_arrays_intersection([1,3,5,7,8], [2, 3, 4, 7, 8], [1, 3, 7, 8, 9, 11]))