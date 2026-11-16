import pandas as pd
import numpy as np
import pandera as pa
# Load the Excel file
df = pd.read_excel(
    r"C:\Users\hadil\OneDrive\Desktop\data sc\Dataset for Data Analytics.xlsx"
)

df["CouponCode"] = df["CouponCode"].fillna("No Coupon")# Replace missing values in CouponCode with "No Coupon"

print(df.isnull().sum())# Count missing values in each column

# Show basic statistics for the numerical columns
print(df[["Quantity","UnitPrice","ItemsInCart","TotalPrice"]].describe())
# Calculate the first quartile (25%)
Q1=df[["Quantity","UnitPrice","ItemsInCart","TotalPrice"]].quantile(0.25)
# Calculate the third quartile (75%)
Q3=df[["Quantity","UnitPrice","ItemsInCart","TotalPrice"]].quantile(0.75)
# Calculate the Interquartile Range
IQR=Q3-Q1
# Calculate the lower boundary for outliers
lower_bound=Q1-1.5*IQR
# Calculate the upper boundary for outliers
upper_bound=Q3+1.5*IQR
print("Q1 :")
print(Q1)
print("\nQ3 :")
print(Q3)

print("\nIQR :")
print(IQR)

print("\nLower Bound :")
print(lower_bound)

print("\nUpper Bound :")
print(upper_bound)
# Find values above the upper boundary
print(df[df["TotalPrice"]>upper_bound["TotalPrice"]])
# Find values above the lower boundary
print(df[df["TotalPrice"]<lower_bound["TotalPrice"]])
lower=lower_bound["TotalPrice"]
upper=upper_bound["TotalPrice"]
# Cap outliers to keep all rows in the dataset
df["TotalPrice"]=df["TotalPrice"].clip(lower,upper)
# Check the data after outlier treatment
print(df[["Quantity","UnitPrice","ItemsInCart","TotalPrice"]].describe())
# Phase 2: Feature Engineering
# Data cleaning is complete.Create new features from the existing data
df["HasCoupon"]=(df["CouponCode"]!="No Coupon").astype(int)
print(df[["CouponCode","HasCoupon"]].head(10))
#count the number of orders for each customer
df["CustomerOrderCount"]=df.groupby("CustomerID")["OrderID"].transform("count")
print(df[["CustomerID","CustomerOrderCount"]].head(10))
#count the number of orders for each product
df["ProductSalesCount"]=df.groupby("CustomerID")["OrderID"].transform("count")
print(df[["CustomerID","ProductSalesCount"]].head(10))
# Show the categorical columns in the dataset
print(df.select_dtypes(include="object").columns)
# Select the categorical columns that we want to convert
categorical_columns=["Product","PaymentMethod","OrderStatus","CouponCode","ReferralSource"]
# Convert categorical columns into numerical columns using One-Hot Encoding
df=pd.get_dummies(df,columns=categorical_columns,dtype=int)
print(df.head(10))
#calculate the correlation between numerical features
corrolation_mtx=df.corr(numeric_only=True).abs()
print(corrolation_mtx)
# Keep only the upper triangle of the correlation matrix
upper_triangle = corrolation_mtx.where(
    np.triu(np.ones(corrolation_mtx.shape), k=1).astype(bool)
)
# Show the upper triangle
print(upper_triangle)
#Find pairs with correlation greater than 0.80
high_corr=upper_triangle[upper_triangle > 0.80]
if high_corr.dropna().empty:
    print("No highly correlated feature pairs found.")
else:
    print(" highly correlated feature pairs ")
    print(high_corr.dropna())
#Create a schema with the expected data types
schema=pa.DataFrameSchema({"Quantity":pa.Column(int),"UnitPrice":pa.Column(float),
                          "ItemsInCart":pa.Column(int),"TotalPrice":pa.Column(float),
                          "HasCoupon":pa.Column(int),"CustomerOrderCount":pa.Column(int)
                          , "ProductSalesCount":pa.Column(int)})
# Validate the DataFrame using the schema
try:
    schema.validate(df,lazy=True)
    print("Data validation successful: the data is correct")
except pa.errors.ShemaErrors:
    print("Data validation failed: the data is not correct")

# Save the cleaned data into a new Excel file
df.to_excel(
    r"C:\Users\hadil\OneDrive\Desktop\data sc\Dataset_cleaned.xlsx",
    index=False
)
