import matplotlib.pyplot as plt
import pandas as pd

categories = ['Tweets', 'Followers', 'Listed', 'Favorites']
values = list(range(len(categories)))

fig, ax = plt.subplots()

legislators = pd.read_csv('legislators.csv')
tweets = pd.read_csv('legislators-twitter.csv')
df = pd.merge(legislators, tweets, left_on='twitter_id', right_on='Screen name')

democrats = df[df['party'] == 'D']
republicans = df[df['party'] == 'R']
democrat_vals = [democrats[cat].median() for cat in categories]
republican_vals = [republicans[cat].median() for cat in categories]

ax.bar(values, democrat_vals, align='center', label='Democrats', color='DodgerBlue')
ax.bar(values, republican_vals, align='center', bottom=democrat_vals,
       label='Republicans', color='Crimson')
ax.set_xticks(values)
ax.set_xticklabels(categories)

ax.legend()
ax.set_title('Twitter Metrics of US Legislators') 
ax.set_ylabel('Median value')

fig.savefig('congress_twitter.png')



