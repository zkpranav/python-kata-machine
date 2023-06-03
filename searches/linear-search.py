def linearSearch(haystack, needle):
    status = False

    for i in range(0, len(haystack)):
        if (haystack[i] == needle):
            status = True

    return status
