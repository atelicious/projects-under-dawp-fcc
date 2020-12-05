#This is my solution to the Demographic Data Analyzer Problem in FCC's Data Analysis with Python.
#You can view the original question and my repl solution @ https://repl.it/@atelicious/FCC-demographic-data-analyzer


import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    men_df = df[df['sex'] == 'Male'] #lets create a dataframe with only men in sex column
    men_age = men_df['age'].mean() #then filter it into a series and apply the .mean() method
    average_age_men = round((men_age), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors = df['education'].value_counts()
    raw_bach_percentage = bachelors['Bachelors'] * 100 /bachelors.sum()
    percentage_bachelors = round(raw_bach_percentage, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    #lets create the filter first for that satisfies the condition education > Bachelors

    higher_education_filter = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')

    #then create a series with this filter and use the method .sum() to get the number of rows that returns True in our filter 
    higher_education = pd.Series(higher_education_filter).sum()

    #lets create the filter first for that satisfies the condition education < Bachelors
    lower_education_filter = (df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')

    #then create a series with this filter and use the method .sum() to get the number of rows that returns True in our filter 
    lower_education = pd.Series(lower_education_filter).sum()

    # percentage with salary >50K
    #lets create a filter using the filter above combined with the new filter >50K
    higher_education_above_filter = higher_education_filter & (df['salary'] == '>50K')
    higher_education_above = pd.Series(higher_education_above_filter).sum()
    raw_high_educ_percentage = higher_education_above * 100/ higher_education
    higher_education_rich = round(raw_high_educ_percentage, 1)

    higher_education_below_filter = lower_education_filter & (df['salary'] == '>50K')
    higher_education_below = pd.Series(higher_education_below_filter).sum()
    raw_low_educ_percentage = higher_education_below * 100/ lower_education
    lower_education_rich = round(raw_low_educ_percentage, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_total = (df['hours-per-week'] == min_work_hours).sum()
    min_work_filter = (df['salary'] == '>50K') & (df['hours-per-week'] == min_work_hours)
    count_min_work = pd.Series(min_work_filter).sum()
    raw_count_percentage = count_min_work * 100 / min_total
    rich_percentage = round(raw_count_percentage, 1)

    # What country has the highest percentage of people that earn >50K?
    #lets create a dataframe with >50k values only

    df_above_50k = df[df['salary'] == '>50K']

    #then create a series that contains the list of countries with corresponding numbers
    country_pop_50k = df_above_50k['native-country'].value_counts() 
    country_total_pop = df['native-country'].value_counts()

    #then divide both series
    pop_comparison = country_pop_50k  / country_total_pop

    # .idxmax() will return the index of the maximum value of the series
    highest_earning_country = pop_comparison.idxmax()
    highest_earning_country_percentage = round(pop_comparison.max()*100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    #lets create first a df with both india and >50k filter
    india_filter = (df['native-country'] == 'India') & (df['salary'] == '>50K')
    india_50k_df = df[india_filter]
    occupation_series = india_50k_df['occupation'].value_counts()


    top_IN_occupation = occupation_series.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
