import json
import csv
import os

file = ""
os.system("tcd -v" + file + " -f json")
with open(file+'.json', encoding='utf8') as out:
    chat = json.loads(out.read())
sounds = []
comments = chat["comments"]
for com in comments:
    if "SoundAlerts" in com["commenter"]["display_name"]:
        sounds.append([com["created_at"], com["message"]["body"]])

lerts = []
for s in sounds:
    #my_string.split("world",1)[1] 
    lerts.append(s[1].split("play ",1)[1])
print(lerts)
alerts  = set(lerts)
print(alerts)

for alert in alerts:
    print(lerts.count(alert), alert)
