# 'Data Analysis.py' | Anastasia Bolotnikova | 16.05.14

import matplotlib.pyplot as plt
import numpy as np

def rm_anova(dec_rule, test_data, alf = 0.05):

    # s - Number of factors (test subjects)
    s = len(test_data)

    # a - Number of levels (conditions)
    a = len(test_data[0])

    # Number of measurments
    N = s*a

    # Calculate Degrees of Freedom

    DF_between = a-1

    DF_within = N-a

    DF_subjects = s-1

    DF_error = DF_within - DF_subjects

    DF_total = N-1


    # Calculate Sums of Squares

    sumsOfLevels = [0]*a

    for el in test_data:
        for i in range(a):
            sumsOfLevels[i] += el[i]

    sumOfAllLev = sum(sumsOfLevels)

    SS = sum([el**2 for el in sumsOfLevels])

    SS_between = SS/s - (sumOfAllLev)**2/N


    sumOfSquares  = 0

    for el in test_data:
        sumOfSquares += sum(subEl**2 for subEl in el)
        

    SS_within = sumOfSquares - (SS)/s


    sumOfsumsOfSqaredLevels  = 0

    for el in test_data:
        sumOfsumsOfSqaredLevels += sum(el)**2
        
    SS_subjects = sumOfsumsOfSqaredLevels/a - (sumOfAllLev)**2/N


    SS_error = SS_within - SS_subjects

    SS_total = SS_between + SS_within


    # Calculate Meaned Squares

    MS_between = SS_between/DF_between

    MS_error = SS_error/DF_error

    # Calculate F value

    F = MS_between/MS_error
    

    # ANOVA Tabel
    table = '\t\tSS\t\tdf\t\tMS\t\tF\nBetween\t\t'+str(round(SS_between,2))+'\t\t'+str(round(DF_between,2))+'\t\t'+str(round(MS_between,2))+'\t\t'+str(round(F,2))+ \
            '\nWihtin\t\t'+str(round(SS_within,2))+'\t\t'+str(round(DF_within,2))+'\t\t'+ \
            '\n-Subjects\t'+str(round(SS_subjects,2))+'\t\t'+str(round(DF_subjects,2))+ \
            '\n-Error\t\t'+str(round(SS_error,2))+'\t\t'+str(round(DF_error,2))+'\t\t'+str(round(MS_error,2))+ \
            '\nTotal\t\t'+str(round(SS_total,2))+'\t\t'+str(round(DF_total,2))+'\n\n'

    
    # Define Hypotheses

    null_hyp = 'Mean values under all '+str(a)+' conditions are equal'
    alternative_hyp = 'The '+str(a)+' contidions differ significantly on time values, F('+str(DF_between)+', '+str(DF_error)+') = '+str(round(F,2))+', p<'+str(alf)+'\n'
    

    # If F is grather than the value of decision rule, reject the null hypotheses

    if(F>dec_rule):
        return alternative_hyp, table
    else:
        return null_hyp, table


def rm_tukey_HSD(test_data, q_value, MS_error):

    s = len(test_data)
    a = len(test_data[0])

    HSD = q_value*(MS_error/s)**(1/2)
    
    sumsOfLevels = [0]*a

    for el in test_data:
        for i in range(a):
            sumsOfLevels[i] += el[i]

    meansOfLevels = [el/s for el in sumsOfLevels]
    diff_groups = []

    for i in range(len(meansOfLevels)-1):
        for j in range(i,len(meansOfLevels)):
            diff = abs(meansOfLevels[i]-meansOfLevels[j])
            if(diff>HSD):
                diff_groups.append([i,j,round(diff,2)])

    result = ['Difference between groups '+str(el[0]+1)+' and '+str(el[1]+1)+\
              ' is significant and equal to '+str(el[2])+'(HSD:'+str(round(HSD,2))+')\n' for el in diff_groups]

          
    return ''.join(result)

