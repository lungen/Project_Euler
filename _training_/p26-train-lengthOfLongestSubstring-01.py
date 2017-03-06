def lengthOfLongestSubstring(s='abcabcb'):

    """
    http://articles.leetcode.com/longest-substring-without-repeating-characters/
    """

    n = len(s)
    i, j = 0, 0
    maxLen = 0
    exist = []

    while j < n:
        if s[j] in exist:
            maxLen = max(maxLen, j-i)
            while s[i] != s[j]:
                i += 1
            i += 1
            j += 1
        else:
            exist.append(s[j])
            j += 1

    maxLen = max(maxLen, n - i)
    return maxLen

#print(lengthOfLongestSubstring('abcabcjg'))

