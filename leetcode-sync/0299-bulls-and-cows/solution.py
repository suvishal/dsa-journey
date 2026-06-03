class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        i = 0 
        secret_left = []
        guess_left = []

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_left.append(secret[i])
                guess_left.append(guess[i])

        for digit in guess_left:
            if digit in secret_left:
                cows += 1
                secret_left.remove(digit)


        return str(bulls) + 'A' + str(cows) + 'B'



