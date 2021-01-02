import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    #print(df.count())

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    mask_male = df['sex'] == 'Male'
    average_age_men = round(df[mask_male]['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelor_per = df['education'].value_counts(normalize= True).reset_index()
    percentage_bachelors = round(bachelor_per[bachelor_per['index'] == 'Bachelors']['education'].values[0]*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    mask_adv_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    #& (df['salary'] == '>50K'

    higher_education = df[mask_adv_education]['salary'].value_counts(normalize= True).reset_index()
    lower_education = df[~mask_adv_education]['salary'].value_counts(normalize= True).reset_index()

    # percentage with salary >50K
    higher_education_rich = round(higher_education[higher_education['index'] == '>50K']['salary'].values[0]*100, 1)
    lower_education_rich = round(lower_education[lower_education['index'] == '>50K']['salary'].values[0]*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == df['hours-per-week'].min()]['salary'].value_counts(normalize= True).reset_index()

    rich_percentage = round(num_min_workers[num_min_workers['index'] == '>50K']['salary'].values[0]*100, 1)

    # What country has the highest percentage of people that earn >50K?

    earing_country0 = df.groupby(['native-country','salary']).count()['age'].reset_index().set_index(['native-country', 'salary'])
    earing_country1 = earing_country0.groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).reset_index()
    earing_country2 = earing_country1[earing_country1['salary'] == '>50K']


    highest_earning_country = earing_country2[earing_country2['age'] == earing_country2['age'].max()]['native-country'].values[0]
    highest_earning_country_percentage = round(earing_country2[earing_country2['age'] == earing_country2['age'].max()]['age'].values[0], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    mask_popular_job = (df['native-country'] == 'India') & (df['salary'] == '>50K')
    top_IN_occupation = df[mask_popular_job]['occupation'].value_counts().index[0]

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