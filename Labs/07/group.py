import pandas as pd

df = pd.read_csv('heartDisease.csv')

df['sex'] = df['sex'].replace({0: 'female', 1: 'male'})
print(df.head()) 
print("\n")

males = df[df['sex'] == 'male'][['chol', 'restecg', 'oldpeak']]
females = df[df['sex'] == 'female'][['chol', 'restecg', 'oldpeak']]

male_stats = {
    'mean': males.mean(),
    'median': males.median(),
    'min': males.min()
}

female_stats = {
    'mean': females.mean(),
    'median': females.median(),
    'min': females.min()
}

print("Male Statistics:")
print(pd.DataFrame(male_stats))

print("\nFemale Statistics:")
print(pd.DataFrame(female_stats))
