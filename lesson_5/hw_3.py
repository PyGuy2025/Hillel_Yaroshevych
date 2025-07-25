from string import punctuation


users_hash = input("Enter your hashtag: ").title()
symbols = punctuation + ' '

for _ in symbols:
    users_hash = users_hash.replace(_, '')

if len(users_hash) < 140:
    print(f"Your hashtag is #{users_hash}")
else:
    print(f"Your hashtag is #{users_hash[:139]}")