from build import Input, Template
from stackauth import StackAuth
from stackexchange import Site, ArqadeMeta

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
            elif answer.up_vote_count > best_answer.up_vote_count:
                best_answer = answer

        # Initialzie winning_answer
        self.winning_answer = best_answer
        return best_answer

    @property
    def sotw_num(self):
        pass

    @property
    def username(self):
        pass

    @property
    def tag(self):
        pass

    @property
    def upvotes(self):
        pass

    @property
    def last_winning(self):
        pass

    @property
    def last_screenshot(self):
        pass

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
    if theme.tolower() not in ["y", "n"]:
        continue
    elif theme.tolower() == "y":
        theme_title = input("Theme title:")
        theme_description = input("Theme description:")
    break

# Retrieve question and create the post
id = 16693
meta = Site(ArqadeMeta)
question = meta.question(id)


# Perform the build
input = Input()
template = Template(input)
template.CreateOutput()