def get_group_means(test_data):
    
    s = len(test_data)
    a = len(test_data[0])
    
    sumsOfLevels = [0]*a

    for el in test_data:
        for i in range(a):
            sumsOfLevels[i] += el[i]

    meansOfLevels = [el/s for el in sumsOfLevels]

    return meansOfLevels
    

# Print Results

def print_ANOVA_and_Tukey():

    print('---BLURRINESS IMPACT---')
    print(rm_anova(dec_rule, test_data_BLUR, alf = 0.05)[0])
    print(rm_anova(dec_rule, test_data_BLUR, alf = 0.05)[1])
    print(rm_tukey_HSD(test_data_BLUR, q, 2.03))

    print('---SIZE IMPACT---')
    print(rm_anova(dec_rule, test_data_SIZE, alf = 0.05)[0])
    print(rm_anova(dec_rule, test_data_SIZE, alf = 0.05)[1])
    print(rm_tukey_HSD(test_data_SIZE, q, 3.14))

    print('---DISTANCE IMPACT---')
    print(rm_anova(dec_rule, test_data_DIST, alf = 0.05)[0])
    print(rm_anova(dec_rule, test_data_DIST, alf = 0.05)[1])
    print(rm_tukey_HSD(test_data_DIST, q, 2.13))



# Plot Blurriness
def plot_BLUR(levels, MEANS_BLUR):
    plt.plot(levels,MEANS_BLUR,'--bH')
    plt.xlabel('Blurriness',fontsize=18)
    plt.ylabel('Time (sec)',fontsize=18)
    plt.xticks(np.arange(0, 40, 10))
    plt.xlim(0,40)
    plt.ylim(0,12)
    plt.show()


# Size
def plot_SIZE(levels, MEANS_SIZE):
    plt.plot(levels,MEANS_SIZE,'--bH')
    plt.xlabel('Size',fontsize=18)
    plt.ylabel('Time (sec)',fontsize=18)
    plt.xticks(np.arange(0, 40, 10))
    plt.xlim(0,40)
    plt.ylim(0,12)
    plt.show()


# Distance
def plot_DIST(levels, MEANS_DIST):
    plt.plot(levels,MEANS_DIST,'--bH')
    plt.xlabel('Distance',fontsize=18)
    plt.ylabel('Time (sec)',fontsize=18)
    plt.xticks(np.arange(40, 230, 60))
    plt.xlim(90,230)
    plt.ylim(0,12)
    plt.show()


# test_data_X - Test Data matrix levels*factors

test_data_BLUR = []

test_data_SIZE = []

test_data_DIST = []


f = open('test data.txt')

f.readline()

for line in f:
    parameters = line.split(';')
    test_data_BLUR.append(parameters[0].split())
    test_data_SIZE.append(parameters[1].split())
    test_data_DIST.append(parameters[2].split())

test_data_BLUR = [[int(time)/1000 for time in el] for el in test_data_BLUR]
test_data_SIZE = [[int(time)/1000 for time in el] for el in test_data_SIZE]
test_data_DIST = [[int(time)/1000 for time in el] for el in test_data_DIST]


# dec_rule - Decision Rule

## calculate decision rule for yuor DF_between, DF_error and alpha (p) values:
## http://www.danielsoper.com/statcalc3/calc.aspx?id=4

dec_rule = 3.73889183

# q - critical value of 'q' statistics

## look up q-value for your number of groups(a), DF_error and alpha:
## http://www.real-statistics.com/statistics-tables/studentized-range-q-table

q = 3.701

MEANS_BLUR = get_group_means(test_data_BLUR)
MEANS_SIZE = get_group_means(test_data_SIZE)
MEANS_DIST = get_group_means(test_data_DIST)

    

print_ANOVA_and_Tukey()

plot_BLUR([10,20,30],MEANS_BLUR)
plot_SIZE([10,20,30],MEANS_SIZE)
plot_DIST([100,160,220],MEANS_DIST)










