import json

data = json.load(open("correctResults.json"))
prop = "got_BN_dice"

print("label,rank,correct")

for result in data:
    expected = result["expected"]
    if(expected == result[prop]["iso"] or 
       ("ISO_639:" + expected) in result[prop]["iso"]):
        correct = 1
    else:
        correct = 0
    print("%s,%s,%s" % (result["input"], result[prop]["rank"], correct))
