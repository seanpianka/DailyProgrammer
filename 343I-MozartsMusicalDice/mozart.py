import math
import random


with open('mozart-dice-table.txt') as f:
    table = [list(map(int, l.strip().split())) for l in f.readlines()]


def normalize_measures(measures, beats_per_measure):
    for i in range(len(measures)): # each measure of 3 beats
        shift = measures[i][0][1]

        for j in range(len(measures[i])): # each beat within the measure
            measures[i][j][1] = measures[i][j][1] - shift + (i * beats_per_measure)

    return measures


def select_measures(measures, measure_count):
    selected_measures = []

    for i in range(measure_count):
        dice_roll = random.randint(1, 6) + random.randint(1, 6)
        selected_measures.append(measures[table[i][dice_roll - 2] - 1])

    return selected_measures


def mozart_diceroll(beats, measure_count, beats_per_measure):
    total_measures = math.ceil(beats[-1][1]) / beats_per_measure

    measures = []
    measure = []
    i = 0

    for i in range(len(beats)):
        if beats[i][1] < (len(measures) + 1) * beats_per_measure:
            measure.append(beats[i])
        else:
            measures.append(measure)
            measure = []
    measures.append(measure)

    selected_measures = select_measures(measures, measure_count)
    normalized_measures = normalize_measures(selected_measures, beats_per_measure)

    return [beat for measure in normalized_measures for beat in measure]


if __name__ == '__main__':
    with open('mozart-dice-starting.txt') as f:
        beats = [[float(x) if x.replace('.', '', 1).isdigit() else x for x in beat.strip().split()] for beat in f.readlines()]

    new_beats = mozart_diceroll(beats, 16, 3)
    print('\n'.join([' '.join(list(map(str, b))) for b in new_beats]))
