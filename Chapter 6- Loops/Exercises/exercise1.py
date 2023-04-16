prompt = "What toppingg would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    toppingg = input(prompt)
    if toppingg != 'quit':
        print(" I'll add " + toppingg + " to your pizza.")
    else:
        break
