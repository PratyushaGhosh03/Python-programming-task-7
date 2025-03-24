def is_palindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

def partition_palindromes(s):
    result = []
    
    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        
        for end in range(start, len(s)):
            if is_palindrome(s, start, end):
                backtrack(end + 1, path + [s[start:end + 1]])
    
    backtrack(0, [])
    return result

# Example usage
s = "aab"
print(partition_palindromes(s))
