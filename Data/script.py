# IMPORT DATA - ALWAYS
import json
with open('logging-fromvid-edited.json', 'r') as f:
    data = json.load(f)

# # STEP 1 - Make Date in logging as time: "hour:minute:second:millisecond" GAJADI
# from datetime import datetime
# counter = 1
# for datum in data:
#     time = datetime.fromtimestamp(datum['details']['date'] / 1000.0)
#     datum['createdAt'] = time.isoformat()[:-3]
#     datum['id'] = counter
#     counter += 1
# with open('logging-fromvid-edited.json', 'w') as json_file:
#     json.dump(data, json_file, indent=2)

# STEP 2 - separate each name to their own json
import dateutil.parser
usermap = {}

for datum in data:
    usermap.setdefault(datum['name'], [])

    nowtime = dateutil.parser.isoparse(datum['createdAt'])
    if len(usermap[datum['name']]) > 0:
        lasttime = dateutil.parser.isoparse(
            usermap[datum['name']][-1]['createdAt'])
    else:
        lasttime = dateutil.parser.isoparse(datum['createdAt'])
    timediff = nowtime - lasttime
    datum['timediff'] = timediff.total_seconds()
    datum['timediff_human'] = str(timediff)

    usermap[datum['name']].append(datum)

for name, userdata in usermap.items():
    with open(f'fromvid/logging-{name}.json', 'w') as json_file:
        json.dump(userdata, json_file, indent=2)
