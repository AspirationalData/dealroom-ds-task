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





