import zipfile
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


#Data Extraction
#Path for zip file and file to extract
zip_file_path = "Customer_Churn_Prediction\Customer_Churn_Dataset.zip"
extraction_dir = "extraction_data"

#Creating directory to extract file
os.makedirs(extraction_dir, exist_ok = True)

#Extracting zip file
with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
    zip_ref.extractall(extraction_dir)

#Listing extracted files
extracted_files = os.listdir(extraction_dir)
print(f"Extracted Files: {extracted_files}")


#Data Loading
data_file = os.path.join(extraction_dir, "Telco_customer_churn.xlsx")
data = pd.read_excel(data_file)
print(data.head())


#Data Preprocessing
#No missing values
#Converting categorical variables to numerical (if any)
data = pd.get_dummies(data)
#Split into features and target
X = data.drop("Churn Value", axis=1)
y = data["Churn Value"]


#Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 6000)


#Building a Machine Learning Model
#Initialize and train the model
model = LogisticRegression()
model.fit(X_train, y_train)

#Make predictions
y_pred = model.predict(X_test)

#Evaluate the model
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))