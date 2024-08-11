# Offset static address finder for DS Memory dumps/Action replay code

This program basically finds the pointer address which points to the offset address to use for Action Reply codes. i.e. the address you use with the BXXXXXXX 00000000 command. [Here](https://doc.kodewerx.org/hacking_nds.html#arcodetypes) for more info.
I mainly used this for desume but should also work with Cheat engine, so long as you can dump the whole memory into a file.

Tqdm option is avaliable as well, if u want a progress bar to look cool :P

## Usage
1. find interested memory address and record this down (example: memory address that stores player step number or calculator value in pokemon platinum, something like 0x0227F30C)

2. dump 1st memory file (desume: tools -> view memory -> dump all.)

3. restart game (Desume savestates do not work. so manually reload the rom and load a save file)

4. repeat step 1 to 3 until you have about 3 or more memory files. The more dumps u have the more accurate the results will be, probably.

5. calculate the difference between each subsequent dump memory address with the memory address recorded for dump 1. record this difference in decimal (base-10) (meaning if your 1st dump is 0x0227F30C and second dump is 0x0227F32C, dump2 - dump1 =0x00000020 = 32 (base-10). so dump2Diff is 32) if you get a negative value, just absolute the value to get a positive number. Then record dump3-dump1, dump4-dump1 so on so forth.

6. run this program

```python FindOffSetPointerAddr.py path/to/dump1 path/to/dump2 dump2Diff path/to/dump3 dump3Diff ...```

7. Possible static pointer addresses will be in red and inbetween []. Use this value for the BXXXXXXX command in Action replay. If the first address causes issues, then test the next ones until you find one that works.

## Credits
anon20345823 [Reddit post](https://www.reddit.com/r/learnprogramming/comments/6kqbcr/making_an_action_replay_code/): For inspiration to remake what his program probably did. His link to his program is dead as of 11-aug-24, which prompted me to make this program. Also i have no affiliation with him whatsoever.

## License
![Alt text](./CC0.svg "a title")
Program is provided as is.
