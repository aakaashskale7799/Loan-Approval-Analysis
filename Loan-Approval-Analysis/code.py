# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 



# code starts here
path=pd.read_csv("/opt/greyatom/kernel-gateway/data/executor/attachments/account/b1/2a7f53f8-19f6-45c7-9d74-560da9338b1a/b69/a340d73b-3d57-4e25-9cfd-074cea5af958/file.csv")
bank=pd.DataFrame(path)
categorical_var=bank.select_dtypes(include = 'object')
print(categorical_var.head())
numerical_var=bank.select_dtypes(include = 'number')
print(numerical_var)

# code ends here


# --------------
# code starts here
banks=bank.drop(["Loan_ID"], axis=1)
banks.isnull().sum()
bank_mode=banks.mode().iloc[0]
banks.fillna(bank_mode, inplace=True) 
print(banks.isnull().sum())



#code ends here


# --------------
# Code starts here
avg_loan_amount=pd.pivot_table(banks , values="LoanAmount",index=["Gender","Married","Self_Employed"],aggfunc=np.mean)


# code ends here



# --------------
# code starts here
# code for loan aprroved for self employed
loan_approved_se = banks.loc[(banks["Self_Employed"]=="Yes")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_se)

# code for loan approved for non self employed
loan_approved_nse = banks.loc[(banks["Self_Employed"]=="No")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_nse)

# percentage of loan approved for self employed
percentage_se = (loan_approved_se * 100 / 614)
percentage_se=percentage_se[0]
# print percentage of loan approved for self employed
print(percentage_se)

#percentage of loan for non self employed
percentage_nse = (loan_approved_nse * 100 / 614)
percentage_nse=percentage_nse[0]
#print percentage of loan for non self employed
print (percentage_nse)

# code ends here


# --------------
# code starts here
x=banks["Loan_Amount_Term"]
loan_term=banks["Loan_Amount_Term"].apply(lambda x: x/12)

big_loan_term=[]
for x in loan_term:
    if x>=25:
        big_loan_term.append(x)
big_loan_term=len(list(big_loan_term))
print(big_loan_term)



# code ends here


# --------------
# code starts here

columns_to_show = ['ApplicantIncome', 'Credit_History']
 
loan_groupby=banks.groupby(['Loan_Status'])

loan_groupby=loan_groupby[columns_to_show]

# Check the mean value 
mean_values=loan_groupby.agg([np.mean])

print(mean_values)



