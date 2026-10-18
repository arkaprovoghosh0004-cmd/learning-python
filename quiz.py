qna = {"What is 2+2 ? " :"4", 
"What color is the sky on a clear day? ": "blue", 
"How many days are there in a week? ": "7", 
"What is the capital of France? ": "Paris", 
"What does CPU stand for? ": "Central Processing Unit" }

score = 0

for question, answer in qna.items():
  q = input(question)
  
  if q.lower() == answer.lower():
    print("Correct!")
    score += 1
  else: 
    print(f"Wrong. The correct answer is {answer} ")

print("Final score: ", score, "/", len(qna))
  
