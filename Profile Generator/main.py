from faker import Faker
from faker.providers import BaseProvider
import pandas as pd
import random
from io import StringIO

# create faker object and set locality to India (English)
faker = Faker('en_IN')

# create pandas DataFrame to store faker profiles
df = pd.DataFrame()

# sets the initial profile data provided by faker
for i in range(100):
    df = df.append(faker.profile(), ignore_index = True)

# delete unnecessary columns
del df['blood_group']
del df['ssn']

# adding custom columns
# use this same format for adding as many columns as desired

# create a list of possible entry values to new column (ex: religion)
religion = ['Hinduism', 'Islam', 'Christianity', 'Sikhism', 'Buddhism', 'Jainism', 'Other']

# loop to assign a random entry to each row of the original df
for i in range(100):
    # do this for each new column to add
    df.at[i, 'religion'] = random.choice(religion)

# reorders the columns alphabetically
# note: case-senstive (if column name is capitalized, it will be placed before all columns that start with lower-case)
df = df.reindex(sorted(df.columns), axis=1)

# export the df to csv file
df.to_csv('user-profiles-test.csv')