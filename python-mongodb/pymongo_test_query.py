from pymongo_get_database import get_database
from pandas import DataFrame

dbname = get_database()
collection_name = dbname["user_1_items"]

item_details = collection_name.find()

# convert the dictionary objects to dataframe
items_df = DataFrame(item_details)

# see the magic
print(items_df)