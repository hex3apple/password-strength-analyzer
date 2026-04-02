from src.entropy import calculate_entropy
#this grabs the function 'calculate_entropy' from the file 'entropy' for use in this program

def rate_password(password: str) -> dict:
    """
        Analyze a password and return its entropy and a strength rating.
        Returns a dictionary so it can be used easily in a CLI or web app.
    """
    entropy = calculate_entropy(password)
    # the numbers 28, 36, 60, and 128 are chosen based on the NIST guidelines
    if entropy < 28:
        rating = "very weak"
    elif entropy < 36:
        rating = "weak"
    elif entropy < 60:
        rating = "moderate"
    elif entropy < 128:
        rating = "strong"
    else:
        rating = "very strong"
    
    return {
        "password": password,
        "entropy": round(entropy, 2),
        "rating": rating
    }