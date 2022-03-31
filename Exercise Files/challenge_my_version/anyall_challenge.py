import string

def contains_punctuation(input_str):
    ''' Return True if the input_str contains punctuations.
    Return False otherwise '''
    
    return any(
        a_char is string.punctuation
        for a_char in input_str
    )
