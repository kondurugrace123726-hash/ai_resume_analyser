skills = ['java', 'python', 'html', 'css', 'sql', 'javascript' ]
resume = input("Paste your Resume text:\n").lower()
found = []
missing = []
for skill in skills:
    if skill in resume:
        found.append(skill)
    else:
        missing.append(skill)

score = (len(found)/len(skills)) * 100

print("\n Resume Score: ", round(score), "%")
print("Skills found: ", ",".join(found))
print("Skills missing: ", ",".join(missing))

if score < 50:
    print("Suggestion: Add more technical skills")
else:
    print("Good technical profile!")