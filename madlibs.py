def getWord(wordDescription):
    wordType = input(f"Please give me a {wordDescription} ")
    return wordType

sillyword = getWord('silly word')
pluralnoun = getWord('plural noun')
bodypartplural = getWord('part of the body (plural)')
noun = getWord('noun')

madLib = (f"'{sillyword}! Playing Mad Libs is way more fun than squishing {pluralnoun} with my bare {bodypartplural}. I don't even have to take a hot {noun} afterward!'")
print(madLib)

