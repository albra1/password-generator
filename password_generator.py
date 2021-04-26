import secrets
import string

class Password_Generator:

    # generates a cryptograpic secure random string of a given lenght
    def generate_password(self, length, chars):
        
        return "".join(secrets.choice(chars) for _ in range(length))


    # calculates the entropy bits for a password
    # entropy values form Wikipedia: https://en.wikipedia.org/wiki/Password_strength#Entropy_as_a_measure_of_password_strength
    def calc_entropy(self, word):

        nums = set(string.digits)
        lower = set(string.ascii_lowercase)
        upper = set(string.ascii_uppercase)
        special = set(string.punctuation)

        # numeric only
        if(word.isnumeric()):
            return len(word) * 3.322 

        # ASCII printable (alphanumeric case sensitive plus special chars)
        elif(any(char in lower for char in word) & any(char in upper for char in word) & any(char in nums for char in word) & any(char in special for char in word)):
            return len(word) * 6.555

        # Case sensitive alphanumeric 
        elif(any(char in lower for char in word) & any(char in upper for char in word) & any(char in nums for char in word)):
            return len(word) * 5.954


        # Case insensitive alphanumeric
        elif((any(char in lower for char in word) ^ any(char in upper for char in word)) & any(char in nums for char in word)):
            return len(word) * 5.17


        # Case sensitive Latin alphabet
        elif(any(char in lower for char in word) & any(char in upper for char in word)):
            return len(word) * 5.7

        # Case insensitive Latin alphabet 
        else:
            return len(word) * 4.7