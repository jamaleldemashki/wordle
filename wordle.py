from collections import Counter



def best_starting_word_with_frequency(word_list_file):
    #Read words
    with open(word_list_file, "r") as f:
        words = [line.strip() for line in f]
        
    #Count letter frequencies
    letter_counter = Counter()
    for w in words:
        for ch in w:
            letter_counter[ch] += 1
    
    #Get 5 most frequently used letters
    top_5_letters = [letter for letter, _ in letter_counter.most_common(6)]
    print(top_5_letters)
    
    unique_words = []
    for w in words:
        if len(set(w)) == 5:
            unique_words.append(w)
    
    print(f"We have: ", len(unique_words), " unique word.")
    
    best_word = None
    best_score = -1
    
    #Now find the word with the most top-5 letters
    for w in unique_words:
        score = sum(ch in top_5_letters for ch in w)
        if score > best_score:
            best_score = score
            best_word = w
            
    return best_word, best_score
    

if __name__ == "__main__":
    chosen_word, score = best_starting_word_with_frequency("five_letter_words.txt")
    print("Potential best starting word:", chosen_word)
    print("It contains", score, "of the top 6 letters overall.")
      