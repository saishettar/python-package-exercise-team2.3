# Python Package Exercise

## Pypi

[Team2-Virtual-Pet 0.1.0](https://pypi.org/project/Team2-Virtual-Pet/0.1.0/)

![Tests](https://github.com/software-students-fall2026/python-package-exercise-team2.3/actions/workflows/build.yaml/badge.svg)

**This team used an extension**

## Install

You will need python 3.13 or 3.14, and Pipenv to use this package. Run these commands in your terminal to install.

## Use MyVirtualPet

Care for your virtual pet through feeding, resting, playing, and cleaning. Check up on its health to make sure you’re fulfilling all of its needs! Use the menu provided when the file is run to navigate your pet-interaction options.

### Feeding

`feed(pet)` sets hunger to 0 and records a `feed` event with the hunger value before and after. The menu option (3) feed calls it. Hunger of 0 means the pet is full, and 100 means it is starving.

### Rest

`restore_energy(pet)` adds 20 energy and keeps the result at 100 or below. If energy actually changes, it records a `stat` event with the value before and after. The menu option (1) rest calls it. You can pass a different amount, as in `restore_energy(pet, 10)`.

### Playing

`play(pet, name, play_type)` increases their happiness (`happy`). Each play option increases happiness by a different amount, scaling from walk (+5), to catch (+5), to pet (+15). With each interaction that is not playing (like resting, feeding, or cleaning), happiness decreases by 10.

### Cleaning

`clean(pet)` sets hygiene to 100 and records a clean event with the hygiene value before and after. The menu option (4) clean calls it. Hygiene of 100 is fully clean, and 0 is the worst.

### Health

`wellness` calculates overall wellness by averaging energy, hygiene, happiness, and inverse hunger (100 - hunger). `update_health` increases health by 2 when all stats are healthy, or decreases health when wellness falls below 50. Health ranges from 0 to 100, and the pet dies when health reaches 10 or below. `diagnose_pet` identifies health issues, while `recommend_action` suggests the most urgent action to improve the pet's condition.

### Saving/Loading

`save_pet(pet, path)` writes the pet to a JSON file. The file keeps the name, alive, the five stats, the history, and `last_seen`, which is the timestamp used for time passing. `load_pet(path)` reads that file and returns the pet. A missing file raises `FileNotFoundError`. A file that is not valid JSON, or a pet missing its name, `alive`, or a stat, is rejected. In the game, the file is `~/.virtual_pet.json`. The pet is loaded at startup and saved after rest, play, feed, clean, and quit.

### History

`record_event` appends one event to `pet["history"]`. An event is `feed`, `play`, `clean`, or `stat`. Play stores the play type in `detail`. A stat event stores the stat name and the value before and after the change. `get_history(pet, limit)` returns the most recent `limit` events, oldest of that slice first. `limit` of 0 returns an empty list. The returned events are copies, so changing them does not change the stored log. The menu shows the latest events, and they come back after a save and load.

### Death

`check_death` determines whether the pet has died from low health or inactivity. The pet dies when its health reaches 10 or below, or when it has not been opened for 7 days. The function checks the pet's health, alive status, and the time since it was last opened. If either death condition is met, `alive` is set to `False`. The dead pet is displayed in the terminal, and the user is prompted to create a new Tamagotchi. Once a pet dies, it can’t be revived.

## Build and Test

You will need Python 3.13 or 3.14 and Pipenv installed. After downloading or cloning the repository, navigate to the project directory and run the following commands to install dependencies:

```bash
pipenv install --dev
```

Run the virtual pet application:

```bash
pipenv run python -m package.interaction
```

Run all unit tests using pytest:

```bash
pipenv run python -m pytest -v
```

## Team

- [Sienna Maguire](https://github.com/SiennaSSM)
- [Marco Gulino](https://github.com/MarcoHGulino)
- [Sai Shettar](https://github.com/saishettar)
- [Elton Yu](google.com/url?q=https://github.com/elbow74&sa=D&source=docs&ust=1794675275101573&usg=AOvVaw0tdhmdTSazQ4S3R2UEBUix)
