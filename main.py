#### Fonction secondaire
"""g"""


def ispalindrome(s):
    """fonction qui test si un mot est un palindrome"""
    if s!=s[::-1]:
        return False
    return True


def main():
    """appel de la fonction"""
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
