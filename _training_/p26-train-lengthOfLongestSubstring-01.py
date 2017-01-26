def lengthOfLongestSubstring(s='abcabcb'):

    """
    http://articles.leetcode.com/longest-substring-without-repeating-characters/
    """

    n = len(s)
    i, j = 0, 0
    maxLen = 0
    exist = []
    status = ''  # debugging-info

    while j < n:
        status = s[j]  # debugging-info
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

print(lengthOfLongestSubstring('abcabcjg'))



def train_it(s='abcabcd'):

   n = len(s)
   i, j = 0, 0
   maxLen = 0
   exist = []

   while j < n:
       if s[j] in exist:
           maxLen = max(maxLen, j - i)
           while s[i] != s[j]:
               i += 1
           i += 1
           j += 1
       else:
           exist.append(s[j])
           j += 1
   return maxLen

#print(train_it())
