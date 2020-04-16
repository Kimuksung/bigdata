import pandas as pd


raw_data = {
            'first_name': ['Jason', 'Jason', 'Tina', 'Jake', 'Amy'],
            'last_name': ['Miller', 'Miller', 'Ali', 'Milner', 'Cooze'],
            'age': [42, 42, 36, 24, 73],
            'preTestScore': [42, 42, 31, 2, 42],
            'postTestScore': [25, 25, 57, 62, 70]
}
df = pd.DataFrame(raw_data)
print(df)
df.drop_duplicates(['preTestScore'], keep='last')
print(df)