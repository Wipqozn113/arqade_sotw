from build import Input, Template
from stackauth import StackAuth
from stackexchange import Site, ArqadeMeta
import re

class SOTWParser:
    winning_answer = None

    def __init__(self, question):
        self.question = question

    @property
    def winningAnswer(self):
        # Don't want to do this twice
        if self.winning_answer is not None:
            return self.winning_answer
        
        # Find the winning post
        best_answer = None
        for answer in self.question.answers:
            if best_answer is None:
                best_answer = answer
            elif answer.score > best_answer.score:
                best_answer = answer

        # Initialzie winning_answer
        self.winning_answer = best_answer
        return best_answer

    @property
    def sotw_num(self):
        title = self.question.title
        regex = re.compile('#[0-9]+')
        match = regex.search(title)
        
        return (int(match.group(0)[1:]) + 1)


    @property
    def username(self):
        return self.winningAnswer.owner.display_name

    @property
    def tag(self):
        regex = re.compile('[tag:[0-9a-zA-Z\-]+]')
        match = regex.search(self.winningAnswer.body)

        return match.group(0)

    @property
    def upvotes(self):
        return self.winningAnswer.score

    @property
    def last_winning(self):
        return self.question.link

    @property
    def last_screenshot(self):
        regex = re.compile('https://i.stack.imgur.com/[0-9a-zA-Z]+.jpg')
        match = regex.search(self.winningAnswer.body)

        return match.group(0)


# Retrieve ID or URL for previous SOTW
inp = input("Please enter the Post ID or URL for the SOTW that just finished: ")
if inp.strip().isdigit():
    id = int(inp)
elif "/" in inp:
    id = int(inp.split("questions")[1].split("/")[1])
else:
    print("Invalid ID or URL!")
    exit()

# Determine if there's a theme
theme_title = None
theme_description = None
while True:
    theme = input("Is there a theme (y/n)?")
    if theme.lower() not in ["y", "n"]:
        continue
    elif theme.lower() == "y":
        theme_title = input("Theme title:")
        theme_description = input("Theme description:")
    break

# Retrieve question and create the post
id = 16693
meta = Site(ArqadeMeta)
question = meta.question(id)
parser = SOTWParser(question)


# Perform the build
'''
input = Input()
template = Template(input)
template.CreateOutput()
'''
