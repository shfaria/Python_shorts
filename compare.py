import pandas as pd

# day1 = pd.read_csv("/Users/shfaria/Downloads/Training on On Premises Video Conferencing -Recap Quiz on Day 1-grades.csv")
# day2 = pd.read_csv("/Users/shfaria/Downloads/Training on On Premises Video Conferencing -Recap Quiz on Day 2-grades.csv")
day = pd.read_csv("/Users/shfaria/Documents/belisac-grade-compare-test.csv")
day5 = pd.read_csv("/Users/shfaria/Downloads/Training on On Premises Video Conferencing -Day 5 Quiz-grades.csv")


mergedata = day.merge(day5, how = 'outer', on='Email address')


mergedata.to_csv("/Users/shfaria/Documents/final-belisac-grade-compare-test.csv", index=False)
            
            

    