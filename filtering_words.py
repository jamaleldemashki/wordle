#Helper function to remove words containing digits. Cleaning the data we have
def noDigit(word):
    for i in word:
        if i >= "0" and i <= "9":
            return False
    return True

def noPoint(word):
    for i in word:
        if i == "." or i == "!" or i == "?" or i == ",":
            return False
    return True

def filter_five_letter_words(input_file, output_file):
    #We first need to read the words from the words file
    with open(input_file, "r") as f:
        words = f.readlines()
        
    #Wordle only uses 5 letter words, therefor we will filter out wirds of length != 5
    five_letter_words = []
    for word in words:
        cleaned_word = word.strip() #remove white spaces or newlines
        if len(cleaned_word) == 5:
            if noDigit(cleaned_word) and noPoint(cleaned_word):
                five_letter_words.append(cleaned_word.lower())
            
    #Now let us write the filtered words in a new file
    with open(output_file, "w") as out:
        for w in five_letter_words:
            out.write(w + "\n")
            
    print(f"Number of 5-letter words found: {len(five_letter_words)}")
    

if __name__ == "__main__":
    filter_five_letter_words("words.txt", "five_letter_words.txt") 