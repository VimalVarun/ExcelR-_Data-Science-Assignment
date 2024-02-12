#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the libraries
from scipy import stats
import pandas as pd
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# # 1 Question
# 
# A F&B manager wants to determine whether there is any significant difference in the diameter of the cutlet between two units. A randomly selected sample of cutlets was collected from both units and measured? Analyze the data and draw inferences at 5% significance level. Please state the assumptions and tests that you carried out to check validity of the assumptions.
# 

# In[2]:


#Stage 1. Here we have two independent samples, Hence, we go for T-test two sample with two tails test

#Stage 2. Define Hypothesis

    #(i)Reject Null Hypothesis (H0) population mean1 = population 2
    #(ii)Alternate Hypothesis (Ha) population1 ≠ Population 2
    
#Stage 3. we have to find the two side probability hence its two tail test

#Stage 4. Alapha value or significance value

#Stage 5. Calculate P value

#Stage 6. Make Conclusion

    #P < alpha Reject H0
    #P < alpha fail to reject H0


# In[3]:


Cutlets = pd.read_csv("Cutlets.csv")
Cutlets


# # Stage 1. Define Hypothies
# 
# (i)Reject Null Hypothesis (H0) population mean1 = population 2
# (ii)Alternate Hypothesis (Ha) population1 ≠ Population 2

# In[4]:


Cutlets.describe()


# In[5]:


unite_A = Cutlets["Unit A"]


# In[6]:


unite_B = Cutlets["Unit B"]


# In[7]:


statistic , p_value = stats.ttest_ind(unite_A ,unite_B)


# In[8]:


statistic


# In[9]:


p_value


# # Stage 4. Alapha value or significance value
# 
# Error rate significance is 5%. However, as it is a two-tail test, we must compute both sides of the possibility; as a result, the significance error can be divided by two. Consequently, the right side's significance error is 0.025.

# # Plotting Q-Q plot to check whether the distribution follows normal distribution or not# 

# In[10]:


plt.figure(figsize = (8,6))
labels = ['Unit A', 'Unit B']
sns.distplot(Cutlets['Unit A'], kde = True)
sns.distplot(Cutlets['Unit B'],hist = True)
plt.legend(labels);


# In[11]:


alpha = 0.025
print('Significnace=%.3f, p=%.3f' % (alpha, p_value))

if p_value < alpha:
    print('Reject Ho. there is a significance difference between two Units A and B.')
else:
    print('Fail to reject Null Hypothesis. There is a no significane of different')


# In[ ]:





# # 2.Question
# 
# A hospital wants to determine whether there is any difference in the average Turn Around Time (TAT) of reports of the laboratories on their preferred list. They collected a random sample and recorded TAT for reports of 4 laboratories. TAT is defined as sample collected to report dispatch.
# 

# # Here we have four independent samples, Hence, we go for Annova test.
# 
# Define Hypothesis
# 
#     #(i)Null Hypothesis (H0) Sample1 = Sample2 = Sample =3, Sample = 4
#     #(ii)Alternate Hypothesis (Ha) Atleast one of them is different
#     

# In[12]:


LabTAT = pd.read_csv("LabTAT.csv")
LabTAT


# In[13]:


f ,p = stats.f_oneway(LabTAT['Laboratory 1'],LabTAT['Laboratory 2'],LabTAT['Laboratory 3'],
                       LabTAT['Laboratory 4'])


# In[14]:


f, p


# # Plotting Q-Q plot to check whether the distribution follows normal distribution or not

# In[15]:


plt.figure(figsize = (8,6))
labels = ['Lab 1', 'Lab 2','Lab 3', 'Lab 4']
sns.distplot(LabTAT['Laboratory 1'], kde = True)
sns.distplot(LabTAT['Laboratory 2'],hist = True)
sns.distplot(LabTAT['Laboratory 3'],hist = True)
sns.distplot(LabTAT['Laboratory 4'],hist = True)
plt.legend(labels);


# In[16]:


alpha = 0.05
print('Significnace=%.3f, p=%.3f' % (alpha, p))
if p < alpha:
    print('Reject Ho. there is a significance difference between TAT of reports of the laboratories.')
else:
    print('Fail to reject Null Hypothesis. All Samples are equal to same')


# In[ ]:





# # Question 3     
# 
# Sales of products in four different regions is tabulated for males and females. Find if male-female buyer rations are similar across regions.
# 

# # Stage 1 = Here we have two independent samples. Hence, we go for Chi square test
# # stage 2 
# Make two Hypothesis one contradicting to other
# 
# Null Hypothesis: There is no association or dependency between the gender based buyer rations across regions
# 
# Alternative Hypthosis: There is a significant association or dependency between the gender based buyer rations across regions
# 
# # Stage 3
# 
# as it is chi squre test hence there is only one tail. Therefore, the alpha value is 0.05

# In[32]:


from scipy.stats import chi2_contingency
import numpy as np


# In[18]:


BuyerRatio =  pd.read_csv("BuyerRatio.csv", index_col=0)
BuyerRatio


# In[19]:


chi2,P,df,exp = chi2_contingency(BuyerRatio)


# In[20]:


P


# In[21]:


chi2


# In[22]:


df


# In[23]:


exp


# In[30]:


alpha = 0.05
print('Significnace=%.3f, p=%.3f' % (alpha, P))
if P < 0.05:      
    print('Reject Null Hypothesis.Columns are dependent on each other.')
else:
    print('Fail to reject null hypothesis.Columns are Independent on each other')


# In[ ]:





# # Question 4

# #     TeleCall uses 4 centers around the globe to process customer order forms. They audit a certain %  of the customer order forms. Any error in order form renders it defective and has to be reworked before processing.  The manager wants to check whether the defective %  varies by centre. Please analyze the data at 5% significance level and help the manager draw appropriate inferences
# 

# # Stage 1 = Here we have four independent samples. Hence, we go for Chi square test
# 
# # stage 2 
# Make two Hypothesis one contradicting to other
# 
#     #(i)Null Hypothesis (H0) Sample1 = Sample2 = Sample =3, Sample = 4
#     #(ii)Alternate Hypothesis (Ha) Atleast one of them is different

# In[39]:


Costomer_OrderForm = pd.read_csv("Costomer+OrderForm.csv")
Costomer_OrderForm


# In[40]:


Costomer_OrderForm.describe()


# In[42]:


#Checking value counts in data
print(Costomer_OrderForm['Phillippines'].value_counts(),Costomer_OrderForm['Indonesia'].value_counts(),Costomer_OrderForm['Malta'].value_counts(),Costomer_OrderForm['India'].value_counts())


# In[58]:


#Creating Contingency table
contingency_table = [[271,267,269,280],[29,33,31,20]]
contingency_table


# In[59]:


#Calculating Expected Values for Observed data
chi2,P,df,exp = chi2_contingency(contingency_table)


# In[60]:


chi2


# In[62]:


P


# In[63]:


df


# In[64]:


exp


# In[65]:


stat, p, df, exp = stats.chi2_contingency(contingency_table)
print("Statistics = ",stat,"\n",'P_Value = ', p,'\n', 'degree of freedom =', df,'\n', 'Expected Values = ', exp)


# In[66]:


alpha = 0.05
print('Significnace=%.3f, p=%.3f' % (alpha, P))
if  P < 0.05:      
    print('Reject Null Hypothesis.Columns are dependent on each other.')
else:
    print('Fail to reject null hypothesis.Columns are Independent on each other')


# In[67]:


P


# In[68]:





# In[ ]:





# In[ ]:




