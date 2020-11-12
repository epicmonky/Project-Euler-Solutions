# Using names.txt, begin by sorting it into alphabetical order. Then work out the alphabetical value for each name,
# multiply this value by its alphabetical position to obtain a name score.
# For example, COLIN is worth 3 + 15 + 12 + 9 + 14 = 53 and it is the 938th name, so COLIN has score 938 x 53 = 49714.

# What is the total of all the name scores in the file?


# Gets score of name
def name_score(name):
    score = 0
    for i in range(len(name)):
        score += ord(name[i]) - 64
    return score


if __name__ == '__main__':
    total_score = 0

    f = open("data/p022_names.txt")
    names = f.read()
    name_list = names.split(',')
    for i in range(len(name_list)):
        name_list[i] = name_list[i].strip('"')
    sorted_names = sorted(name_list)

    for i in range(len(sorted_names)):
        total_score += (i + 1) * name_score(sorted_names[i])
    print(total_score)
    f.close()
