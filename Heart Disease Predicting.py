import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from scipy.special import lmbda
from scipy.stats import yeojohnson, skew

df = pd.read_csv("Heart Disease.csv")
df = df.dropna(subset=["id"])
df = df.dropna()
print(df["HeartDisease"].value_counts())

heart_disease = pd.Categorical(df["HeartDisease"],ordered=True)
heart_disease = heart_disease.rename_categories([0,1])
df["HeartDisease"] = heart_disease



y = df["HeartDisease"]
x = ["age","weight","alco","cigs"]







# We will perform 2 Logistic analysis:
# One will be with the data we have. No changes
# The second will be with treated data. Making the data normal using log method
# Based on that we will make a conclusion that which model is better with predictability

y = y
X1 = sm.add_constant(df[x])
result = sm.Logit(y,X1).fit()
print("Normal Logistic Regression")
print(result.summary())
#
# # Logistic using log
#
X = df[x]
df_with_log = np.log1p(X)
X = sm.add_constant(df_with_log)
print("Logistic using log method")
result = sm.Logit(y,X).fit()
print(result.summary())





# Another logistic regression but omitting weight since it had barely any significance
col = ["age","alco","cigs"]

X = sm.add_constant(df[col])
result = sm.Logit(y,X).fit()
print("Result of Logistic normal regression omitting weight")
print(result.summary())




# Now time for the predictive model

def heart_disease_predict(age,alco,cigs):
    intercept = -8.7705
    b_age = 0.0906
    b_alco = 0.0884
    b_cigs = 0.0481

    z = intercept + (b_age * age) + (b_alco * alco) + (b_cigs * cigs)

    probability = 1/(1+np.exp(-z))
    percentage_of_having_having_disease = probability * 100

    print(f"The percentage that you have heart disease is: {percentage_of_having_having_disease:.2f}%")
    print("It is to be noted that the pseudo R-square for this model is 0.1182; the model is acceptably good but may have inaccuracies.")

print("Welcome to the Heart Disease predicting model")
user_age = float(input("Enter your age: "))
user_alco = float(input("Enter your alcohol consumption per bottle (1 litre) in one week: "))
user_cigs = float(input("Enter number of cigarettes you smoke in one week: "))

heart_disease_predict(user_age,user_alco,user_cigs)





















# print(whisker)
# print(high_weight.to_string())
# print("Although some weights are way beyond the limit of interquartile range, they might have important info which, if we negate might lead to misleading results")

