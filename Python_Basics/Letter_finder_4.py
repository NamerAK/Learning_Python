#This program finds the number of times a specific word is used in a sentence

search = "i" #input("Please enter the letter or digit you want to search:\n")

sentence = "My name is Namer Afzal Khan. My age is 33. My educational background relates to finance, banking and IT. The purpose of this program is to find the number of times a specific word is used in a sentence. Let's see how many times my is detected in this sentence. "#input("Please write a sentence and then press enter:\n")

word_counter = 0
word = ""


if search.lower() == sentence.lower():
    print("Hey!!! why are you tring to waste my time :<")

else:
    for letter in sentence:
        if letter != " ":
            word = word + letter
        else:
            if word.lower() == search.lower():
                word_counter = word_counter + 1
                word = ""
            else:
                word = ""



print(f'Number of times \"{search}\" is used in \"{sentence}\" is: {word_counter}')

