import json

with open ("alice.txt", mode = "r", encoding = "utf-8" ) as alice_file:
    freq = {}
    
    for line in alice_file:
        words = line.split()
    
        for word in words:
            word = word.strip()

            for char in word:
                char = char.lower()
                freq[char] = freq.get(char,0) + 1   
                
sorted_freq = dict(sorted(freq.items()))

with open('hw01_output.json', mode='w', encoding='utf-8') as output_file:
    json.dump(sorted_freq, output_file, indent = 4, ensure_ascii=False)