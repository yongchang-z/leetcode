"""
This function finds the longest common prefix string amongst an array of 
strings. If there is no common prefix, it returns an empty string."""

# Intuitive solution
def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    for i, char in enumerate(strs[0]):
        for string in strs[1:]:
            if i >= len(string) or string[i] != char:
                return strs[0][:i]
    
    return strs[0]

# Optimized solution
def longestCommonPrefixOptimized(strs):
    if not strs:
        return ""
    
    shortest, longest = min(strs), max(strs)

    for i in range(len(shortest)):
        if shortest[i] != longest[i]:
            return shortest[:i]
    
    return shortest
    


