from string import punctuation


users_hash = input("Enter your hashtag: ")
symbols = punctuation

for char in symbols:
    users_hash = users_hash.replace(char, '')

done_hash = users_hash.title().replace(' ', '')

print(f"Your hashtag is #{done_hash[:139]}")