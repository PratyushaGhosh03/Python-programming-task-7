def generate_parentheses(n):
    result = []
    
    def backtrack(s, open_count, close_count):
        if len(s) == 2 * n:
            result.append(s)
            return
        
        if open_count < n:
            backtrack(s + "(", open_count + 1, close_count)
        if close_count < open_count:
            backtrack(s + ")", open_count, close_count + 1)
    
    backtrack("", 0, 0)
    return result

# Example usage
n = 3
print(generate_parentheses(n))
