infile = open("text.txt", 'r')
histogram = { }

for line in infile:

    words = line.split()

    for word in words:
        nb_occurs = histogram.get(word, 0)
        histogram[word] = nb_occurs + 1

infile.close()

words = sorted(histogram.keys())

for word in words:
    print(histogram[word], ": ", word)