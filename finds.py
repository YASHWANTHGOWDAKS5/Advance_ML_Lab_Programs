import pandas as pd

enjoy_sports_data = [
    {"Sky": "Sunny", "AirTemp": "Warm", "Humidity": "Normal", "Wind": "Strong", "Water": "Warm", "Forecast": "Same", "EnjoySport": "Yes"},
    {"Sky": "Sunny", "AirTemp": "Warm", "Humidity": "High", "Wind": "Strong", "Water": "Warm", "Forecast": "Same", "EnjoySport": "Yes"},
    {"Sky": "Rainy", "AirTemp": "Cold", "Humidity": "High", "Wind": "Strong", "Water": "Warm", "Forecast": "Change", "EnjoySport": "No"},
    {"Sky": "Sunny", "AirTemp": "Warm", "Humidity": "High", "Wind": "Strong", "Water": "Cool", "Forecast": "Change", "EnjoySport": "Yes"}
]

data = pd.DataFrame(enjoy_sports_data)

data = data.values

h = []
index=-1
for instence in data:
    if instence[-1].lower() == 'yes':
        h = instence[:-1] # Initial first positive hypothysis
        index+=1
        break
print(f"Found positive instence at index {index}.")
print(f"Initial Hypothysis: {h}\n")

for inst in data:
    if inst[-1].lower() == 'yes':
        print("Hypothysis: ",h)
        print("Compared with:",inst[:-1])
        for i in range(len(h)):
            if h[i]!=inst[i]:
                h[i]='?'
            else:
                h[i]==inst[i]
        print("\nUpdated Hypothysis: ",h,"\n")

print("-_"*10,"\n")
print("Final Hypothysis: ",h)

#Output

# Initial Hypothysis: ['Sunny' 'Warm' 'Normal' 'Strong' 'Warm' 'Same']

# Hypothysis:  ['Sunny' 'Warm' 'Normal' 'Strong' 'Warm' 'Same']
# Compared with: ['Sunny' 'Warm' 'Normal' 'Strong' 'Warm' 'Same']

# Updated Hypothysis:  ['Sunny' 'Warm' 'Normal' 'Strong' 'Warm' 'Same'] 

# Hypothysis:  ['Sunny' 'Warm' 'Normal' 'Strong' 'Warm' 'Same']
# Compared with: ['Sunny' 'Warm' 'High' 'Strong' 'Warm' 'Same']

# Updated Hypothysis:  ['Sunny' 'Warm' '?' 'Strong' 'Warm' 'Same'] 

# Hypothysis:  ['Sunny' 'Warm' '?' 'Strong' 'Warm' 'Same']
# Compared with: ['Sunny' 'Warm' 'High' 'Strong' 'Cool' 'Change']

# Updated Hypothysis:  ['Sunny' 'Warm' '?' 'Strong' '?' '?'] 

# -_-_-_-_-_-_-_-_-_-_ 

# Final Hypothysis:  ['Sunny' 'Warm' '?' 'Strong' '?' '?']