import pandas as pd

print("                      ===== Data Science =====")

Data = pd.read_csv("Negara.csv")

df = pd.DataFrame(Data)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print("\n")
print(df)
print("\nBerikut data mean:")
print(mean)
print("\nBerikut Data Standard Deviation:")
print(std)