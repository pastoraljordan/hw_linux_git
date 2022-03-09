def sort_list(a_list):
    n = len(a_list)
    i = 0
    while i < n:
        j = 0
        while j < (n-i-1):
            if a_list[j] > a_list[j + 1]:
                temp = a_list[j]
                a_list[j] = a_list[j + 1]
                a_list[j + 1] = temp
            j += 1
        i += 1
    return a_list
