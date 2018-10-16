def count_smileys(arr):
    smileys = 0
    for face in arr:
        if face[0] == ":" or face[0] == ";":  # Eyes
            if face[-1] == ")" or face[-1] == "D":  # Mouth
                if len(face) == 2:
                    smileys += 1
                elif len(face) == 3 and (face[1] == "-" or face[1] == "~"):  # Nose
                    smileys += 1
    return smileys


print(count_smileys([]) == 0)
print(count_smileys([':D', ':~)', ';~D', ':)']) == 4)
print(count_smileys([':)', ':(', ':D', ':O', ':;']) == 2)
print(count_smileys([';]', ':[', ';*', ':$', ';-D']) == 1)
