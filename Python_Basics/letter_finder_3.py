#This program finds the number of times a specific letter is used in a sentence

search = "is" #input("Please enter the letter or digit you want to search:\n")

sentence = "My name is Namer Afzal Khan. My age is 33. My educational background relates to finance, banking and IT. The purpose of this program is to find the number of times a specific word is used in a sentence. Let's see how many times my is detected in this sentence. "#input("Please write a sentence and then press enter:\n")


search_length = len(search)

search_word_character_counter = 0

character_counter =0 #Character counter excluding white space

words_counter = 0

total_words = []

each_word_length = []

word = ""

counter = 0



for i in range(len(sentence)):
    if sentence[i].lower() == search.lower():
        words_counter = words_counter + 1
        word = ""
        character_counter = 0
    elif sentence[i].lower() == search[character_counter].lower():
        word = word + sentence[i].lower()
        character_counter = character_counter + 1
        if character_counter == search_length:
            character_counter = 0
        
    elif sentence[i].lower() == search[character_counter].lower():
        word = word + sentence[i].lower()
        character_counter = character_counter + 1
        if character_counter == search_length:
            character_counter = 0
       
            
        
    elif sentence[i] == " ":
        
        if word.lower() == search.lower():
            words_counter = words_counter + 1
            character_counter = 0
        word = ""

    elif sentence[i].lower() != search[character_counter].lower():
            word = ""
            character_counter = 0

    print(f'Sentence_letter_counter = {i} | Sentence_letter = {sentence[i]}  | Search_Index = {i % search_length}  | Word = {word} | Words_counter = {words_counter}')
   
           
        
    
    
print(words_counter)
print(f'The number of times {search} appeared in \"{sentence}\" is: {words_counter}')
