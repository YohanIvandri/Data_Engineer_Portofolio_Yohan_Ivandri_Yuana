import pandas as pd


# transform csv 
def transform(df, csv_path):
    exchange_rate = (
        pd.read_csv(csv_path)
        .set_index('Currency')['Rate']
        .to_dict()
    )

    for curr in ['EUR', 'GBP', 'INR']:
        df[f'MC_{curr}_Billion'] = (
            df['MC_USD_Billion']
            .mul(exchange_rate[curr])
            .round(2)
        )

    return df
