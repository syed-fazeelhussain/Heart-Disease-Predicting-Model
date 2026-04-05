import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Heart Disease.csv")
heart_disease = pd.Categorical(df["HeartDisease"],ordered=True)
heart_disease = heart_disease.rename_categories([0,1])
df["HeartDisease"] = heart_disease
x = ["age","alco","weight","cigs"]
df = df.dropna()



sns.set_theme(style="darkgrid")
figure, axes = plt.subplots(2,2,figsize=(28,10))
flat_axes = axes.flatten()

# Generating subplots for boxplots, to find outliers
for i, col in enumerate(x):
    sns.boxplot(x=df[col], ax = flat_axes[i])
    flat_axes[i].set_title(f"Box Plot for {col}")

plt.tight_layout()
plt.show()


# # Generating KDE plots for assessing normality

sns.set_theme(style="darkgrid")
figure, axes = plt.subplots(2,2,figsize=(28,10))
flat_axes = axes.flatten()

for i,col in enumerate(x):
    sns.kdeplot(x=df[col], ax = flat_axes[i])
    flat_axes[i].set_title(f"KDEPlot for {col}")

plt.tight_layout()
plt.show()


#Logistic Reg plots

sns.set_theme(style="darkgrid")
figure, axes = plt.subplots(2,2,figsize=(28,10))
flat_axes = axes.flatten()


col = ["age","alco","cigs"]
for i,col in enumerate(col):
    sns.regplot(x=df[col],y=df["HeartDisease"],data=df,ax=flat_axes[i],logistic=True,ci=None,line_kws={"color":"red"})
    flat_axes[i].set_title(col)









plt.tight_layout()
plt.show()