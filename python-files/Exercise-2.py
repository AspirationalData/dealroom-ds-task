# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer


# %%
df = pd.read_csv("~/Documents/dealroom-ds-task/data/data_scientist_intern_revenue_model.csv")
df


# %%
for value in df[list(df.columns)]:
    df[str(value)] = df[str(value)].replace(",", "")

df

# %% [markdown]
# ### Now that we know how to format the data accordingly, let's apply this operation to all the fields in the DataFrame.
# 

# %%
# Let's visualize the dataframe to check if the changes were applied correctly.
df


# %%
df.columns[1 : 6]


# %%
df.columns


# %%
df

# %% [markdown]
# ## We need to remove the commas that separate the numbers, since otherwise it would give us probems down the line, because data type would be STRING intead of INT.
# %% [markdown]
# ### Let's remove the thousand separator in order to be able to work with the data using scikit-learn.
# %% [markdown]
# ### We figured out a formula to remove the commas that prevent scikit-learn from being able to work with this data.
# ### We use a regular expression: substitute all special charachters with nothing. 
# ### In practice, this deletes all special characters, including commas.

# %%
# This is the programming logic to do the replacing on one column only.
df['Revenue_2015'] = df['Revenue_2015'].str.replace(r'\W',"")


# %%
### After deleting the space that was present after the the column 'Revenue_2015' manually, I am able to access the data from said column.
df['Revenue_2015']


# %%
# This is the column name list that we will work with.
print(list(df.columns))


# %%
# We don't need to modify every column, but the following ones:
df.columns[1 : 6]


# %%
# We only include columns that have comma separators. The one that have decimal separator do not need to be converted, since they can be converted to INT automatically
#  and don't abide by the REGEX rule we created.

# We exclude the first and the last column in this loop.
for value in df.columns[1 : 6]:
    df[str(value)] = df[str(value)].str.replace(r'\W',"")
    


# %%


# %% [markdown]
# ### We will use SimpleImputer from scikit-learn to fill out NaN values with the row's mean, so that we have all the data we need to predict the 2020's revenue using a Linear Regression.
# 
# ### After calculating the linear model, we will evaluate the goodness of fit of this model.

# %%
# We convert the dataframe into an array and discard the last column, the variable to predict.
df_process = df.iloc[:, :-1].values
df_process


# %%
# We create a "mean_imputer" option with the appropiate parameters to perform the preprocessing.
mean_imputer = SimpleImputer(missing_values=[np.nan, ''], strategy="mean", verbose=0)


# %%
df_process = mean_imputer.fit_transform(df_process[1:, 1:10])


# %%
# mean_imputer = mean_imputer.fit(df_process[1:, 1:10])
# df_process = mean_imputer.transform(df_process[1:, 1:10])
# df_process


# %%
df_process


