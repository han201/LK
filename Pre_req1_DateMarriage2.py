#Write a program to discover the answer to this puzzle:"Let's say men and women are paid equally (from the same uniform distribution).
# If women date randomly and marry the first man with a higher salary, what fraction of the population will get married?"
'''
I don't think you can do this analytically- there is a time element where females can continue dating until they find a match.
And once they find a match, they leave the dating pool, and you need to keep track of that.
Eventually though, you are left with a  pool of females with high salaries and a pool of men with low salaries,
and even if this remaining pool continues dating to infinity, they can never find a match.
So the answer is asymptoting to a single value of around 68%.

I realize that my analytical solution is incorrect as it does not
'remove' the matched pair as you pointed out.

BTW, instead of 'randomly choosing one woman and one man' for each
time step, my initial approach was to generate two random arrays of
men and women, and have each woman go on a date with men until she
finds (or does not find) a match. Then I removed the matched man, and
then repeated for the next woman. In this case, the solution is
sensitive to the number of 'population'. As I increase the population,
the proportion of matched couple increases (see my Python code below.
When population is 10, the matching is about 50% with a large
variation. As I increase the population, ,the matching rate goes up to
98%). I actually realized that what I did was the following according
to the link above.

First things first: This is a very politically incorrect question. It degrades women by implying that they only marry for money.
However, it degrades men even more! Per this question, a male's threshold is "does she have a pulse?"

There are ways to rephrase this question that avoid the political incorrectness issue.
For example, let sets X and Y be sets of the same cardinality.
Each set comprises members with two attributes, value, which is drawn from U(0,1), and paired, which is initially false.
By some scheme, we'll pair members of set X and set Y such that for each pair (x,y),
we have x.paired == y.paired == false prior to the pairing and x.value > y.value'. After pairingxandy, thepairedattributes of membersxandyare set totrue`.

The fraction of the population that can be paired depends very much on the algorithm used to match elements of sets X and Y.
This is not a well-phrased question.

Serial-serial matching

Assign random values to the value attribute of each member of set X and pf set Y.
Walk over members yy of set Y. For each such member y, walk over members x of set X until a member is found that satisfies !x.paired && (x.value > y.value).
This member x is then paired with member y. The percentage of the population that is paired by this algorithm is about 97%.

Serial-random matching

Assign random values to the value attribute of each member of set X and pf set Y.
For each pairable member of set Y (a member y of set Y whose value is greater than the maximum value of all unpaired members of set X is not "parable"),
repeatedly randomly select a member of x of the unpaired members of set X until x.value > y.value. This member x is then paired with member y.
The percentage of the population that is paired by this algorithm is about 68%.

Random-serial matching

This is in a sense the inverse of the above algorithm.
Here we repeatedly select a random member y from the unpaired members of set Y.
Then we walk over the elements of set X, in order, until a match is found.
Walking over the end says that y is a old maid is unpairable.
The algorithm stops when the minimum value of set Y is greater than the maximum value of set X.
The percentage of the population that is paired by this algorithm is about 68%, the same as above.

Random-random matching

Randomly select a member y from the unpaired members of set Y and randomly select a member x from the unpaired members of set X.
Pair these two members if x.value > y.value. Keep doing this until there are no pairable members left in the set.
The percentage of the population that is paired by this algorithm is about 68%, the same as above.

Speed dating Speed matching

Basically, this is the above algorithm but in parallel.
Here we randomly pair members from the unpaired members of set Y with unpaired members of set X.
All of these that meet the criterion x.value > y.value are paired, en masse.
The percentage of the population that is paired by this algorithm is about 68%, the same as above.
The performance of this algorithm is anything but that of the above. This algorithm is blazingly fast.

match.com matching Optimal matching

Here we try to match members of set X and set Y that just barely pass the criteria.
Doing this serially barely beats the serial-serial algorithm.
Do this in parallel, and almost every member gets paired with another.
The only ones that don't get paired are the members of set Y that are completely unpairable.

'''

# I will use 'random-random' matching here.

import random
repeat = 10
sumrate=0
for r in range(0, repeat):
    women = list()
    men = list()
    population = 10000
    maxsalary = 100000
    married = 0
    time_limit = 10*population
    for i in range(0, population):
        woman = random.randint(1, maxsalary)   # from Uniform distribution
        women.append(woman)
    for j in range(0, population):
        man = random.randint(1, maxsalary)  # from Uniform distribution
        men.append(man)

    for time in range(0, time_limit):
        # randomly choose a man and a woman
        random_woman = random.randint(0, len(women)-1)
        random_man = random.randint(0, len(men)-1)

        if (women[random_woman]<men[random_man]):
            married = married + 1
           # print women[random_woman], "<", men[random_man], ", married = ", married
            women.remove(women[random_woman])
            men.remove(men[random_man])

    rate = married/(population*1.0)
    sumrate = sumrate + rate
    print "Number of married couples among ", population, ":", married, "with marriage rate", rate
averagerate = sumrate/(repeat*1.0)
print "The average marriage rate after repeating ", repeat, " times is ", averagerate
