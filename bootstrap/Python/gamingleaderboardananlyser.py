import pandas as pd
scores = [98500, 87200, 76400, 65100, 54800]
players = pd.Series(scores, index=['NightWolf', 'StarBlaze', 'PixelKing', 'CyberFox', 'IronStorm'])
print(plaayers)
data = {
    'Player': ['NightWolf', 'StarBlaze', 'PixelKing', 'CyberFox', 'IronStorm']
    'Level':  [42, 38, 35, 30, 27],
    'Score':  [98500, 87200, 76400, 65100, 54800],
    'Wins' :  [210, 185, 162, 140, 118]
}
df = pd.DataFrame(data)
print(df)
print()
print('Row top (Player):')
print(df.loc[0])
print()
print('Rows 2 and 3:')
print(df.loc[2:3])
print()
full_df = pd.read_csv('leaderboard.csv')
print('First 5 rows (head):')
print(full_df.head())
print()
print('Last 3 rows (tail):')
print(full_df.tail(3))
print()
print(full_df.info())
print()
clean_off = full_df.dropna()
print(clean_df.to_string())
print()
filled_df = full_df.fillna(0)
print(filled_df.to_string())