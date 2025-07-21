#This program finds the number of times a specific letter is used in a sentence

sentence = "My name is Namer Afzal Khan. My age is 33. My educational background relates to finance, banking and IT. The purpose of this program is to find the number of times a specific word is used in a sentence. Let's see how many times my is detected in this sentence. "#input("Please write a sentence and then press enter:\n")

search = "Is" #input("Please enter the letter or digit you want to search:\n")

search_word_character_counter = 0
character_counter =0 #Character counter excluding white space

words_counter = 0

total_words = []

each_word_length = []

word = ""

counter = 0

for i in sentence:
    for j in range(len(search)):
        if search[j].lower() == i.lower():
            character_counter += 1
            word = word + i
        break
    if word == search:
        words_counter += 1
        character_counter = 0
        word = ""
    
    

print(words_counter)
print(f'The number of times {search} appeared in \"{sentence}\" is: {words_counter}')
