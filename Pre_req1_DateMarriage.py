#Write a program to discover the answer to this puzzle:"Let's say men and women are paid equally (from the same uniform distribution).
# If women date randomly and marry the first man with a higher salary, what fraction of the population will get married?"

import random
repeat = 1000
sumrate=0
for r in range(0, repeat):
    women = list()
    men = list()
    population = 1000
    maxsalary = 1000000
    for i in range(0, population):
        woman = random.randint(1, maxsalary)   # from Uniform distribution
        women.append(woman)
    for j in range(0, population):
        man = random.randint(1, maxsalary)  # from Uniform distribution
        men.append(man)

   # print women
   # print men

    married = 0
    for k in women:
        for h in men:
            if (k<h):     # Woman found a man with a higher salary
                married = married + 1
                men.remove(h)
                #print k, h, men
                break

    rate = married/(population*1.0)
    sumrate = sumrate + rate
averagerate = sumrate/(repeat*1.0)
print "The average marriage rate after repeating ", repeat, " times is ", averagerate


