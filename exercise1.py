import os
import msvcrt
import random
import json

prepareDuration = 30  # 秒
firstDuration = 10  # 分钟
secondDuration = 5  # 分钟
thirdDuration = 1  # 分钟
restDuration = 1  # 分钟

titleText = 'exercise_1'
descriptionText = (f'{prepareDuration} seconds for prepare, then {firstDuration} min slow, {secondDuration} min '
                   f'middle, {thirdDuration} min fast, and {restDuration} min rest')
duration = (prepareDuration + (firstDuration + secondDuration + thirdDuration + restDuration) * 60) * 1000  # 毫秒
creatorText = 'FunscriptCreator'

metadata = {"title": titleText, "description": descriptionText, "performers": [], "video_url": "", "tags": [],
            "duration": duration, "average_speed": 1, "creator": creatorText}
actions = []


# 生成actions
def add(time, pos):
    actions.append({"at": time, "pos": pos})


def ran(min, max):
    return random.randint(min, max)


t = 0
add(t, 10)
t = prepareDuration * 1000
count = 0
min = 900
max = 1100
tt = (prepareDuration + firstDuration * 60) * 1000
while t < tt:
    t += ran(min, max)
    add(t, ran(57, 63))
    t += ran(min, max)
    count = (count + 1) % 10
    if count == 9:
        add(t, ran(0, 10))
    else:
        add(t, ran(27, 33))

min = 600
max = 800
tt += secondDuration * 60 * 1000
while t < tt:
    t += ran(min, max)
    add(t, ran(67, 73))
    t += ran(min, max)
    add(t, ran(27, 33))
    count = (count + 1) % 10
    if count == 9:
        for i in range(0, random.randint(0, 5)):
            t += ran(260, 330)
            add(t, ran(50, 60))
            t += ran(260, 330)
            add(t, ran(40, 50))

min = 180
max = 230
tt += thirdDuration * 60 * 1000
while t < tt:
    t += ran(min, max)
    add(t, ran(80, 90))
    t += ran(min, max)
    add(t, ran(0, 5))

min = 300
max = 400
tt += restDuration * 60 * 1000
while t < tt:
    t += ran(min, max)
    add(t, ran(0, 8))
    t += ran(min, max)
    add(t, 0)

script = {"metadata": metadata, "actions": actions}
scriptFile = f'{titleText}.funscript'
if os.path.exists(scriptFile):
    os.remove(scriptFile)

scriptStr = json.dumps(script, separators=(',', ':'))
with open(scriptFile, 'w') as f:
    f.write(scriptStr)

print('success')
msvcrt.getch()
