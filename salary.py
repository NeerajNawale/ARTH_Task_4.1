import joblib as jb
import sys

model = jb.load("salary_model.pk1")
y = model.predict([[sys.argv[1]]])

print("\n\n\nPredicted Salary for '"+sys.argv[1]+"' year's of experience --> ", end="")
print(y)
print("\n\n")
