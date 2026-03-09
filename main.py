import pandas as pd
import matplotlib.pyplot as plt


class DataAnalysisTool:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        """Load CSV dataset"""
        try:
            self.data = pd.read_csv(self.file_path)
            print("✅ Dataset loaded successfully.\n")
        except FileNotFoundError:
            print("❌ File not found. Please check the path.")
        except Exception as e:
            print("❌ Error loading dataset:", e)

    def clean_data(self):
        """Remove duplicates and missing values"""
        if self.data is not None:
            initial_rows = len(self.data)
            self.data.drop_duplicates(inplace=True)
            self.data.dropna(inplace=True)
            cleaned_rows = len(self.data)
            print(f"✅ Data cleaned: {initial_rows - cleaned_rows} rows removed.\n")

    def show_basic_info(self):
        """Display dataset info and first few rows"""
        if self.data is not None:
            print("📊 Dataset Info:")
            print(self.data.info())
            print("\n📝 First 5 Rows:")
            print(self.data.head())

    def show_statistics(self):
        """Display statistical summary"""
        if self.data is not None:
            print("\n📈 Statistical Summary:")
            print(self.data.describe())

    def plot_column(self, column_name):
        """Plot histogram of a column"""
        if self.data is not None:
            if column_name in self.data.columns:
                self.data[column_name].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
                plt.title(f"Distribution of {column_name}")
                plt.xlabel(column_name)
                plt.ylabel("Frequency")
                plt.grid(axis='y', linestyle='--', alpha=0.7)
                plt.show()
            else:
                print("❌ Column not found.")


def main():
    file_path = input("Enter dataset CSV file path: ")
    tool = DataAnalysisTool(file_path)

    tool.load_data()
    tool.clean_data()
    tool.show_basic_info()
    tool.show_statistics()

    while True:
        column = input("\nEnter column name to visualize (or press Enter to exit): ")
        if not column:
            break
        tool.plot_column(column)


if __name__ == "__main__":
    main()
