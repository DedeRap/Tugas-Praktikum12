import pandas as pd

print("                    ===== Data Science ke 2 =====")

Data = pd.read_csv("Negara.csv")

df = pd.DataFrame(Data)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print("\n")
print(df)
print("\nBerikut data mean:")
print(mean)
print("\nBerikut Data Standar Deviation:")
print(std)

mean.to_csv("NegaraMean.csv")
std.to_csv("NegaraStandarDeviation.csv")
print("\nFile telah dibuat.")