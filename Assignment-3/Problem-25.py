def is_pal(num):
    return str(num) == str(num)[::-1]

def all_palindrome(arr):
    for x in arr:
        if not is_pal(x):
            return False
    return True

print(all_palindrome([111,222,333,444,555]))  
print(all_palindrome([121,131,20]))          