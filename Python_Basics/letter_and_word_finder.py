#This program finds the number of times a specific word is used in a sentence

search = "is" #input("Please enter the letter or digit you want to search:\n")

sentence = "My name is Namer Afzal Khan. My age is 33. My educational background relates to finance, banking and IT. The purpose of this program is to find the number of times a specific word is used in a sentence. Let's see how many times my is detected in this sentence. "#input("Please write a sentence and then press enter:\n")

word_counter = 0

word = ""

substring = ""

total_instances_as_substring = 0

counter = 0

word_character_counter = 0

if search.lower() == sentence.lower():
    print("Hey!!! why are you tring to waste my time :<")

else:
    for letter in range(len(sentence)):
        if sentence[letter] != " ":
            word = word + sentence[letter]

            if sentence[letter].lower() == search.lower():
                word = ""
                word_counter = word_counter + 1
                substring = ""
                counter = 0
                total_instances_as_substring =  total_instances_as_substring + 1

            
            elif sentence[letter].lower() == search[counter].lower():
                substring = substring + sentence[letter].lower()
                word_character_counter = word_character_counter + 1
                if substring.lower() == search.lower():
                    total_instances_as_substring =  total_instances_as_substring + 1
                    counter = 0
                    substring = ""
                else:
                    if counter == len(search) - 1:
                        counter = 0
                    else:
                        counter = counter + 1

            else:
                substring = ""
                counter = 0
                word_character_counter = word_character_counter + 1

        else:
            if word.lower() == search.lower():
                word_counter = word_counter + 1
                word = ""

            else:
                word = ""

            word_character_counter = 0



print(f'Number of times \"{search}\" is used in \"{sentence}\" is: {word_counter}')

print("\n\n\n")

print(f'Number of times \"{search}\" appeared as a substring in \"{sentence}\" is: {total_instances_as_substring}')

