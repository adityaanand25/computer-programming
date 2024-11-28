#Write a program to find the key associated with the minimum value in a dictionary.
python

scores = {'Alice': 85, 'Bob': 78, 'Charlie': 90}
min_score_key = min(scores, key=scores.get)
print(min_score_key)
