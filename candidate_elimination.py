import pandas as pd

enjoy_sports_data = [
    {"Sky": "Sunny", "AirTemp": "Warm", "Humidity": "Normal", "Wind": "Strong", "Water": "Warm", "Forecast": "Same", "EnjoySport": "Yes"},
    {"Sky": "Sunny", "AirTemp": "Warm", "Humidity": "High", "Wind": "Strong", "Water": "Warm", "Forecast": "Same", "EnjoySport": "Yes"},
    {"Sky": "Rainy", "AirTemp": "Cold", "Humidity": "High", "Wind": "Strong", "Water": "Warm", "Forecast": "Change", "EnjoySport": "No"},
    {"Sky": "Sunny", "AirTemp": "Warm", "Humidity": "High", "Wind": "Strong", "Water": "Cool", "Forecast": "Change", "EnjoySport": "Yes"}
]

data = pd.DataFrame(enjoy_sports_data).values

X = data[:,:-1]
y = data[:,-1]

s = X[0].copy()
G = [['?' for _ in range(len(s))]]

for i in range(len(data)):
    if y[i]=='Yes':
        G = [g for g in G if all(g[j]=='?' or g[j]==X[i][j] for j in range(len(s)))]
        for j in range(len(s)):
            if s[j]!=X[i][j]:
                s[j]='?'
        
    else:
        new_G = []
        for j in range(len(s)):
            if s[j]!='?' and s[j]!=X[i][j]:
                g = ['?' for _ in range(len(s))]
                g[j]=s[j]
                new_G.append(g)
        G = new_G
print("Specific final:",s)
print("General final:",G)

# Output
# Specific final: ['Sunny' 'Warm' '?' 'Strong' '?' '?']
# General final: [['Sunny', '?', '?', '?', '?', '?'], ['?', 'Warm', '?', '?', '?', '?']]