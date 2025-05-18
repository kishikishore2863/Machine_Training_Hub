import pandas as pd

data = {
    "name":["kishi","kishore","hellen","alex"],
    "age":[21,21,23,24]
}
df = pd.DataFrame(data)
print(df)
print("Average age:", df["age"].mean())