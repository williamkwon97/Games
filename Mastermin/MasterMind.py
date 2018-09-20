

Colors = ["R", "G", "Y", "P", "B", "O"]
answer = []
file = open("input.txt", "r")
for x in file:
    answer=x.strip("\n")

def getGuessFromUser():
  userGuess = input("Guess: ")
  return userGuess


def displayFeedback(feedback):
  print("Feedback: {0}{1}{2}{3}".format(feedback[0], feedback[1], feedback[2], feedback[3]))


def errorMessage():
  print("Error")


def finalScoreCodebreaker(numOfTurns):
  print("Score: -{0}".format(numOfTurns))


def generateAnswer():
    answeris = []
    with open('input.txt', 'r') as f:
        for x in f:
            answeris.append(x.strip("\n"))
    myList = list(answeris[0])
    return (myList)
    return answeris
def main():
  answer = generateAnswer()


  s=0


  # user get in right first try
  guessedAnswer = False
  incorrect = False
  n=1
  while n <= 10 :
     guess = getGuessFromUser()
     guess.upper()

     if len(guess)!= 4 :
         errorMessage()
         continue

     if not all(c in Colors for c in guess):
        errorMessage()
        continue


     for i in range(len(answer)):
        if (guess[i] != answer[i]):
           incorrect = True



     feedback=[]
     if incorrect:


        d = {'R' : 0, 'G' : 0,  'Y' : 0, 'P' : 0, 'B' : 0, 'O' : 0}

        for a in answer:
            d.update({a: d.get(a) + 1})

        for i in range(4):



           if answer[i] == guess[i]:
              feedback.append(guess[i])
           elif answer[i] != guess[i] and d[guess[i]] > 0:
              feedback.append("W")
              d.update({guess[i]: d.get(a) - 1})
           else  :
              feedback.append("_")

     else:
        feedback = answer
     s+=1
     if guessedAnswer == incorrect:
         displayFeedback(guess)
         finalScoreCodebreaker(s)
         break
     displayFeedback(feedback)
     finalScoreCodebreaker(s)
     n+=1






main()
