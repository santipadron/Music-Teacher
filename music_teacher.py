import random

##VARIABLES##

#NOTES#
notes_1 = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C#', 'Cb', 'D#', 'Db', 'E#', 'Eb', 'F#', 'Fb', 'G#', 'Gb', 'A#', 'Ab', 'B#', 'Bb']

#CHORDS#
chord_type = [" ", "min", "aug", "°", "sus4", "b5", "maj7", "7", "6", "min(maj7)", "min7", "min6", "min7(b5)", "°7", "maj7(#5)", "7(#5)", "7sus", "maj7(b5)", "7(b5)"]
inversion_triad = [" ", "1st inversion", "2nd inversion"]
inversion_tetrad = [" ", "1st inversion", "2nd inversion", "3rd inversion"]

#SCALES AND MODES#
scales_modes = ["major", "natural minor", "harmonic minor", "melodic minor", "dorien", "phrygien", "lydien", "mixolydien", "eolien", "locrien", "pentatonic major", "pentatonic minor", "blues"]


##RANDOMISERS##

#CHORD GENERATOR#
def chord_generator():
    note = random.choice(notes_1)
    ctype = random.choice(chord_type)
    for i in ctype:
        if i == "7" or "6":
            inv = random.choice(inversion_tetrad)
        else:
            inv = random.choice(inversion_triad)
    print(note + ctype + " " + inv + "\n")
        
#SCALE/MODE GENERATOR#
def scale_generator():
    notes = random.choice(notes_1)
    stype = random.choice(scales_modes)
    print(notes + " " + stype + "\n")

#REAL BOOK STANDARD GENERATOR#
line = random.choice(open('book.txt', encoding="utf-8").readlines())

##CHOICE##
choice = input("What do you wish to practice? ('c' for chords; 's' for scales/modes; 'js' for a jazz standard)\n")

if choice == "c":
    print(" ")
    for i in range(10):
        chord_generator()
elif choice == "s":
    print(" ")
    for i in range(10):
        scale_generator()
elif choice == "js":
    print(line)
else:
    print("\nIncorrect input")