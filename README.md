# dealroom-ds-task

## Data Science Internship Test.

## - Exercise 2:

- First of all, we'll need to import the libraries that we'll be working with, in this case, **numpy, pandas and scikit-learn**.

In order to solve the problem, we need to use the same data type across all the datapoints available, so we'll try to uniform the data. 

1. We will remove the "thousand" separator (comma every three numbers to improve legibility) and the decimal separators present on the dataset. 
To achieve that goal, we will use a string method called .replace() that we will apply to each column of the Dataframe, except the first and last column, that will be left aside.


2. Later, we will transform our Dataframe into a Numpy array to pass the values to SimpleImputer(), a scikit-learn function. 
This function will fill out empty and NaN values with the mean value of the column, making the data ready for Machine Learning later, at least from a pre-processing standpoint.



3. After the previous step, we want to create a linear regression using the datapoints of each row to approximate the value of the last column (for each row), draw a scatterplot and draw the line that better fits the data (the line that minimizes the absolute value of the error)

4. After we have our predicted value, we will add the new data to the original dataset.


5. The last step would be to evaluate the goodness of fit of this model. We would do this using parameters like R-squared and the F-test.


## - Exercise 3:

- For this exercise, we only need to import the **pandas** library.

This exercise has an added difficulty that might now be evident for the untrained eye, but that can ruin a business decision if data is not cleaned correctly.

Some of the questions could be: 

**- What would constitute a duplicate in this scenario?**

**- Are there many colums that, when combined together, constitue a "PRIMARY KEY, using an SQL-like mentality?**

**And so on**

As the goal of this exercise is to present duplicates but we are unsure on which criteria to use, we will create different "alternatives" to answer this question, by creating different **.CSV** files for us to decide which criteria to apply to clean the data later.

1. Our first step is importing the data and assigning it to a variable


2. Later, we face the issue of finding duplicates: 
   
   We offer 2 criteria to check if a row has duplicates: 

   - Finding the same value across columns['A', 'B'] could be deemed as a duplicate.
  
   - Finding an exact row match is undeniably a duplicate.
  

  To find exact row matches, we simply execute **df.loc[df.duplicated(), :]**.

  To find **"column['A', 'B']"** matches we run the following command, substituting the placeholders for column names inside quotation marks: **df.loc[df.duplicated(subset=['{}', '{}']), :]**.

3. After we find the duplicates we were looking for through Python shell, we assign our results to a variable and export said variable to a **.CSV** file.


In the documents, you will find alternative approaches to get some of the information we were looking for.



