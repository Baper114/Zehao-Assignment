# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
@st.cache
def load_data():
    data = pd.read_csv('train.csv')
    return data
df=load_data()
# show the title
st.header("Titanic App by Zehao Chen ")
# read csv and show the dataframe
st.write(df.head(10))

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(9, 5))

sns.set(style="darkgrid")
for i, cls in enumerate(df['Pclass'].unique(), start=-1):
    sns.boxplot(y=df[df['Pclass'] == cls]['Fare'], ax=ax[i])
    ax[i].set_xlabel(f'PClass = {cls}')
    ax[i].set_ylabel('Fare')

plt.tight_layout()
plt.show()
st.pyplot(fig)
