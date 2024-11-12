import pandas as pd

df = pd.read_csv('book.csv')

m1 = 25 # max bet of account with profit boost based on t&c of bookie
boost = 100 # profit boost in percentage
max_boostwin = 275 # maximum you can gain on the boost based on t&c of bookie

boost_mult = boost/100 + 1

# Function to calculate boosted udogsodds
def calculate_boosted_odds(row):
    if row['udogsodds'] > 0:
        return row['udogsodds'] * boost_mult
    elif row['udogsodds'] < 0:
        return row['udogsodds'] / boost_mult
    else:
        return row['udogsodds']  # Handle case where odds are 0 (if needed)

# Apply the function to each row
df['udogsodds_boosted'] = df.apply(calculate_boosted_odds, axis=1)

# Function to convert  favodds to decimal
def convert_favodds_to_dec(row):
    if row['favodds'] < 0:
        return 1 - (100 / row['favodds'])  
    elif row['favodds'] > 0:
        return 1 + (row['favodds'] / 100)
    return 1  # If favodds is 0, handle it

# Apply the function to each row
df['favodds_dec'] = df.apply(convert_favodds_to_dec, axis=1)

# Function to convert boosted udogsodds to decimal
def convert_udogsodds_to_dec(row):
    if row['udogsodds_boosted'] < 0:
        return 1 - (100 / row['udogsodds_boosted']) 
    elif row['udogsodds_boosted'] > 0:
        return 1 + (row['udogsodds_boosted'] / 100)
    return 1  # If udogsodds_boosted is 0, handle it

# Apply the function to each row
df['udogsodds_dec'] = df.apply(convert_udogsodds_to_dec, axis=1)

def calculate_profits(row):
    udogsodds_mult = row['udogsodds_dec']  # Assuming udogsodds_dec has been calculated
    favodds_mult = row['favodds_dec']  # Assuming favodds_dec has been calculated

    # Calculate hedge bet amount on the non-boosted app (m2)
    m2 = m1 * udogsodds_mult / favodds_mult

    # Calculate profit if underdog wins
    win = (m1 * (udogsodds_mult - 1)) - m2

    # Calculate additional profit due to boost
    profitboost_val = m1 * (udogsodds_mult - 1)
    boost_val = profitboost_val / max_boostwin * 100

    return pd.Series({
        'm2': m2,
        'win': win,
        'profitboost_val': profitboost_val,
        'boost_val': boost_val
    })

# Apply the function to each row
df[['m2', 'win', 'profitboost_val', 'boost_val']] = df.apply(calculate_profits, axis=1)

df_sorted = df.sort_values(by='win', ascending=False)
print(df_sorted)



'''

m2 = m1 * udogsodds_mult / favodds_mult # calculate how much to hedge on other app (non boosted app)

win = ( m1 * ( udogsodds_mult - 1 ) ) - m2 # profit if udog wins
#win = ( m2 * ( favodds_mult - 1 ) ) - m1 # profit if fav wins


profitboost_val = m1 * ( udogsodds_mult - 1 ) # how much additional profit you are getting because of the boost by betting the same amount of "max bet" 
boost_val = profitboost_val/max_boostwin * 100 # how much of the max boost win you are using

# questions
# does boost_val correlate to boost_val

print(f"profit = {win}")
print(f"boost_val = {boost_val}")
'''