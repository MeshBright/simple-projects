# 1. DEFINE THE DATA
# We are creating the dictionary that holds the score for every letter.
letter_scores = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# We are defining the raw text string that needs processing.
text_data = """
  What do you think you can do? Huh?!!! Well, whatever you think you can do I can do better, do you hear me?? Yeah, I' talking to you Methushael
"""

# 2. CLEANING THE TEXT (The "Inefficient" Way)
# Instead of using replace() once, we will manually define a list of things we want to remove.
punctuation_to_remove = [",", ".", "!", "?", "\n"]

# We start with the original text.
clean_text_step_1 = text_data

# We loop through every single punctuation mark in our list above.
for mark in punctuation_to_remove:
    # We replace that specific mark with an empty space " ".
    # Note: Using " " instead of "" helps prevent words from sticking together.
    clean_text_step_1 = clean_text_step_1.replace(mark, " ")

# Now we need to handle casing. We will manually convert the whole string to lowercase.
clean_text_lower = clean_text_step_1.lower()

# Now we need to turn this big string into a list of individual words.
# We split by empty spaces.
raw_word_list = clean_text_lower.split(" ")

# The split above might create empty strings '' because of extra spaces.
# We will create a new list and manually copy over only the "real" words.
final_word_list = []
for word in raw_word_list:
    # If the word is NOT an empty string, we keep it.
    if word != "":
        final_word_list.append(word)

# 3. GETTING UNIQUE WORDS
# Instead of using set(), we will manually check for duplicates.
unique_words = []
for word in final_word_list:
    # We check if the word is already in our new list.
    if word not in unique_words:
        # If it is not there, we add it.
        unique_words.append(word)

# 4. SCORING THE WORDS (Nested Loops)
# We will create a dictionary to store our results.
word_scores = {}

# We start looping through every unique word we found.
for word in unique_words:
    # We create a variable to hold the score for THIS current word.
    current_score = 0
    
    # Now we loop through every letter inside the current word.
    for letter in word:
        # We look up the letter in our letter_scores dictionary.
        # We check if the letter exists in the dictionary first to be safe.
        if letter in letter_scores:
            points_for_this_letter = letter_scores[letter]
            # We add those points to the current score.
            current_score = current_score + points_for_this_letter
            
    # 5. APPLYING CONDITIONS (Bonus Points)
    # We count how many letters are in the word.
    length_of_word = len(word)
    
    # We check the rule: if length is greater than 6.
    if length_of_word > 6:
        # We add 5 bonus points.
        current_score = current_score + 5
        
    # Now that we are done calculating, we save it into our dictionary.
    # The key is the word, the value is the final score.
    word_scores[word] = current_score

# 6. FILTERING HIGH SCORES (The Manual Way)
# We want a list of strings for words with scores > 10.
# Instead of a list comprehension, we do a standard loop.
high_value_words = []

# We loop through the dictionary keys (the words).
for word in word_scores:
    # We retrieve the score for that word.
    score = word_scores[word]
    
    # We check the condition.
    if score > 10:
        # We manually build the formatted string.
        formatted_string = word + " ==> " + str(score)
        # We add it to our final list.
        high_value_words.append(formatted_string)

# 7. FINAL OUTPUT
# We print the result.
print("High Value Words List:")
print(high_value_words)








