Question: Find the longest common prefix among an array of strings.

def longest_common_prefix(strings):
    if not strings:
        return ""
    
    prefix = strings[0]
    
    for string in strings[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
