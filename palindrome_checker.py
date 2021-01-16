def is_palindrome(input_string):
    """Check if a string is a palindrome
    irrespective of capitalisation
    Returns:
        True if string is a palindrome
        e.g
        >>> is_palindrome("kayak")
        OUTPUT : True
        False if string is not a palindrome
        e.g 
        >>> is_palindrome("Boat")
        OUTPUT : False
    """
    
    # Create variables to hold new strings to be compared
    new_string = ""
    reversed_string = ""
    
    # Ensure that the string is not empty
    if input_string != '':
        # Change input into lower case and loop through each letter
        for char in input_string.lower():
            # Remove all white spaces 
            # Add each letter to a string
            # Reverse the string
            if char  != " ":
                new_string += char
                reversed_string = ''.join(reversed(new_string))
                
        # Compare the strings
        
        if new_string == reversed_string:
            return True
        return False
    return "String is empty"
   
    
# Tests
print(is_palindrome("kayak")) # Return True
print(is_palindrome("Hold Your fire")) # Return False
print(is_palindrome("Never Odd or Even")) # Return True
print(is_palindrome("abc")) # Return False
print(is_palindrome("")) # Return "String is empty"