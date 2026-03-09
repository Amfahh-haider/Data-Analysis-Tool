import pandas as pd
import matplotlib.pyplot as plt


class DataAnalysisTool:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        try:
            self.data = pd.read_csv(self.file_path)
            print("Dataset loaded successfully.\n")
        except Exception as e:
            print("Error loading dataset:", e)

    def clean_data(self):
        if self.data is not None:
            self.data = self.data.drop_duplicates()
            self.data = self.data.dropna()
            print("Data cleaned.\n")

    def show_basic_info(self):
        if self.data is not None:
            print("Dataset Info:\n")
            print(self.data.info())
            print("\nFirst 5 Rows:\n")
            print(self.data.head())

    def show_statistics(self):
        if self.data is not None:
            print("\nStatistical Summary:\n")
            print(self.data.describe())

    def plot_column(self, column_name):
        if self.data is not None and column_name in self.data.columns:
            self.data[column_name].plot(kind='hist', bins=20)
            plt.title(f"Distribution of {column_name}")
            plt.xlabel(column_name)
            plt.ylabel("Frequency")
            plt.show()
        else:
            print("Column not found.")


def main():
    file_path = input("Enter dataset CSV file path: ")

    tool = DataAnalysisTool(file_path)

    tool.load_data()
    tool.clean_data()
    tool.show_basic_info()
    tool.show_statistics()

    column = input("\nEnter column name to visualize (or press Enter to skip): ")
    if column:
        tool.plot_column(column)


if __name__ == "__main__":
    main()
