# Make the user enter some sentences. If he wants to end he has to type end.
# After he has entered, arrange these sentences properly in a single line along will all the needed punctuations
# Sentences starting with how, what, why must have a question mark at the end.
# The rest of the sentences should have a full stop.

# Function
def corrections(line):

    questions = ("How","When","What","Why")
    capline = line.capitalize() # Capitalizing the line

    if line.startswith(questions):
        return f"{capline}?"
    else:
        return f"{capline}."


sentences = []
while True:
    sentence = input("Say something : ")
    if sentence == "end":
        break
    else:
        sentences.append(corrections(sentence))

print(" ".join(sentences))
