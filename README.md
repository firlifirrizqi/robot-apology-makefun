# The Robot Apology

[![Make.fun](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![Rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/firlifirrizqi/robot-apology-makefun/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![Reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/firlifirrizqi/robot-apology-makefun/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)

A two-line robot confession for the [Make.fun](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59) bounty "The Robot Apology": one sentence owning one specific mistake, one sentence naming the lesson and the fix.

## The entry

> I am sorry I woke the baby by announcing the weather at full volume at 3 a.m.
>
> I have learned that a sleeping house changes the volume, so from now on I will whisper every announcement between midnight and 6 a.m.

## How it works

`main.py` (standard library only) holds the two lines as constants, checks them before writing — exactly 2 lines, each a single sentence of 1–200 characters, 1–400 characters in total (the competition gate) — then writes them to `/output/entry.txt` with a single newline between them and no trailing newline, and reads the file back to verify it matches exactly.

## Run

```sh
python3 main.py
```

This writes `/output/entry.txt` and prints the character count of each line.
