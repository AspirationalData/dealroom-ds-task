# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ### The goal of this exercise is finding duplicates in this file.
# 
# ### However, what we consider "duplicate" might vary from person to person and has to be adapted to the business need we are intending to meet, so in this exercise we'll generate different files for each approach we use to find duplicates.
# 
# ### For example, we might consider one datapoint as duplicate if various relevant columns (features) of the dataframe have the same values.
# 
# 
# ## Through this notebook, we will showcase different criteria to define one datapoint as "duplicate".

# %%
import pandas as pd


# %%
# We read the file and create a variable with its contents to explore it with pandas.
df = pd.read_csv('/home/local/Documents/dealroom-ds-task/data/data_scientist_duplicate_detection.csv')
df


# %%
# Duplicate = Coincidence in "id" and "name".
dups_id_name_overlap = df.loc[df.duplicated(subset=['id', 'name']), :]

# Export duplicates to file.
dups_id_name_overlap.to_csv("~/Documents/dealroom-ds-task/output_csv/dups_id_name_overlap.csv")


# %%
# # Duplicate = Coincidence in "tagline" and "name".
dups_tagline_name_overlap = df.loc[df.duplicated(subset=['tagline', 'name']), :]

# Export duplicates to file.
dups_tagline_name_overlap.to_csv("~/Documents/dealroom-ds-task/output_csv/dups_tagline_name_overlap.csv")


# %%
# Duplicate = Coincidence in "zip" and "name".
dups_zip_name_overlap = df.loc[df.duplicated(subset=['zip', 'name']), :]

# Export duplicates to file.
dups_zip_name_overlap.to_csv("~/Documents/dealroom-ds-task/output_csv/dups_zip_name_overlap.csv")


# %%
# Duplicate = Coincidence in "address" and "name".
dups_adress_name_overlap = df.loc[df.duplicated(subset=['address', 'name']), :]

# Export duplicates to file.
dups_adress_name_overlap.to_csv("~/Documents/dealroom-ds-task/output_csv/dups_adress_name_overlap.csv")

# %% [markdown]
# ### We considered different options to check for duplicates and we dumped the duplicate datapoints to different files in order to decide later which datapoints to drop, depending on which criteria we find the most fitting.
# %% [markdown]
# ### Now, we'll explore some more "manual" ways to find the number of duplicates in total in the dataset.

# %%
# Alternate way to check if there's any duplicate (we check all the elements of the row, row by row).
temp_var = df.duplicated()

# We create a counter to count the total amount of duplicates.
dup_num = 0

for dup in temp_var:
    # If a duplicate is found (row is marked as True by df.duplicated())
    if dup == True:
        # Add 1 unit to the counter
        dup_num += 1

# We print the value of the counter in console.
print("There is {} duplicate/s (row by row) in the Dataframe".format(dup_num))


# %%
# Alternate Approach for checking total row duplicates:
# Exact coincidence, element per element in a given row, using the sum() method to get the cumulative sum of "True" values of df.duplicated().
df.duplicated().sum()


# %%
# We'll show on the screen the duplicated rows. It will show the UNIQUE INSTANCES that are duplicated.
# This means that even if a row is duplicated multiple times, it will only show up once in the output.
df.loc[df.duplicated(), :]


# %%
# We can thing of this as a table in a Relational Database: same ID means it's the same element, thus duplicate.

# In order to find duplicates, we count the instances of each row.
# For that purpuse, we use Counter from collections:
#  
# The Counter method will create a dictionary that contains a key-value pair with the attribute and the total counts of each instance of the attribute at hand.
from collections import Counter

id_counts = Counter(df['id'])

# We loop through every key-value pair in the Counter dictonary. If the count is greater than one, print the ID (has duplicates)
for key, value in id_counts.items():
    if value > 1:
        # print(key)
        # print(value)
        print("({}, {})".format(key, value), end= "\n" * 2)
        print("The key (or ID) {} has a total of {} instances in this CSV file".format(key, value))

# %% [markdown]
# ### As you can see, there's only one row that is duplicated (element by element).
# ### It has two ocurrences in total in the .csv file.

