scores = []

number_of_students = int(input("Enter the number of students: "))

for i in range(number_of_students):
  score = list(map(int, input("Enter thr marks of 2 subjects").split()))
  scores.append(score)
  
valid_scores = []

for i in scores:
  valid = True
  for j in i :
    if j == 0 :
      valid = False
      break
  if valid:
    valid_scores.append(i)

print(len(valid_scores))
  