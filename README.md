# scavenger-hunt

## How to Play
* Have three or more people on a video call via fixed video - two participants and at least one judge.
* Before the call, the judge should run this script to generate a randomized scavenger hunt list for the participants.
* To start the game in the video call, the judge will screen share the scavenger hunt list to the two participants.
* As soon as the scavenger hunt list is shared, the two participants are trying to collect as many items from the list as possible as quickly as possible.
* The two participants should have a _second_ mobile device n the video call that they will carry with them wile participating in the scavenger hunt (for entertainment reasons).
* The participants must bring the item to the fix video location to show the judge the item.
* The winner is the participant that collects as many items as possible from their scavenger hunt list the fastest.
* Inspired by the Bon Appétit Scavenger Hunt: https://www.youtube.com/watch?v=CE3OutlMcfM

## Setup
* To setup the project, run:
```bash
source ./setup.sh
```

## Testing
* To test the project, run:
```bash
python -m pytest -vv ./tests/*_tests.py
```

## Running
* To execute the script, run:
```bash
python scavenger_hunt.py
```

* The output HTML file will be written to the `/output` directory with your specified file name. 