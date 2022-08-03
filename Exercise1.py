import calendar
import os
import pandas as pd


def read_csv(file_path: str) -> pd.DataFrame:
    """
    # Parameters:
    - file_path: string that contains the path to the csv file. Example: "C:/Users/Public/2017.csv"
    
    # Returns:
    - pandas.DataFrame
    """
    print(f"Reading file from {file_path}")
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print("No '2017.csv' file found in root folder")
        os._exit(0)
    if df.empty:
        raise Exception("No Dataframe obtained.")
    return df


def most_transactions_exchange(df: pd.DataFrame) -> pd.DataFrame:
    new_df = df[df['exchange'] != 'off exchange']['exchange'].value_counts()
    exchange_name, transactions_count = new_df.idxmax(), new_df.to_list()[0]
    return exchange_name, transactions_count


def highest_combined_value_eur(df: pd.DataFrame) -> pd.DataFrame:
    # Normalize date.
    new_df = df.copy()
    new_df['inputdate'] = pd.to_datetime(
        new_df['inputdate'], format="%Y%m%d")
    # Find values from August 2017 and calculate max valueEUR.
    sorted_df = new_df[(new_df['inputdate'].dt.year == 2017) & (new_df['inputdate'].dt.month == 8)][[
        'companyName', 'valueEUR']].groupby('companyName').sum().sort_values('valueEUR', ascending=False)
    company_name = sorted_df.iloc[0].name
    return company_name


def transactions_percentage_per_month(df: pd.DataFrame) -> pd.DataFrame:
    new_df = df.copy()
    # Normalize tradeDate.
    new_df['tradedate'] = pd.to_datetime(
        new_df['tradedate'], format="%Y%m%d")
    filtered_df = new_df[(new_df['tradedate'].dt.year == 2017)
                         & (new_df['tradeSignificance'] == 3)]
    year_qty = len(filtered_df.axes[0])
    results = list()
    for i in range(1, 13):
        month_qty = len(
            filtered_df[filtered_df['tradedate'].dt.month == i].axes[0])
        # Month quantity of transactions
        percentage = int(100*month_qty/year_qty)
        month_name = calendar.month_name[i][:3]
        results.append(f"{month_name}, {percentage}%")
    return results


if __name__ == '__main__':
    # Define absolute path.
    PATH = os.path.abspath('.')
    # Load csv.
    df = read_csv(PATH+'/2017.csv')
    # 1. What Exchange has had the most transactions in the file?
    exchange_name, count = most_transactions_exchange(df)
    print("What Exchange has had the most transactions in the file?")
    print(f"\tAnswer: {exchange_name}, {count} transactions")
    # 2. In August 2017, which companyName had the highest combined valueEUR?
    company_name = highest_combined_value_eur(df)
    print("In August 2017, which companyName had the highest combined valueEUR?")
    print(f"\tAnswer: {company_name}")
    # 3. For 2017, only considering transactions with tradeSignificance 3, what is the percentage of transactions per month?
    transactions_per_month = transactions_percentage_per_month(df)
    print("For 2017, only considering transactions with tradeSignificance 3, what is the percentage of transactions per month?")
    for month in transactions_per_month:
        print(month, sep="\n")
