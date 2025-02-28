import sqlalchemy as sql
import pandas as pd

# mention correct path after sqlite:///
engine = sql.create_engine("sqlite:///./mock4/mock_roe_4/violations.db")
db_data = pd.read_sql("select * from violations", engine)

# db_data contains the data from the database in dataframe.
# use directly till here to use in your code.

# Display the first 5 rows of the DataFrame
db_data.to_csv('./processed_files/violations.csv', index=False)