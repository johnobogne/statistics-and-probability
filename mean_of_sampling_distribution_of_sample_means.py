import random
import math
import time
from itertools import combinations

def aligner(value) :
    return format(value, '.5f')

def getSampleProbability(frequency, samples, decimals) :
    return float(round((frequency / samples), decimals))

def getSampleMean(sample_mean, calculated_probability, decimals) :
    return float(round(sample_mean * calculated_probability, decimals))

def getSampleVariance(sample_mean, calculated_mean, decimals) :
    return float(round(sample_mean * calculated_mean, decimals))

def getVariance(variances, mean) :
    return round(variances - mean**2, 2)

def getStandardDeviation(var) :
    return round(math.sqrt(var), 2)

def round_to(inp) :
    if inp == '' :
        return 5
    else :
        return int(inp)

#Input
inpObservations = input('Observations (split by space): ')
size = int(input('Sample size: '))
round_to_nearest = round_to(input('Round to: '))

#Processing observations
lstObservations = [item for item in inpObservations.split(' ')]
combination = combinations(lstObservations, size)

#Table of samples and its corresponding mean
number_of_samples = 0
running_total = 0
means = {}
print('\nSamples  |   Mean')
for sample in list(combination) :
    for observation in sample :
        running_total += int(observation)
    running_mean = float(round(running_total / size, 5))
    means[running_mean] = means.get(running_mean, 0) + 1
    print(*sample, '|', aligner(running_mean))
    running_total = 0
    number_of_samples += 1

#Sorting Dictionary
temp_sorted_means = sorted([m for (m, f) in means.items()])
sorted_means_dict = {}
for temp_means in temp_sorted_means :
    sorted_means_dict[temp_means] = sorted_means_dict.get(temp_means, means[temp_means])

#Table of everything
summation_of_probabilities = 0
summation_of_means = 0
summation_of_variances = 0
print('\nMean     |  Freq   |   P(X)  |  X*P()  |  X^2*P(X)')
for (mean, frequency) in sorted_means_dict.items() :

    individual_probability = getSampleProbability(frequency, number_of_samples, round_to_nearest)
    individual_mean = getSampleMean(mean, individual_probability, round_to_nearest)
    individual_variance = getSampleVariance(mean, individual_mean, round_to_nearest)

    #Summations
    summation_of_probabilities += individual_probability
    summation_of_means += individual_mean
    summation_of_variances += individual_variance

    print(
        aligner(mean), '|   ',
        frequency, '   |',
        aligner(individual_probability), '|',
        aligner(individual_mean), '|',
        aligner(individual_variance)
    )

#Extra Calculations
calculated_variance = getVariance(summation_of_variances, summation_of_means)

#Print Results
print('\nNumber of samples:', number_of_samples)
print('Mean of Sampling Distribution:', summation_of_means)
print('Variance of Sampling Distribution:', calculated_variance)
print('Standard Deviation of Sampling Distribution', getStandardDeviation(calculated_variance))
time.sleep(30)
