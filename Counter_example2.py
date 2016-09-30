from collections import Counter
# example
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print cnt

fhand = raw_input('Enter a file name: \n')

try:
    with open(fhand) as fopen:
        counts = dict()
        count2 = Counter()
        for line in fopen:
            line = line.rstrip()
            if line.startswith('From'):
            # print line
                words = line.split()
            # print words2
                if len(words)>2:
                    counts[words[1]]=counts.get(words[1], 0) + 1
                    count2[words[1]] += 1
        print counts
        print count2

except:
    print 'Invalid file name'
    exit()

