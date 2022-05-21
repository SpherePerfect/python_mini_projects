dictionary = {"lenient":"more merciful or tolerant than expected",\
"orientation":"the action of orienting someone or something relative to the points of a compass or other specified positions.",\
"orthopaedic":"relating to the branch of medicine dealing with the correction of deformities of bones or muscles.",\
"reasonable":"having sound judgement; fair and sensible."}

print("Hello, welcome to the mini dictionary")

print("Type the word you want to search")

searched_word = input()

if searched_word in dictionary:
    print("The meaning of", searched_word,"is:", dictionary[searched_word])
else:
    print("This word was not found")




