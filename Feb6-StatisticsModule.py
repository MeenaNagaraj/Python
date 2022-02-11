#Statistics Module
#used to calculate mathematical statistics of numeric data.
import statistics

#mean, median and mode are the 3 commonly used measures of central tendancy
#mean - Add all the numbers then divide by the amount of numbers
#median - order the set of numbers,the median is the middle number
#mode - the most common number

#1.statistics.mean() Method - statistics.mean() Method
print(statistics.mean([1,2,3,4,5,6]))   #o/p:3.5

#2.statistics.median() Method - Calculate the median (middle value) of the given data
#sorts the data in ascending order before calculating the median
print(statistics.median([1, 3, 5, 7, 9, 11, 13]))   #o/p: 7
print(statistics.median([13,1,11,3,9,5,7]))         #o/p:7
print(statistics.median([1, 3, 5, 7, 9, 11]))       #o/p:6.0

#3.statistics.median_high() Method - Calculate the high median (middle value) of the given data
#sorts the data in ascending order before calculating the median
print(statistics.median_high([1,3,5,7,9,11]))   #o/p:7

#4.statistics.median_low() Method -Calculate the low median (middle value) of the given data
print(statistics.median_low([1,3,5,7,9,11]))    #o/p:5

#5.statistics.mode() Method - calculate the mode of the given numeric or nominal data se
print(statistics.mode([1,3,3,3,5,7,7,9]))   #o/p:3

#6.statistics.stdev() Method - calculate the statndard deviation of the given data
print(statistics.stdev([1,3,5,7,9,11]))     #o/p:3.7416573867739413

#7.statistics.pstdev() Method -calculate the standard deviation from an enitre population
print(statistics.pstdev([1,3,5,7,9,11]))    #o/p:3.415650255319866

#8.statistics.pvariance() Method - calculates the variance of an entire population
print(statistics.pvariance([1,3,5,7,9,11]))     #o/p:11.666666666666666

#9.statistics.variance() Method - calculates the variance from a sample data
print(statistics.variance([1,3,5,7,9,11]))      #o/p:14

#10.statistics.median_grouped() Method - calculate the median of grouped continuous dta
print(statistics.median_grouped([1,2,3,4]))      #o/p:2.5




