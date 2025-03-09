# This function counts the words in the file
def words_in_string (words):
    word_counter = 0
    
    words_string = words.split()

    for word in words_string:
        word_counter += 1
    print("----------- Word Count ----------")
    print(f"Found {word_counter} total words")

# This function shows the number of time each character appears
def character_count (book_string):

    character_dictionary = {}

    for character in book_string:
        lower_case = character.lower()

        if lower_case in character_dictionary:
            
            character_dictionary[lower_case] += 1
        else: 
            character_dictionary[lower_case] = 1

    for i in character_dictionary:
        
        print(f"{i}:  {character_dictionary[i]}")

    # print(f"{character_dictionary}")

    # return character_dictionary
