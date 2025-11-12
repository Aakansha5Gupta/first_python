import pandas as pd 
# create a dataset using dictionary
data = {
    "Student_ID":[181,182,183,184,185],
    "Name":["Aakansha Gupta",'Anushka Khare',"Avinash Yadav","Naksh Goyel","Prachi Garg"],
    "Gender":["F","F","M","M","F"],
    "Maths":[78,85,69,92,74],
    "Science":[83,79,72,95,68],
    "English":[87,90,75,89,88],
    "Attendance":[92,96,81,99,98]
}

# Convert to pandas dataforms
df = pd.DataFrame(data)

#display dataset
print(df)

#save dataset to CSV file
df.to_csv("students_performance.csv",index=False)