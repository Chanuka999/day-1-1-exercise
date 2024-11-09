student_scores = input("Input a list of students scores:").split()

for b in range(0, len(student_scores)):
    student_scores[b] = int(student_scores[b])
print(student_scores)

max_score =0
for score in student_scores:
    if(score > max_score):
        max_score = score   
print(f"the height score is:{max_score}")
