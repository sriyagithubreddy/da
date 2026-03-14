import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv(
    "adult.data.csv",
    names=[
        "age","workclass","fnlwgt","education","education-num",
        "marital-status","occupation","relationship","race","sex",
        "capital-gain","capital-loss","hours-per-week","native-country","salary"
    ],
    skipinitialspace=True
    )

    # 1. How many of each race are represented
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round(
        (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1
    )

    # 4. Advanced education (Bachelors, Masters, Doctorate)
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # 5. Percentage with higher education earning >50K
    higher_education_rich = round(
        (higher_education[higher_education['salary'] == '>50K'].shape[0] /
         higher_education.shape[0]) * 100, 1
    )

    # 6. Percentage without higher education earning >50K
    lower_education_rich = round(
        (lower_education[lower_education['salary'] == '>50K'].shape[0] /
         lower_education.shape[0]) * 100, 1
    )

    # 7. Minimum number of hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # 8. Percentage of people working minimum hours earning >50K
    min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = round(
        (min_workers[min_workers['salary'] == '>50K'].shape[0] /
         min_workers.shape[0]) * 100, 1
    )

    # 9. Country with highest percentage of people earning >50K
    country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True)

    highest_earning_country = country_salary.loc[:, '>50K'].idxmax()

    highest_earning_country_percentage = round(
        country_salary.loc[:, '>50K'].max() * 100, 1
    )

    # 10. Most popular occupation for those earning >50K in India
    top_IN_occupation = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].value_counts().idxmax()

    # Print results
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_education_rich)
        print("Percentage without higher education that earn >50K:", lower_education_rich)
        print("Min work time:", min_work_hours)
        print("Percentage of rich among those who work fewest hours:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


# Run the function when the file is executed
if __name__ == "__main__":
    calculate_demographic_data()