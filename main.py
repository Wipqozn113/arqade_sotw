from pathlib import Path
import datetime as dt

class Input:
    def __init__(self, filename='input.in'):
        with open(filename) as file:
            for line in file:
                if line.startswith('sotw_num'):
                    self.sotw_num = self.GetValue(line)
                elif line.startswith('tag'):
                    self.tag = self.GetValue(line)
                elif line.startswith('upvotes'):
                    self.upvotes = self.GetValue(line)
                elif line.startswith('username'):
                    self.username = self.GetValue(line)
                elif line.startswith('theme_title'):
                    self.theme_title = self.GetValue(line, "No Theme")
                elif line.startswith('theme_text', ):
                    self.theme_text = self.GetValue(line, "There's no theme this week, so just send us the best you've got!")
                elif line.startswith('last_winning'):
                    self.last_winning = self.GetValue(line)
                elif line.startswith('last_screenshot'):
                    self.last_screenshot = self.GetValue(line)
                elif line.startswith('vote_date'):
                    self.vote_date = self.GetValue(line, self.DateHelper(7))
                elif line.startswith('end_date'):
                    self.end_date = self.GetValue(line, self.DateHelper(14))
    
    def DateHelper(self, delta):
        date = dt.datetime.today() + dt.timedelta(delta)
        return date.strftime('%Y-%m-%d')

    def GetValue(self, line, default=""):
        l = line.split("|")
        val = default
        if len(l) == 2 and len(l[1]) > 1:
            val = l[1].strip()

        return val

class Template:
    def __init__(self, input, filename='template.in', inputs=('sotw_num', 'username', 'tag', 'upvotes', 'theme_title', 'theme_text', 'last_winning', 'last_screenshot', 'vote_date', 'end_date')):
        self.template = Path(filename).read_text()
        self.input = input
        self.inputs = inputs

    def CreateOutput(self, filename="output.out"):
        output = self.template
        for inp in self.inputs:
            val = getattr(self.input, inp)
            output = output.replace("{" + inp + "}", val)

        with open(filename, 'w') as file:
            file.write(output)

input = Input()
template = Template(input)
template.CreateOutput()

        


