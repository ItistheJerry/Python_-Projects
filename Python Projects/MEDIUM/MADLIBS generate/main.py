# Story will have Replacable words where we take input and complete the story and read it


'''One day, a <adjective> <animal> was wandering through the <place> when it stumbled upon a <adjective> <object>. Curious, it picked it up and suddenly, POOF!—the <object> started to glow!

Before the <animal> could react, a <adjective> <creature> appeared and said, "I am the guardian of the <object>! To keep it, you must complete a <adjective> challenge!"

The <animal> took a deep breath and bravely said, "I'm ready!"


What happened next? Well, that's a story for another day...

/Users/thejoker/Desktop/Python Projects/MEDIUM/MADLIBS generate/story.txt

'''



with open("\n/Users/thejoker/Desktop/Python Projects/MEDIUM/MADLIBS generate/story.txt \n", "r") as f:
    story = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

# Below code is for locating the words
# enumerate gives access to the position as well as element at the position
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1] # slice operator where start of the word and end of the word:
        words.add(word)
        start_of_word = -1


answers = {}

# we will loop through all of the unique words and ask user to fill


for word in words:
    answer = input(f"Enter a word for: {word}: ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)

