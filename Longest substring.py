def longest_unique_substring(s):
    char_map = {}
    left = max_length = 0

    for right, char in enumerate(s):
        if char in char_map:
            left = max(left, char_map[char] + 1)
        char_map[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage
print(longest_unique_substring("abcabcbb"))
