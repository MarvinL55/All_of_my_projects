import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the data into a Pandas DataFrame
df = pd.read_csv("C:\\Users\\marvi\\Downloads\\AAPL.csv")

# fill missing values with the mean of the column
#df.fillna(df.mean(), inplace=True)
df = df.loc[:, df.columns.str.contains('^[a-zA-Z]+$', regex=True)]


# calculate the daily returns of each stock
returns = df.pct_change()

# calculate the average daily return and standard deviation of the portfolio
portfolio_return = returns.mean().mean()
portfolio_std_dev = returns.std().mean()

# calculate the expected return and risk of the portfolio
expected_return = portfolio_return * 252
risk = portfolio_std_dev * np.sqrt(252)

# plot the expected return and risk as a scatter plot
plt.scatter(risk, expected_return, alpha=0.5)
plt.xlabel('Risk')
plt.ylabel('Expected Return')
plt.title('Risk and Reward of Portfolio')
plt.show()
