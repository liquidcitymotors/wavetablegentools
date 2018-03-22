# tool to generate scale code for the pll via

import numpy as np

import math

import csv

#initialize lists to parse the csv
ratio_subset = []
ratio_table = []
interval_subset = []
interval_table = []
scale_tags = []


scale_name = "harmSubharm"

is_1voct = 0;


#parse the csv for integer ratios and calculate an interval in terms of octaves
with open(scale_name + ".csv", newline="\n") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if row[0] != "":
            if row[1] == "":
                scale_tags.append(row[0])
                print(row[0])
            else:
                ratio = [int(row[0]), int(row[1])]
                ratio_subset.append(ratio)
                interval_subset.append(math.log(float(ratio[0]/ratio[1]), 2))

        elif ratio_subset != []:
            ratio_table.append(ratio_subset)
            ratio_subset = []
            interval_table.append(interval_subset)
            interval_subset = []

#Calculate octave bin for each interval in each scale and append to the first table

print(len(ratio_table))
print(len(interval_subset))

row_pointer = 0
octave_spans = []

for i in interval_table:

    octave_checker_positive = -8

    while max(interval_table[row_pointer]) > octave_checker_positive:

        octave_checker_positive = octave_checker_positive + 1

    octave_checker_negative = 8

    while min(interval_table[row_pointer]) < octave_checker_negative:

        octave_checker_negative = octave_checker_negative - 1

    octave_checker = octave_checker_positive - octave_checker_negative

    interval_pointer = 0

    for j in interval_table[row_pointer]:

        ratio_table[row_pointer][interval_pointer].append(int(12*interval_table[row_pointer][interval_pointer]))
        interval_pointer = interval_pointer + 1

    ratio_table[row_pointer].sort(key=lambda x: int(x[2]))

    octave_spans.append(octave_checker)
    row_pointer = row_pointer + 1


print(interval_table)
print(ratio_table)
print(scale_tags)
print(octave_spans)

num_scales = len(scale_tags)

#get start and end indices for each scale in the n octave tile of best fit

start_end_table = []
start_end_subset = []

for i in ratio_table:

    row_pointer = ratio_table.index(i)

    lower_bound = 8

    while (min(interval_table[row_pointer])) < lower_bound:

        lower_bound = lower_bound - 1

    pad = -lower_bound*12

    for j in ratio_table[row_pointer]:

            interval_pointer = ratio_table[row_pointer].index(j)

            if interval_pointer == 0:

                start = 0;
                end = pad + int((ratio_table[row_pointer][interval_pointer][2] + ratio_table[row_pointer][interval_pointer + 1][2])/2)
                start_end_subset.append([start, end])

            elif interval_pointer != (len(ratio_table[row_pointer]) - 1):

                start = start_end_subset[interval_pointer - 1][1] + 1;
                end = pad + int((ratio_table[row_pointer][interval_pointer][2] + ratio_table[row_pointer][interval_pointer + 1][2])/2)
                start_end_subset.append([start, end])

            else:

                start = start_end_subset[interval_pointer - 1][1] + 1;
                end = octave_spans[row_pointer]*12 - 1
                start_end_subset.append([start, end])

    start_end_table.append(start_end_subset)
    start_end_subset = []


print(start_end_table)

# generate the n octave sized tile for each row using the indices from above

subtile = []
tiles = []

for i in ratio_table:

    row_pointer = ratio_table.index(i)

    for j in ratio_table[row_pointer]:

        interval_pointer = ratio_table[row_pointer].index(j)

        starting_index = start_end_table[row_pointer][interval_pointer][0]

        last_index = start_end_table[row_pointer][interval_pointer][1]

        idx = starting_index

        while idx <= last_index:

            subtile.append(tuple(ratio_table[row_pointer][interval_pointer][0:2]))
            idx += 1;


    tiles.append(subtile)

    subtile = []

print(tiles)

full_scale = []
full_row = []
pitch_class_set = set([])

for i in tiles:

    row_pointer = tiles.index(i)

    j = 0
    
    while j < 64:
        
        octave = int(j // len(i)) * octave_spans[row_pointer]

        numerator_int = int(tiles[row_pointer][j % len(i)][0])
        
        denominator_int = int(tiles[row_pointer][j % len(i)][1])
        
        temp_numerator = numerator_int * 2 ** octave
        
        divisor = math.gcd(int(temp_numerator), int(denominator_int))
        
        fundamental_divisor = int(denominator_int / divisor)
        
        ratio_tag = "ratio" + str(temp_numerator) + "_" + str(denominator_int)
            
        fix32_calculation = int(temp_numerator * 2**48/denominator_int)
    
        integer_part = fix32_calculation >> 32
    
        fractional_part = fix32_calculation - (integer_part << 32)

        ratio_holder = (ratio_tag, integer_part, fractional_part, fundamental_divisor)
        
        if ratio_holder not in pitch_class_set:
            pitch_class_set.add(ratio_holder)

        full_row.append(ratio_holder)

        j += 1
    
    j = 63

    while j >= 0:
        octave = abs((j-64) // len(i)) * octave_spans[row_pointer]

        numerator_int = int(tiles[row_pointer][(len(i) - (64 - j)) % len(i)][0])

        denominator_int = int(tiles[row_pointer][(len(i) - (64 - j)) % len(i)][1])

        temp_denominator = denominator_int * 2 ** octave

        divisor = math.gcd(int(numerator_int), int(temp_denominator))

        fundamental_divisor = int(temp_denominator / divisor)

        ratio_tag = "ratio" + str(numerator_int) + "_" + str(temp_denominator)

        fix32_calculation = int(numerator_int*2**48 / temp_denominator)

        integer_part = fix32_calculation >> 32

        fractional_part = fix32_calculation - (integer_part << 32)

        ratio_holder = (ratio_tag, integer_part, fractional_part, fundamental_divisor)

        full_row.insert(0, ratio_holder)

        j -= 1
        
        if ratio_holder not in pitch_class_set:
            pitch_class_set.add(ratio_holder)

    full_scale.append(full_row)
    full_row = []


text_file = open(scale_name + ".txt", "a")
text_file.truncate()

#####################

text_file.write("const ScaleNote *" + scale_name + "[8];\n\n")

for i in pitch_class_set:
    ratio_tag = i[0]
    integer_part = i[1]
    fractional_part = i[2]
    fundamental_divisor = i[3]
    text_file.write("#define " + ratio_tag + " {" + str(integer_part) + ", " + str(fractional_part) + ", " + str(fundamental_divisor) + "}\n")

print(len(pitch_class_set))

print(len(full_scale[0]))

text_file.write("\n\n\n")

for i in range(0,num_scales):

    for j in range(0, 128):

        ratio_tag = str(full_scale[i][j][0])

        if j == 0:
            text_file.write("const ScaleNote " + scale_tags[i] + "[128] = {" + ratio_tag + ", ")
        elif j != 127:
            if j%12 != 0:
                text_file.write(ratio_tag + ", ")
            else:
                text_file.write(ratio_tag + ", \n")
        else:
            text_file.write(ratio_tag + "}; \n\n")

text_file.write("\n\n\n")

for i in range(len(scale_tags)):

    if i == 0:
        text_file.write("const ScaleNote *" + scale_name + "[8] = {" + scale_tags[i] + ", ")
    elif i != (len(scale_tags) - 1):
        text_file.write(scale_tags[i] + ", ")
    else:
        text_file.write(scale_tags[i] + "}; \n\n")






    


