import random

# Frequency distribution of letters of alphabet
LETTER_FULL_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

# This string reflects the frequency distribution of the various letters for selection probability
LETTER_FREQ_POOL = "AAAAAAAAABBCCDDDDEEEEEEEEEEEEFFGGGHHIIIIIIIIIJKLLLLMMNNNNNNOOOOOOOOPPQRRRRRRSSSSTTTTTTUUUUVVWWXYYZ"

# Points for each letter
LETTER_POINTS = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}


def draw_letters():     
    letters_drawn =[]
    letter_freq = {}
    i = 0
    for i in range(10):
        #Select a random letter
        letter = random.choice(LETTER_FREQ_POOL)

        # Maintain frequency distribution of randomly drawn letters
        if letter in letter_freq:
            letter_freq[letter] += 1
            # Check if letter drawn at random is within frequency limits - redraw letter if not
            if letter_freq[letter] > LETTER_FULL_POOL[letter]:
                continue
        else:
            letter_freq[letter] = 1

        # Add letter to letter bank
        letters_drawn.append(letter)
    
    return letters_drawn

def uses_available_letters(word, letter_bank):
    letter_list = letter_bank.copy()
    
    for letter in word:
        if letter.upper() in letter_list:
            # Update still available letters by removing letter from list
            letter_list.remove(letter.upper())
        else: 
            return False
        
    return True

def score_word(word):
    score = 0
    for letter in word:
        score += LETTER_POINTS[letter.upper()]

    # Points bonus for words having 7-10 letters
    if (len(word) >= 7):
        score += 8

    return score

def get_highest_word_score(word_list):
    i = 0
    max_score_ind = 0
    scores = []
    
    for word in word_list:

        scores.append(score_word(word))      
        
        if (i == 0):
            max_score_ind = 0
        elif (scores[i] > scores[max_score_ind]):
            #New high score, track its index
            max_score_ind = i
        elif (scores[i] == scores[max_score_ind]):
            x = len(word_list[i])
            y = len(word_list[max_score_ind])
            # Equality rule 1: Multiple words with same score - keep the earlier word in list
            if (x == y):
                pass
            #Equality rule 2: If both words less than 10 letters, pick word with less letters
            elif ((x < 10) and (y < 10)):
                if (x < y):
                    max_score_ind = i
            # Equality rule 3: If next word has 10 letters but previous one is less, pick the new one
            elif (x == 10 and y < 10):
                max_score_ind = i

        i += 1

    return word_list[max_score_ind], scores[max_score_ind]