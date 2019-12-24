import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('top.csv')


plt.title("Popular Genres Of 2019")
fig, ax = plt.subplots(figsize=(10, 3), tight_layout=True)
ax.tick_params(axis='x', rotation=70)
plt.hist(df.Genre)
plt.show()