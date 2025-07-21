#This program finds the number of times a specific letter is used in a sentence

#sentence = "My name is Namer Afzal Khan. My age is 33. My educational background relates to finance, banking and IT. The purpose of this program is to find the number of times a specific word is used in a sentence. Let's see how many times my is detected in this sentence. "#input("Please write a sentence and then press enter:\n")

sentence = " My name is namer evisgrt is good"

search = "is" #input("Please enter the letter or digit you want to search:\n")

search_word_character_counter = 0
character_counter = 0  #Character counter excluding white space

words_counter = 0

total_words = []

each_word_length = []

word = ""

counter = 0

for i in range(len(sentence)):
    if search.lower() == sentence[i].lower():
        words_counter = words_counter + 1

    elif search[i].lower() == sentence[i].lower():
        
        
    elif search[len(search) - character_counter].lower() == sentence[i].lower():
        word = word + search[len(search) - character_counter].lower()
        if word.lower() == search.lower():
            words_counter = words_counter + 1
            word = ""
            character_counter = len(search) -1
            print (character_counter)
        character_counter = character_counter - 1 if character_counter > 1 else len(search) - 1
    elif search[character_counter - 1] == " ":
        word = ""
        character_counter = 0


    print(i)
        
        

    
print(words_counter)
print(f'The number of times {search} appeared in \"{sentence}\" is: {words_counter}')
