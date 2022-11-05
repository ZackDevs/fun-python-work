# Made by ZackDevs (https://github.com/ZackDevs)

print("This game was created with https://the-trivia-api.com/docs/.")
print("If any answer is wrong it's not my fault.\n")
import requests
import random
response = requests.get(
    'https://the-trivia-api.com/api/questions?categories=general_knowledge&limit=10&difficulty=medium',
)
response = response.json()
points = 0
for i in range(len(response)):
  question = response[i]["question"]
  answers = [response[i]["correctAnswer"]] + response[i]["incorrectAnswers"]
  random.shuffle(answers)
  print(question+"\n")
  for b in range(len(answers)):
    print(f"{b+1} - {answers[b]}")
  reply = input()
  try:
    reply = int(reply)
    if answers[reply-1] == response[i]["correctAnswer"]:
      print(f"Correct! You've now got {points+1}/{len(response)}\n")
      points += 1
    else:
      print(f'Nice try but the correct answer was {response[i]["correctAnswer"]}\n')
      
  except:
    print("Please only use numbers...")
    print(f'Correct Answer: {response[i]["correctAnswer"]}\n')
  
print()
print(f"You've finished the quiz with {points}/{len(response)} points!")
print("Well done.")
  
  
