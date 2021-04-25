import streamlit as st
import numpy as np

import pandas as pd
#from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import RendererAgg
_lock = RendererAgg.lock
 
header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_training = st.beta_container()


with header:
  st.title("welcome to my web app for Data Science.")
  st.write(""" 
	Explore some of my Data Science projects:

	Exploratory Data Analysis & Visualization:

	""")
  st.subheader('The goal of that dataset is to predict if a customer will respond to a personal loan campaign:')


with dataset:
	 bank_personal= pd.read_csv('Bank_Personal_Loan_Modelling.csv')

	 st.write(bank_personal.head(3))



	 st.text('Let s how see the correlation of the attributes looks like:')
	 st.write(bank_personal.corr() )


	#st.write(bank_personal.plot.box("Income") )

	#st.write(bank_personal['Income', 'Personal Loan'].hist(bins=50, figsize=(20,15)) plt.show()
    
          


	 st.text('Some Statistics:')

	 st.write(bank_personal.describe() )

	 st.text('Checking out any missing values:')
	 st.text(bank_personal.isnull().sum())

    #st.write(  sns.heatmap(insurance_copy.isnull()) )
	
	 st.subheader('This is a line chart of column personal loan:')
	 st.line_chart(bank_personal['Personal Loan'])
	 hist_values= np.histogram(bank_personal['Personal Loan'],bins= 24)

	 st.bar_chart(hist_values)

	 st.text('This show the percentage of customer has responded to the first personal loan campaign:')

	 st.write(bank_personal["Personal Loan"].value_counts(normalize=True))	 
       #Income_dist =pd.DataFrame(bank_personal['Income'].value_counts())
     #st.bar_chart(Income_dist)

with _lock:
   #fig.title('This is a figure)')
    st.text('Annual income of the customer:')
    st.line_chart(bank_personal['Income'])

    st.text('this is the mean of income of a customer:')
    st.write(bank_personal["Income"].mean())
   
   

   
   
   
   
    
 
