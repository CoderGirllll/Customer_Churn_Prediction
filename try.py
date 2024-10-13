from zipfile import ZipFile


def main():
    filename = "Customer_Churn_Prediction\Customer_Churn_Dataset.zip"
    with ZipFile(filename, "r") as dataset:
        dataset.printdir()
        print("Extracting")
        dataset.extractall()
        data = dataset.read("Telco_customer_churn.xlsx")
        print("Done")

        count_churn(data)


def count_churn(data):
    #churn = data[30].value_counts()   #30th Column is "Churn Value"
    #print(churn)
    return


main()


'''import kagglehub

path = kagglehub.dataset_download("dataset name")
print("Path: ", path)'''