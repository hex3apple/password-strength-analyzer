from src.entropy import calculate_entropy
from src.analyzer import rate_password
from src.breach_check import check_breach

def main():
    print("=== Password Strength Analyzer ===")
    password = input("Enter a password to analyze: ")

    # Entropy + rating
    analysis = rate_password(password)

    #Breach count
    breaches= check_breach(password)

    print("\n--- Results ---")
    print(f"Password: {analysis['password']}")
    print(f"Entropy: {analysis['entropy']} bits")
    print(f"Strength Rating: {analysis['rating']}")
    print(f"Breach Count: {breaches}")
          
if __name__ == "__main__":
    main()