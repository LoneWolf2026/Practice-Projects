import pandas as pd

df = pd.DataFrame()
columns = 0

percent_col = []
exercise_col = []
weight_prcnt = 100

for i in range(10,4,-1):
    percent_col.append(f'{weight_prcnt}%')
    weight_prcnt = weight_prcnt - 10
    
    dfPRCNT = pd.DataFrame({'Percent_Weight': percent_col})
df = pd.concat([df,dfPRCNT])

while columns < 4:
    exercise = input("List an exercise: ")
    max_weight = round(float(input("What is the max weight you use in pounds? ")),1) #Not the most practical approach to making a weight table, but helps us practice with pandas
    max_reps = int(input("How many reps have you done at this weight: "))

    if max_reps == 1:
        #print(max_weight)
        pass
    elif max_reps > 1:
        if max_reps <= 3:
            max_weight = max_weight/(9/10) #Extrapolating max weight
        elif max_reps > 3 and max_reps <= 5:
            max_weight = max_weight/(8/10)
        elif max_reps > 5 and max_reps <= 10:
            max_weight = max_weight/(7/10)
        elif max_reps > 10:
            print(f"Dude, is {max_weight} lbs really your max weight?")
    weight_prcnt = 100
    for i in range(10,4,-1):
        working_weight = round(max_weight*weight_prcnt/100)
        #print(working_weight)
        exercise_col.append(working_weight) #exercise column holds weights for each individual exercise
        if weight_prcnt >= 20:
            weight_prcnt = weight_prcnt - 10
        else:
            continue
    df[exercise] = exercise_col
    exercise_col.clear()

    columns += 1
    weight_prcnt = 100


print(df)
# try making a table with data analysis libraries with the above