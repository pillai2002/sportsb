import pandas as pd

favodds = -215
udogsodds = 170



m1 = 25 # max bet of account with profit boost based on t&c of bookie
boost = 100 # profit boost in percentage
max_boostwin = 275 # maximum you can gain on the boost based on t&c of bookie


boost_mult = boost/100 + 1

# calculating boosted udogsoddds
if( udogsodds > 0 ):
    udogsodds_boosted = udogsodds * boost_mult
elif( udogsodds < 0 ):
    udogsodds_boosted = udogsodds / boost_mult


# converting favodds to dec
if( favodds < 0 ):
    favodds_mult = 1 - ( 100/favodds )
elif( favodds > 0 ):
    favodds_mult = 1 + ( favodds/100 )

# converting udogsodds_boosted to dec
if( udogsodds_boosted < 0 ):
    udogsodds_mult = 1 - ( 100/udogsodds_boosted )
elif( udogsodds_boosted > 0 ):
    udogsodds_mult = 1 + ( udogsodds_boosted/100 )



m2 = m1 * udogsodds_mult / favodds_mult # calculate how much to hedge on other app (non boosted app)

win = ( m1 * ( udogsodds_mult - 1 ) ) - m2 # profit if udog wins
#win = ( m2 * ( favodds_mult - 1 ) ) - m1 # profit if fav wins


profitboost_val = m1 * ( udogsodds_mult - 1 ) # how much additional profit you are getting because of the boost by betting the same amount of "max bet" 
boost_val = profitboost_val/max_boostwin * 100 # how much of the max boost win you are using

# questions
# does boost_val correlate to boost_val

print(f"profit = {win}")
print(f"boost_val = {boost_val}")








