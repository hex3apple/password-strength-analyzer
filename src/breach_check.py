import hashlib
import requests

def check_breach(password: str) -> int:
    """
    Check if a password has appeared in known data breaches using
    the HaveIBeenPwned k-anonymity API.
    
    Returns the number of times the password appears in breaches.
    """
    # hash the password using SHA-1
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()

    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    # query the HIBP API
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError("error fetching data from HIBP API")
    
    # check if the suffix appears in the returned list
    hashes = (line.split(":") for line in response.text.splitlines())

    for hash_suffix, count in hashes:
        if hash_suffix == suffix:
            return int(count)
    return 0 #not found in any breach