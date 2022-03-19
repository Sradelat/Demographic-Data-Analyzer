import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 150)


def calculate_demographic_data(print_data=True):
    df = pd.read_csv(r"C:\Users\shawn\Desktop\Python Learning\adult.data.csv", delimiter=",")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()  # number of entries for each race

    # What is the average age of men?
    average_age_men = round(df.loc[df["sex"] == "Male", "age"].mean(), 1)  # if male, grab age, take mean

    # What is the percentage of people who have a Bachelor's degree?
    # count num of bachelors under education divided by length of df turned perc
    percentage_bachelors = round(((df["education"] == 'Bachelors').sum() / df.shape[0]) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[(df["education"] == "Bachelors") |  # or
                              (df["education"] == "Masters") |
                              (df["education"] == "Doctorate")]
    lower_education = df.loc[(df["education"] != "Bachelors") &  # and
                             (df["education"] != "Masters") &
                             (df["education"] != "Doctorate")]

    # percentage with salary >50K
    # amount of True values divided by length of the df turned perc
    higher_education_rich = round(((higher_education["salary"] == ">50K").sum() / higher_education.shape[0]) * 100, 1)
    lower_education_rich = round(((lower_education["salary"] == ">50K").sum() / lower_education.shape[0]) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()  # value is 1

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    # num of people with hours worked == 1
    num_min_workers = df.loc[df["hours-per-week"] == min_work_hours].shape[0]  # value is 20
    # filters hours worked == 1 AND salary == >50K / number of workers with 1 hour worked * 100 for percentage
    rich_percentage = round((df.loc[(df["hours-per-week"] == min_work_hours) & (df["salary"] == ">50K")].shape[0] /
                            num_min_workers * 100), 1)  # value is 10.0 percent

    # What country has the highest percentage of people that earn >50K?
    num_rich_in_country = df.loc[df["salary"] == ">50K", "native-country"].value_counts()  # count of >50K in each cntry
    num_in_country = df["native-country"].value_counts()  # count of instances of each country
    # sort values highest to lowest (we want the highest)
    highest_earning_country = ((num_rich_in_country / num_in_country) * 100).sort_values(ascending=False).index[0]
    highest_earning_country_percentage = round(((num_rich_in_country /
                                                 num_in_country) * 100).sort_values(ascending=False)[0], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[(df["native-country"] == "India") &  # print highest occupation value in India & >50K
                               (df["salary"] == ">50K"), "occupation"].value_counts().index[0]

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



