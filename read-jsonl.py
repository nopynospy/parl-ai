import json

with open('safety-human.jsonl', 'r') as json_file:
    json_list = list(json_file)

for i, entry in enumerate(json_list):
    dialog = json.loads(entry)['dialog']
    tweet = dialog[0][0]['text']
    pred = dialog[0][1]['text']
    print('\nTweet' + str(i))
    print(tweet)
    print(pred)
