import math

def calculate_entropy(password: str) -> float:
    """
    calculate the entropy of a password based on its length and character set.
    entropy is measured in bits and it represents password unpredictability.
    """
    if not password:
        return 0.0
    
    charset_size = 0
    #checks which character groups are present
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(not c.isalnum() for c in password):
        charset_size += 32 # aproxomate number of common symbols
    
    # entropy formula: length * log2(character set size)
    entropy = len(password) * math.log2(charset_size)
    return entropy