class Quiz:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question = [
     "Who developed Python Programming Language?\n(a)Guido Van Rossum\n(b)E F Codd\n",
     "What is WORA?\n(a)Wear Once Roll Anywhere\n(b)Write Once Read Anywhere\n",
]

keys = [
     Quiz(question[0], "a"),
     Quiz(question[1], "b"),
]

def run_quiz(keys):
     score = 0
     for i in keys:
          answer = input(i.prompt)
          if answer == i.answer:
               score += 1
     print("You scored", score, "out of", len(keys), ". ")

run_quiz(keys)
