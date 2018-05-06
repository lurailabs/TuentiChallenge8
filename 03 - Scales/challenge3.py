#!/usr/bin/env python3

INPUT_FILE = 'submitInput.txt'
OUTPUT_FILE = 'submitOutput.txt'

notes = [('C', 'B#'), ('C#', 'Db'), 'D', ('D#', 'Eb'), ('E', 'Fb'), ('F', 'E#'), ('F#', 'Gb'),
         'G', ('G#', 'Ab'), 'A', ('A#', 'Bb'), ('B', 'Cb')]
major_scale_steps = [2, 2, 1, 2, 2, 2, 1] #steps in semitones
minor_scale_steps = [2, 1, 2, 2, 1, 2, 2] #steps in semitones
inputs = []

def create_scales(steps):
    all_scales = {}
    for note in notes:
        index = notes.index(note)
        scale = [note]
        for step in steps:
            index = (index + step) % len(notes)
            scale.append(notes[index])
        del scale[-1]
        all_scales[note] = scale
    return all_scales


def check(melody, scales):
    set1 = set(melody)
    results = []
    for key, values in scales.items():
        set2 = set([item for sublist in values for item in sublist]) # lista aplanada
        if set1.issubset(set2):
            if isinstance(key, tuple):
                results.append(key[0])
            else:
                results.append(key)

    results.sort()
    return results


with open(INPUT_FILE, 'r') as f:
    cases = int(f.readline())
    lines = f.readlines()

    position = 0
    while position < len(lines):
        num_notes = lines[position].rstrip('\n')
        if num_notes != '0':
            inputs.append(lines[position+1].split())
            position += 2
        else:
            inputs.append([])
            position += 1

with open(OUTPUT_FILE, 'w') as f:
    newLine = ''
    for case in range(len(inputs)):
        major_scales_coincidences = list(map(lambda x: 'M' + x, check(inputs[case], create_scales(major_scale_steps))))
        minor_scales_coincidences = list(map(lambda x: 'm' + x, check(inputs[case], create_scales(minor_scale_steps))))
        all_coincidences = major_scales_coincidences + minor_scales_coincidences
        if not all_coincidences:
            final_result = 'None'
        else:
            final_result = ' '.join(all_coincidences)

        print(newLine + 'Case #' + str(case + 1) + ': ' + final_result)
        f.write(newLine + 'Case #' + str(case + 1) + ': '  + final_result)
        newLine = '\n'



			
