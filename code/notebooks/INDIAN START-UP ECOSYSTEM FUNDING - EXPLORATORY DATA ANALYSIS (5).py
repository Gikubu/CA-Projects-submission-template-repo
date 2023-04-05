# %% [markdown]
# ## PROJECT SCENARIO
# The company is trying to venture into the Indian start-up ecosystem. As the data experts of the company, we are to investigate the ecosystem and propose the best course of action

# %% [markdown]
# ## PROJECT DESCRIPTION
# In this project, We are going to analyze funding received by start-ups in India from 2018 to 2021. Data for each year of funding is located in a separate csv file in the dataset provided. In these files are the start-ups' details, the funding amounts received, and the investors' information.
# 
# As Data Analysts for this project, we are required to explore the datasets, clean and prepare the datasets, analyze the final prepared dataset and tell compelling stories with intuitive and appropraite visulaizations

# %% [markdown]
# 
# 
# ## BUSINESS QUESTIONS
# 1. Which Industries/sectors received the most and least funding from investors?
# 2. What are the top five (5) cities with the most start-ups?
# 3. What are the top (10) start-ups with most funding?
# 4. Who are the leading or top investors in the Indian start-up ecosystem by number of investments made?
# 5. What is the trend of funding in the Indian start-up ecosystem?
# 6. Which stage of funding did start-ups receive the most funding?
# 7. Which investors invested the biggest funds in a particular field?

# %% [markdown]
# # IMPORTING THE REQUIRED LIBRARIES AND LOADING THE FUNDING DATASETS

# %%
# Import libraries

import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
plt.style.use("fivethirtyeight")
import seaborn as sns
import math
import plotly.express as px

import warnings
warnings.filterwarnings("ignore")

%matplotlib inline

# %%
# Import funding datasets

funding_2018 = pd.read_csv("C:\\Users\PC\\DATA_ANALYTICS_AA\\DATA_ANALYTICS_AA\\PROJECT_PHASE\\PROJECT_1\\DATASET\\startup_funding2018.csv")
funding_2019 = pd.read_csv("C:\\Users\PC\\DATA_ANALYTICS_AA\\DATA_ANALYTICS_AA\\PROJECT_PHASE\\PROJECT_1\\DATASET\\startup_funding2019.csv")
funding_2020 = pd.read_csv("C:\\Users\PC\\DATA_ANALYTICS_AA\\DATA_ANALYTICS_AA\\PROJECT_PHASE\\PROJECT_1\\DATASET\\startup_funding2020.csv")
funding_2021 = pd.read_csv("C:\\Users\PC\\DATA_ANALYTICS_AA\\DATA_ANALYTICS_AA\\PROJECT_PHASE\\PROJECT_1\\DATASET\\startup_funding2021.csv")

# %% [markdown]
# ### EXPLORING THE 2018 FUNDING DATASET

# %%
# Description funds for 2018

funding_2018.head()

# %% [markdown]
# ### checking the basic info of the dataset

# %%
# Checking the shape of the dataset

funding_2018.shape

print("The 2018 Funding data contains " ,funding_2018.shape[0], "rows and " ,funding_2018.shape[1], "columns")

# %%
# Checking the info of the 2018 dataset

funding_2018.info()

# %%
# Checking brief description of the 2018 dataset

funding_2018.describe(include="all").transpose()

# %%
# Checking for NaN values in the dataset

funding_2018.isna().any()

# %%
# Checking for null values in the dataset

funding_2018.isnull().any()

# %% [markdown]
# ### Checking for duplicate(s) in the dataset

# %%
# Checking for duplicates in the 2018 funding dataset

funding_2018.duplicated().sum()

# %%
# Checking for duplicated entry

funding_2018[funding_2018.duplicated()]

# %% [markdown]
# ### Investigating the issue of duplicated value in the dataset

# %%
# Investigating the duplicated entry
funding_2018[funding_2018["Company Name"]=="TheCollegeFever"]

# %% [markdown]
# #### Overview of the "AMOUNT" column

# %%
# Checking the Amount column
funding_2018["Amount"]

# %% [markdown]
# ### Cross-checking selected columns for errors

# %%
# Further cross-checking of selected columns

pd.set_option('display.max_rows', None)
funding_2018[["Company Name", "Industry", "Round/Series", "Location"]]


# %% [markdown]
# ### EXPLORING THE 2019 FUNDING DATASET
# 

# %%
funding_2019.head()

# %% [markdown]
# ### Checking the basic info of the dataset

# %%
# Cheking the shape of the dataset

funding_2019.shape

print("The 2019 Funding data contains " ,funding_2019.shape[0], "rows and " ,funding_2019.shape[1], "columns")

# %%
# Checking the basic info of the dataset

funding_2019.info()

# %%
# Cecking the summary description of 2019 funding data

funding_2019.describe(include="all").transpose()

# %%
# Checking for NaN values

funding_2019.isna().any()

# %%
# Checking for the number of NaN values

funding_2019.isna().sum()

# %% [markdown]
# ##### From the above, it can be evidenced that there are NaN values in the dataset that need to be computed. The process of treating null values can be found in the "RESOLVING ISSUES RAISED FROM THE DATASET" markdown cell

# %% [markdown]
# ### Checking for duplicate(s) in the dataset

# %%
# Checking for duplicated values

funding_2019.duplicated().any()


# %% [markdown]
# ##### From the above, there were no duplicated values in the dataset

# %% [markdown]
# ### Selecting and Highlighting columns for errors

# %%
# Cross-checking selected columns for errors

pd.set_option('display.max_rows', None)
funding_2019[["Company/Brand", "Sector", "Investor", "Stage"]]

# %% [markdown]
# ### EXPLORING 2020 FUNDING DATA

# %%
funding_2020.head()

# %% [markdown]
# ### Checking the basic info of the dataset

# %%
# Checking the shape of the data

funding_2020.shape

print("The 2020 Funding data contains " ,funding_2020.shape[0], "rows and " ,funding_2020.shape[1], "columns")

# %%
# Checking the basic info of the dataset

funding_2020.info()

# %%
funding_2020.isnull().any()

# %%
funding_2020.isnull().sum()

# %% [markdown]
# #####  From the information above, it can be realised that there are NaN values in the dataset that needs to be woked. The process of treating NaN values is outlined in the "RESOLVING ISSUES RAISED FROM THE DATASET" markdown cell

# %%
# Checking the statistical description of the dataset

funding_2020.describe().transpose()

# %% [markdown]
# ### Highlghting and Investigating the unnamed column

# %%
# Investigating the unnamed column:9

pd.set_option('display.max_rows', None)
funding_2020["Unnamed: 9"]

# %% [markdown]
# ### Selecting  columns to investigate for errors

# %%
# Cross-checking selcted columns

pd.set_option('display.max_rows', None)
funding_2020[["Company/Brand", "Sector", "Investor", "Stage", "HeadQuarter"]]

# %% [markdown]
# ### Checking for duplicate values in the dataset

# %%
# Checking for duplicated values

funding_2020.duplicated().any()

# %%
# Summary number of duplicated values

funding_2020.duplicated().sum()

# %% [markdown]
# ##### From the above, it can be recognised that there are three(3) duplicated values in the dataset

# %% [markdown]
# ### Highlighting the duplicated values in the dataset

# %%
#Checking duplicated start-ups

funding_2020[funding_2020.duplicated()]

# %% [markdown]
# ### Investigating the issue of duplicated values in the dataset

# %%
# Highlighting and investigating duplicated value  - "Krimanshi"

funding_2020[funding_2020["Company/Brand"]=="Krimanshi"]

# %%
# Highlighting and investigating duplicated value -- Nykaa

funding_2020[funding_2020["Company/Brand"]=="Nykaa"]

# %%
# Highlighting and investigating duplicated value -- Byju’s

funding_2020[funding_2020["Company/Brand"]=="Byju’s"]

# %% [markdown]
# ### EXPLORING 2021 FUNDING DATASET
# 

# %%
# Checking the head of the data

funding_2021.head()

# %%
# Cecking the tail of the data

funding_2021.tail()

# %% [markdown]
# ### Checking the basic info of the dataset

# %%
# Checking the shape of the data

funding_2021.shape

print("The 2021 Funding data contains " ,funding_2021.shape[0], "rows and " ,funding_2021.shape[1], "columns")

# %%
# Checking the basic info of the data

funding_2021.info()

# %%
# Summary statistical description of the data

funding_2021.describe(include="all").transpose()

# %% [markdown]
# ### Checking for NaN values

# %%
# Checking for NaN values

funding_2021.isna().any()

# %%
# Finding the sum of total of missing values
funding_2021.isna().sum()

# %% [markdown]
# ##### From the information above, it can be realised that there are NaN values in the dataset that needs to be woked. The process of treating NaN values is outlined in the "RESOLVING ISSUES RAISED FROM THE DATASET" markdown cell

# %%
pd.set_option('display.max_rows', None)
funding_2021[["Company/Brand", "Sector", "Investor", "Stage", "HeadQuarter"]]

# %% [markdown]
# ### Checking for duplicated values

# %%
# Checking for duplicated values

funding_2021.duplicated().any()

# %%
print ("There are ",len(funding_2021[funding_2021.duplicated()]) ,"duplicated values in the dataset")

# %% [markdown]
# ### Highlight the duplicated values in the dataset

# %%
# highlingting duplicated values

funding_2021[funding_2021.duplicated()]

# %% [markdown]
# ### Investigating the issue of duplicated values

# %%
# Investigating duplicated values  ---  "Curefoods"

funding_2021[funding_2021["Company/Brand"]=="Curefoods"]

# %%
# Investigating duplicated values  ---  "Bewakoof"

funding_2021[funding_2021["Company/Brand"]=="Bewakoof"]

# %%
# Investigating duplicated values  ---  "FanPlay"

funding_2021[funding_2021["Company/Brand"]=="FanPlay"]

# %%
# Investigating duplicated values  ---  "Advantage Club"

funding_2021[funding_2021["Company/Brand"]=="Advantage Club"]

# %%
# Investigating duplicated values  ---  "Ruptok"

funding_2021[funding_2021["Company/Brand"]=="Ruptok"]

# %%
# Investigating duplicated values  ---  "Trinkerr"

funding_2021[funding_2021["Company/Brand"]=="Trinkerr"]

# %%
# Investigating duplicated values  ---  "Zorro"

funding_2021[funding_2021["Company/Brand"]=="Zorro"]

# %%
# Investigating duplicated values  ---  "Ultraviolette"

funding_2021[funding_2021["Company/Brand"]=="Ultraviolette"]

# %%
# Investigating duplicated values  ---  "NephroPlus"

funding_2021[funding_2021["Company/Brand"]=="NephroPlus"]

# %%
# Investigating duplicated values  ---  "Unremot"

funding_2021[funding_2021["Company/Brand"]=="Unremot"]

# %%
# Investigating duplicated values  ---  "FanAnywhere"

funding_2021[funding_2021["Company/Brand"]=="FanAnywhere"]

# %%
# Investigating duplicated values  ---  "PingoLearn"

funding_2021[funding_2021["Company/Brand"]=="PingoLearn"]

# %%
# Investigating duplicated values  ---  "Spry"

funding_2021[funding_2021["Company/Brand"]=="Spry"]

# %%
# Investigating duplicated values  ---  "Enmovil"

funding_2021[funding_2021["Company/Brand"]=="Enmovil"]

# %%
# Investigating duplicated values  ---  "ASQI Advisors"

funding_2021[funding_2021["Company/Brand"]=="ASQI Advisors"]

# %%
# Investigating duplicated values  ---  "Insurance Samadhan"

funding_2021[funding_2021["Company/Brand"]=="Insurance Samadhan"]

# %%
# Investigating duplicated values  ---  "Evenflow Brands"

funding_2021[funding_2021["Company/Brand"]=="Evenflow Brands"]

# %%
# Investigating duplicated values  ---  "MasterChow"

funding_2021[funding_2021["Company/Brand"]=="MasterChow"]

# %%
# Investigating duplicated values  ---  "Fullife Healthcare"

funding_2021[funding_2021["Company/Brand"]=="Fullife Healthcare"]

# %% [markdown]
# ## ISSUES WITH THE DATA
# #### FUNDING YEAR 2018
# 1. Amount has datatype as object. It should be a float data type
# 2. There are different currencies in the Amount column. All currencies are supposed to be in dollars. There are commas in certain values.
# 3. There are Non-Avalaible Values(NaN) in the dataset
# 4. Company names mixed with website
# 5. There is a google document link in the Rounds/Series column
# 6. The "About" column has no influence on our analysis so hence must be removed.
# 7. There is 1 duplicated information in the dataset(Company Name = TheCollegeFever)
# 8. Location column is not consistent with the rest of the dataset. It contained city, State, and Country.
# 9. There are locations that contain India, Asia. This will be replaced with the most recurring city.
# 
# #### FUNDING YEAR 2019
# 1. There are lots NaN values*** in the Stage, HeadQuaters and Founded columns
# 2. There is the currency sign and commas attached to the amounts.
# 3. What the company does has no influence on our data.
# 4. The Founded Column is in float
# 5. Amount column is in object.
# 6. The Founder columnn is not important to our analysis
# 7. Company/Brand column must be renamed to Company
# 
# #### FUNDING YEAR 2020
# 1. Company/Brand column must be renamed to Company
# 2. Column, "Unnamed:9" has no influence on our dataset
# 3. There is the currency sign and commas attached to the amounts.
# 4. Spelling error (>Vikram Sud, column=192) in the investor column
# 5. There are Headquaters cities that are outside India.
# 6. Duplicated three entries (Byju’s, Nykaa, Krimanshi)
# 7. Columns with names of cities and state.
# 
# #### FUNDING YEAR 2021
# 1. Company/Brand column must be renamed to Company
# 2. There is the currency sign and commas attached to the amounts.
# 3. HeadQuaters changed to Location
# 4. There are lots of NaN values
# 5. There are duplicated values (Curefoods, Bewakoofs, FanPlay, Advantage Club, Ruptok, Trinker, Zorro, Ultraviollette, Nephroplus, Unremot, Fansanywhere,Pingolearn, Spy, Enmovil, ASQI Advisers, Insurance Samadhan, Evenflow Brands, MasterChow, Fullife healthcare)
# 6. There are instances where values have been recorded under the wrong columns

# %% [markdown]
# ### RESOLVING ISSUES RAISED FROM THE DATASET
# 1. Write python functions and pandas codes to remove currency symbols, empty spaces and commas in the numeric values.
# 2. Write python functions and codes to covert datatype of numeric values recorded as objects(string) to floats or ints.
# 3. Replace all categorical null and NaN values with Unknown or Undisclosed.
# 4. Remove columns that will have no bearing on the analysis.
# 5. Provide a common name for values with same meaning in the Stage column
# 6. Change HeadQuarters column name to Location
# 7. Remove hedquaters cities that are outside India
# 8. Use Mode to fill missing or NaN numeric values. Missing and NaN values are almost half of the data and cannot be dropped.
# 9. Locations that contain names of cities, states and country will be replaced with only names of cities
# 10. Row 78, location will be changed to Chennai, row 161 location will be changed to Jaipur, row 184 chnage location to Dhingsara, row 282 change location to Trivanduram, row 284 change location to Samastipor, row 288 change location to Tomkor
# 11. Remove duplicated values.

# %% [markdown]
# ## DATA CLEANING AND PREPARATION
# 
# 1. All identified errors or issues in the dataset will be corrected in the cleaning process.
# 2. The datasets will be concactenanted into a single dataset

# %% [markdown]
# ### CLEANING THE 2018 FUNDING DATASET

# %%
funding_2018.head()

# %% [markdown]
# ### DROP IRRELEVANT COLUMNS
# The "About Company" column is irrelevant to our analysis, hence, we have decided to drop it

# %%
funding_2018.drop("About Company", axis=1, inplace=True)

# %% [markdown]
# ### RENAMING COLUMNS

# %%
funding_2018 = funding_2018.rename(columns={"Company Name" : "Company", "Round/Series" : "Stage", "Industry" : "Sector",
                                           "Amount" : "Amount($)"})

# %%
funding_2018.head()

# %% [markdown]
# ### CLEANING THE "COMPANY" COLUMN

# %%
# Splitting special characters in the company names

funding_2018["Company"] = funding_2018["Company"].str.split(".").str[0]
funding_2018["Company"] = funding_2018["Company"].str.split("/").str[0]
funding_2018["Company"] = funding_2018["Company"].str.split("(").str[0]
funding_2018["Company"] = funding_2018["Company"].str.split("!").str[0]
funding_2018["Company"] = funding_2018["Company"].str.split("/").str[0]

# %%
funding_2018["Company"] = funding_2018["Company"].str.strip("&")

# %% [markdown]
# ### CLEANING THE  SECTOR COLUMN

# %%
# Inputing empty spaces with "Uknown"

funding_2018['Sector'] = funding_2018['Sector'].str.replace('—', 'Unknown')

# %% [markdown]
# ### CLEANING THE STAGE COLUMN

# %% [markdown]
# #### Renaming "Venture - Series Unknown" to "Venture"

# %%
funding_2018["Stage"] = funding_2018["Stage"].replace({"Venture - Series Unknown"  : "Venture"})

# %% [markdown]
# #### Replacing the google document link with "Undiscloed"

# %%
funding_2018["Stage"] = funding_2018["Stage"].drop(labels=178)
funding_2018["Stage"] = funding_2018["Stage"].fillna("Undisclosed")

# %% [markdown]
# ### CLEANING THE AMOUNT COLUMN

# %% [markdown]
# #### Removing special characters ("," , "$", "-") and Inputing empty rows with 0. 
# 

# %%
funding_2018["Amount($)"].replace(",", "", regex=True, inplace=True)
funding_2018["Amount($)"].replace("$", "", regex=True, inplace=True)
funding_2018["Amount($)"].replace("—", 0, regex=True, inplace=True)

# %% [markdown]
# #### Creating a temporary column for computations

# %%
funding_2018['INR Amount'] = funding_2018['Amount($)'].str.split('₹').str[1]
#pd.set_option('display.max_rows',None)
funding_2018["INR Amount"].head()

# %% [markdown]
# #### Converting Indian Rupees to Dollar
# 
# A conversion rate of 1 India Rupee to 0.0121 US Dollars was used.

# %%
funding_2018['INR Amount'] = funding_2018['INR Amount'].apply(float).fillna(0)
funding_2018['USD Amount'] = funding_2018['INR Amount'] * 0.0121
funding_2018['USD Amount'] = funding_2018['USD Amount'].replace(0, np.nan)
funding_2018['USD Amount'] = funding_2018['USD Amount'].fillna(funding_2018['Amount($)'])
funding_2018["Amount($)"] = funding_2018["USD Amount"].apply(lambda x: float(str(x).replace("$","")))
funding_2018["Amount($)"].head()
 


# %% [markdown]
# #### Drop new columns that were created to convert Indian Rupees to Dollars

# %%
funding_2018.drop(["INR Amount", "USD Amount"], axis=1, inplace=True)

# %% [markdown]
# #### Cross-checking the Amount column

# %%
funding_2018["Amount($)"].head()

# %% [markdown]
# ### CLEANING THE LOCATION COLUMN
# 
# From our research, we realized that the Location contained names of Cities, States and Country. Hence, we decided to strip the State and Country. This will ensure that only the Cities remain the values in the Location column.

# %% [markdown]
# #### Removing the States and Country from the Location column

# %%
funding_2018["Location"]=funding_2018['Location'].str.split(',').str[0]

# %% [markdown]
# #### Re-computing the names of cities with errors

# %%
# Inputing the right names of cities

funding_2018["Location"] = funding_2018['Location'].replace("Bangalore", "Bengaluru")
funding_2018["Location"] = funding_2018['Location'].replace("Delhi", "New Delhi")
funding_2018["Location"] = funding_2018['Location'].replace("Bangalore City", "Bengaluru")


# Uttar Prasdesh is a State, we computed it with the Capital, Noida, which is in the dataset
funding_2018["Location"] = funding_2018['Location'].replace("Uttar Pradesh", "Noida")


# India is present in the dataset. However, India is not a City, hence, we will replace it "Unknown")
funding_2018["Location"] = funding_2018['Location'].replace("India", "Unknown")

# %% [markdown]
# ### WORKING ON DUPLICATED VALUES

# %%
# Checking for duplicated value

funding_2018[funding_2018.duplicated()]

# %%
# Investigating the issue of the duplicate

funding_2018[funding_2018["Company"]=="TheCollegeFever"]

# %% [markdown]
# #####  From the dataframe above, this a duplicated entry containing the same values in all the columns. Hence, the duplicate will be dropped from the funding dataframe

# %%
# Removing the incidence of the duplicated value

funding_2018 = funding_2018.drop_duplicates(subset=None, keep="first")

# %%
# Cross-checking the removal of the duplicated value

funding_2018.duplicated().any()

# %%
# Cross-checking the removal of the duplicated value

funding_2018[funding_2018["Company"]=="TheCollegeFever"]

# %% [markdown]
# ### ADD FUNDING YEAR COLUMN TO DATASET FOR ANALYSIS

# %%
funding_2018["funding_year"] = 2018

# %% [markdown]
# #### Re-checking the basic info of the 2018 funding dataset

# %%
funding_2018.info()

# %% [markdown]
# ### VERIFYING THE CLEANED 2018 FUNDING DATASET

# %%
funding_2018.head()

# %% [markdown]
# # CLEANING THE 2019 FUNDING DATASET

# %%
funding_2019.head()

# %% [markdown]
# ### REMOVING COLUMNS THAT ARE NOT IMPORTANT TO OUR ANALYSIS

# %%
# Dropping the "Founded" column
funding_2019.drop("Founded", axis=1, inplace=True)

# Dropping the "What it does" column
funding_2019.drop("What it does", axis=1, inplace=True)

# Dropping the "Founded" column
funding_2019.drop("Founders", axis=1, inplace=True)



# %% [markdown]
# ### RENAMING COLUMNS TO CONFORM WITH THE REST OF THE FUNDING DATASET

# %%
funding_2019 = funding_2019.rename(columns={"Company/Brand" : "Company", "HeadQuarter" : "Location"})

# %%
funding_2019.head()

# %% [markdown]
# ### WORKING ON THE COMPANY COLUMN

# %%
# Correcting the names of companies displayed as websites

funding_2019 = funding_2019.replace("Observe.AI", "Observe AI")
funding_2019 = funding_2019.replace("m.Paani", "Paani")
funding_2019 = funding_2019.replace("Nivesh.com", "Nivesh")
funding_2019 = funding_2019.replace("Infra.Market", "Infra Market")
funding_2019 = funding_2019.replace("Infra.Market", "Infra Market")
funding_2019 = funding_2019.replace("Fireflies .ai", "Fireflies")

# %% [markdown]
# ### WORKING ON THE LOCATION COLUMN

# %%
# Filling NaN values with "Unknown"
funding_2019 = funding_2019.fillna("Unknown")

# Replacicng "Bangalore" with "Bengaluru"
funding_2019 = funding_2019.replace("Bangalore", "Bengaluru")

# Replacicng "Uttar Pradesh" with "Noida"
funding_2019 = funding_2019.replace("Uttar pradesh", "Noida")

# Replacicng "Delhi" with "New Delhi"
funding_2019 = funding_2019.replace("Delhi", "New Delhi")

funding_2019 = funding_2019.replace("Uknown", "Unknown")

# %% [markdown]
# ### WORKING ON THE SECTOR COLUMN

# %%
# Replacing "&" with ","

funding_2019["Sector"] = funding_2019["Sector"].replace("&", ",", regex=True)

# %% [markdown]
# #### Correcting the Names of Sectors 

# %%
# Replacing "Tech" as a Sector with "Technology"

funding_2019 = funding_2019.replace("AI , Tech", "AI , Technology", regex=True)

# Replacing "Food , tech" with "FoodTech"
funding_2019 = funding_2019.replace("Food , tech", "FoodTech", regex=True)

# Replacing "Food tech" with "FoodTech"
funding_2019 = funding_2019.replace("Food tech", "FoodTech", regex=True)

# Replacing "Foodtech" with "FoodTech"
funding_2019 = funding_2019.replace("Foodtech", "FoodTech", regex=True)

# %% [markdown]
# ### WORKING ON THE INVESTOR COLUMN

# %%
# Stripping "." from the end of certain investor names

funding_2019["Investor"] = funding_2019["Investor"].str.strip(".")

# %% [markdown]
# ### WORKING ON THE AMOUNT COLUMN 

# %%
funding_2019["Amount($)"].head()

# %% [markdown]
# #### Take off special symbols("," and "$")

# %%
funding_2019["Amount($)"] = funding_2019["Amount($)"].apply(lambda x: str(x).replace(",", ""))
funding_2019["Amount($)"] = funding_2019["Amount($)"].apply(lambda x: str(x).replace("$", ""))

# %% [markdown]
# #### Change undisclosed amonts to zero(0)

# %%
funding_2019["Amount($)"] = funding_2019["Amount($)"].replace("Undisclosed", 0)
funding_2019["Amount($)"] = funding_2019["Amount($)"].fillna(0)

# %% [markdown]
# #### Change the datatype of Amount column

# %%
funding_2019["Amount($)"] = funding_2019["Amount($)"].astype(float)
funding_2019["Amount($)"].head()

# %% [markdown]
# ## WORKING ON THE STAGE COLUMN

# %% [markdown]
# #### Replace NaN values with "Udisclosed"

# %%
funding_2019["Stage"] = funding_2019["Stage"].fillna("Undisclosed")

# %% [markdown]
# #### Correcting inconsistencies in the values in the stage column

# %%
# Replace "Pre Series A" with "Pre-Series A"
funding_2019["Stage"] = funding_2019["Stage"].replace("Pre series A", "Pre-series A")

# Replace "Seed funding" with "Seed fund"
funding_2019["Stage"] = funding_2019["Stage"].replace("Seed funding", "Seed")

# Replace "Seed round" with "Seed fund"
funding_2019["Stage"] = funding_2019["Stage"].replace("Seed round", "Seed")

# Replace "Post seies A" with "Post-series A"
funding_2019["Stage"] = funding_2019["Stage"].replace("Post series A", "Post-series A")

# %% [markdown]
# ### CHECKING FOR DUPLICATED VALUES

# %%
funding_2019.duplicated().any()

# %% [markdown]
# #### Checking for the occurrence of duplicate

# %%
funding_2019[funding_2019.duplicated()]

# %% [markdown]
# #### Investigating the occurrence of the duplicated entry

# %%
funding_2019[funding_2019["Company"] == "Kratikal"]

# %% [markdown]
# ##### From the above, it can be concluded that the entry is a duplicated entry with the same values in all the colums

# %% [markdown]
# #### Working on the duplicated entry

# %%
# Removing the duplicated entry

funding_2019 = funding_2019.drop_duplicates()

# %%
# Cross-checking for the removal of duplicated entry

funding_2019.duplicated().any()

# %% [markdown]
# ### ADD YEAR COLUMN TO DATASET FOR FURTHER ANALYSIS

# %%
funding_2019["funding_year"] = 2019

# %% [markdown]
# ### cross-checking the basic info of dataset

# %%
funding_2019.info()

# %% [markdown]
# ### VERIFYING THE CLEANED 2019 FUNDING DATASET

# %%
funding_2019.head()

# %% [markdown]
# ## CLEANING THE 2020 FUNDING DATASET

# %%
funding_2020.head()

# %% [markdown]
# ### REMOVING COLUMNS THAT ARE IRRELEVANT TO OUR ANALYSIS

# %%
# Dropping the "Founded" column
funding_2020 = funding_2020.drop(columns="Founded", axis=1)

# Dropping the "What it does" column
funding_2020 = funding_2020.drop(columns="What it does", axis=1)

# Dropping the "Founders" column
funding_2020 = funding_2020.drop(columns="Founders", axis=1)

# Dropping the "Unnamed: 9" column
funding_2020 = funding_2020.drop(columns="Unnamed: 9", axis=1)


# %% [markdown]
# ### RENAMING COLUMN HEADS TO BE CONSISTENT WITH THE REST OF DATA

# %%
# Rename Company/Brand and HeadQuarter columns to conform with the rest of the data

funding_2020 = funding_2020.rename(columns={"Company/Brand" : "Company", "HeadQuarter" : "Location"})

# %% [markdown]
# ### WORKING ON THE COMPANY COLUMN

# %% [markdown]
# #### Correcting Names of Companies to remove special characters

# %%
# Correcting "OurEye.ai"
funding_2020["Company"] = funding_2020["Company"].replace("OurEye.ai", "OurEye AI")

# Correcting "TaxBuddy.com"
funding_2020["Company"] = funding_2020["Company"].replace("TaxBuddy.com", "TaxxBuddy")

# Correcting "Callify.ai"
funding_2020["Company"] = funding_2020["Company"].replace("Callify.ai", "Callify AI")

# Correcting "Artivatic.ai"
funding_2020["Company"] = funding_2020["Company"].replace("Artivatic.ai", "Artivatic AI")

# Correcting "Infra.Market"
funding_2020["Company"] = funding_2020["Company"].replace("Infra.Market", "Infra Market")

# Correcting "Tamasha.live" 
funding_2020["Company"] = funding_2020["Company"].replace("Tamasha.live", "Tamasha")

# Correcting "Rephrase.ai" 
funding_2020["Company"] = funding_2020["Company"].replace("Rephrase.ai", "Rephrase AI")

# Correcting "Observe ai" 
funding_2020["Company"] = funding_2020["Company"].replace("Observe ai", "Observe AI")

# Correcting "Apna.co" 
funding_2020["Company"] = funding_2020["Company"].replace("Apna.co", "Apna")

# Correcting "Phool.co" 
funding_2020["Company"] = funding_2020["Company"].replace("Phool.co", "Phool")

# Correcting "Univ.ai" 
funding_2020["Company"] = funding_2020["Company"].replace("Univ.ai", "Univ AI")

# Correcting "Verloop.io" 
funding_2020["Company"] = funding_2020["Company"].replace("Verloop.io", "Verloop")

# Correcting "Locale ai" 
funding_2020["Company"] = funding_2020["Company"].replace("Locale ai", "Locale AI")


# Correcting "Byju" 
funding_2020["Company"] = funding_2020["Company"].replace("Byju", "Byju's")

# Correcting "Vernacular ai" 
funding_2020["Company"] = funding_2020["Company"].replace("Vernacular ai", "Vernacular AI")

# Correcting "Qure ai" 
funding_2020["Company"] = funding_2020["Company"].replace("Qure ai", "Qure AI")

# %% [markdown]
# ### WORKING ON THE LOCATION COLUMN

# %% [markdown]
# #### correcting the names of cities to conform with other datasets

# %%
# Rename "Bangalore" to "Bengaluru"
funding_2020["Location"] = funding_2020["Location"].replace("Bangalore", "Bengaluru")

# Split cities from states
funding_2020["Location"] = funding_2020["Location"].str.split(',').str[0]

# Fill NaN values with "Unknown"
funding_2020["Location"] = funding_2020["Location"].fillna("Unknown")

# Rename "Delhi" to "New Delhi"
funding_2020["Location"] = funding_2020["Location"].replace("Delhi", "New Delhi")

# Rename "Uttar Pradesh" to "Noida" Tamil Nadu
funding_2020["Location"] = funding_2020["Location"].replace("Uttar Pradesh", "Noida")

# Rename "Tamil Nadu(State)" to "Trivandrum(City)" 
funding_2020["Location"] = funding_2020["Location"].replace("Tamil Nadu", "Trivandrum")

# %% [markdown]
# #### We acknowledege that the location column contains names of cities outside India. These are the Headqauters locations of their corresponding companies. 
# #### We suppose that these companies have subsidiary start-ups in India, and their corresponding details, which are, "sector", "Investor", "Amount" and "Stage" are accurate.
# #### Hence, we decided not to remove these entries since it may have significant impact on our analysis

# %% [markdown]
# ### WORKING ON THE SECTOR COLUMN

# %% [markdown]
# #### Rename start-ups to be consistent with rest of data

# %%
# Replace "&", "/" with ","
funding_2020["Sector"] = funding_2020["Sector"].str.replace("&", ",")
funding_2020["Sector"] = funding_2020["Sector"].str.replace("/", " , ")


# Remove startup, company, platform, Industry, from names of sector to make it uniform with th rest of the funding dataset
funding_2020["Sector"] = funding_2020["Sector"].str.replace("startup", "")
funding_2020["Sector"] = funding_2020["Sector"].str.replace("Startup", "")
funding_2020["Sector"] = funding_2020["Sector"].str.replace("company", "")
funding_2020["Sector"] = funding_2020["Sector"].str.replace("platform", "")
funding_2020["Sector"] = funding_2020["Sector"].str.replace("Industry", "")
funding_2020["Sector"] = funding_2020["Sector"].str.replace("Company", "")

# Relace NaN values with "Unkknown"
funding_2020["Sector"] = funding_2020["Sector"].fillna("Unknown")


# %%
# Replace "tech" with "Tech" for uniformity
funding_2020["Sector"] = funding_2020["Sector"].replace("tech", "Tech", regex=True) 

# %%
# More on correction of sector names

funding_2020["Sector"] = funding_2020["Sector"].replace({"EdtTech" : "EdTech"})
funding_2020["Sector"] = funding_2020["Sector"].replace({"Soil-Tech" : "SoilTech"})
funding_2020["Sector"] = funding_2020["Sector"].replace({"Insurtech" : "InsureTech"})
funding_2020["Sector"] = funding_2020["Sector"].replace({"Agritech" : "AgriTech"})
funding_2020["Sector"] = funding_2020["Sector"].replace({"Tech" : "Technology"})
funding_2020["Sector"] = funding_2020["Sector"].replace({"Ecommerce" : "E-commerce"})
funding_2020["Sector"] = funding_2020["Sector"].replace({"E store" : "E-Store"})
funding_2020["Sector"] = funding_2020["Sector"].replace({"Estore" : "E-Store"})
funding_2020["Sector"] = funding_2020["Sector"].replace({"Food Tech" : "FoodTech"})
funding_2020["Sector"] = funding_2020["Sector"].replace({"Social commerce" : "Social e-commerce"})

# %% [markdown]
# ### WORKING ON THE AMOUNT COLUMN

# %% [markdown]
# #### Remove special signs from amount

# %%
funding_2020["Amount($)"] = funding_2020["Amount($)"].str.replace(",", "")
funding_2020["Amount($)"] = funding_2020["Amount($)"].str.replace("$", "")

# %% [markdown]
# ####  Correct incosistent amounts

# %%
funding_2020["Amount($)"] = funding_2020["Amount($)"].str.replace("887000 23000000", "23000000")
funding_2020["Amount($)"] = funding_2020["Amount($)"].str.replace("800000000 to 850000000", "850000000")

# %% [markdown]
# #### Convert undisclosed and NaN values to 0

# %%
funding_2020["Amount($)"] = funding_2020["Amount($)"].replace("Undisclosed", 0)
funding_2020["Amount($)"] = funding_2020["Amount($)"].replace("Undiclsosed", 0)
funding_2020["Amount($)"] = funding_2020["Amount($)"].replace("Undislosed", 0)
funding_2020["Amount($)"] = funding_2020["Amount($)"].fillna(0)

# %% [markdown]
# #### Change the datatype of amounts to floats

# %%
funding_2020["Amount($)"] = funding_2020["Amount($)"].astype(float)
funding_2020["Amount($)"].head()

# %% [markdown]
# ### WORKING ON THE INVESTOR COLUMN

# %%
# Fill NaN values with "Undisclosed"
funding_2020["Investor"] = funding_2020["Investor"].fillna("Undisclosed")

# Remove special characters
funding_2020["Investor"] = funding_2020["Investor"].str.replace(">", "")
funding_2020["Investor"] = funding_2020["Investor"].str.replace("!", "")
funding_2020["Investor"] = funding_2020["Investor"].str.replace("`", "")

# Correct names of investors
funding_2020["Investor"] = funding_2020["Investor"].replace("ah ! Ventures", "Ah Ventures")
funding_2020["Investor"] = funding_2020["Investor"].replace("Angel investors. HNI", "Angel investors, HNI")
funding_2020["Investor"] = funding_2020["Investor"].replace("Sequoia", "Sequoia Capital")
funding_2020["Investor"] = funding_2020["Investor"].replace("Angellist India", "Angel List India")
funding_2020["Investor"] = funding_2020["Investor"].replace("Angel investors", "Angel Investors")
funding_2020["Investor"] = funding_2020["Investor"].replace("CITE.CO", "IIM Ahmedabad’s incubator (CIIE.CO)")
funding_2020["Investor"] = funding_2020["Investor"].replace("Lightbox. Social Capital, Dunce Capital", "Lightbox, Social Capital, Dunce Capital")




# %% [markdown]
# ### WORKING ON THE STAGE COLUMN

# %% [markdown]
# #### Replace NaN values with "Undisclosed"

# %%
funding_2020["Stage"] = funding_2020["Stage"].fillna("Undisclosed")

# %% [markdown]
# #### Correct names of Stage with errors

# %%
funding_2020["Stage"] = funding_2020["Stage"].replace(" Pre- series A", " Pre-series A")
funding_2020["Stage"] = funding_2020["Stage"].replace("Seed round", "Seed")
funding_2020["Stage"] = funding_2020["Stage"].replace("Seed Round & Series A", "Seed, Series A")
funding_2020["Stage"] = funding_2020["Stage"].replace("Pre Series A", "Pre-series A")
funding_2020["Stage"] = funding_2020["Stage"].replace("Pre seed Round", "Pre-seed")
funding_2020["Stage"] = funding_2020["Stage"].replace("Pre seed round", "Pre-seed")
funding_2020["Stage"] = funding_2020["Stage"].replace("Angel Round", "Angel")
funding_2020["Stage"] = funding_2020["Stage"].replace("Pre series A1", "Pre-series A1")
funding_2020["Stage"] = funding_2020["Stage"].replace("Pre series A", "Pre-series A")
funding_2020["Stage"] = funding_2020["Stage"].replace("Pre series B", "Pre-series B")
funding_2020["Stage"] = funding_2020["Stage"].replace("Series C, D", "Series C, Series D")

# %% [markdown]
# #### Remove classifying descriptions from names of stage

# %%
funding_2020["Stage"] = funding_2020["Stage"].str.replace("Round", "")
funding_2020["Stage"] = funding_2020["Stage"].str.replace("Investment", "")
funding_2020["Stage"] = funding_2020["Stage"].str.replace("funding", "")
funding_2020["Stage"] = funding_2020["Stage"].str.replace("Funding", "")

# %% [markdown]
# ### WORKING ON DUPLICATES

# %%
funding_2020.duplicated().any()

# %% [markdown]
# #### Checking for the occurrence of duplicates

# %%
funding_2020[funding_2020.duplicated()]

# %% [markdown]
# #### Investigating the occurrence of duplicates

# %%
funding_2020[funding_2020["Company"] == "Krimanshi"]

# %% [markdown]
# ##### from the dataframe,rows 129 and 145 are duplicated entries. Hence, row 145 will be dropped.

# %%
funding_2020[funding_2020["Company"] == "Nykaa"]

# %% [markdown]
# ##### Rows 120 and 205 are duplicated entries. Hence, row 205 will be removed

# %%
funding_2020[funding_2020["Company"] == "Byju’s"]

# %% [markdown]
# ##### Rows 326 and 362 are duplicated entries. Hence, row 362 will be dropped

# %%
funding_2020[funding_2020["Company"] == "Yolo"]

# %% [markdown]
# ##### Rows 902 and 964 are duplicated entries. Hence, row 964 will be dropped

# %% [markdown]
# ### Dropping Duplicated Entries
# 
# These rows were duplicated entries and as such must be dropped form the 2020 funding dataset
# 1. Row 145
# 2. Row 205
# 3. Row 362
# 4. Row 964

# %%
# Dropping identified duplicated entries

funding_2020 = funding_2020.drop_duplicates(subset=None, keep="first")

# %%
# Cross-checking to verify dropping of duplicates

funding_2020.duplicated().any()

# %% [markdown]
# ### ADD YEAR COLUMN TO DATASET FOR FURTHER ANALYSIS

# %%
funding_2020["funding_year"] = 2020

# %% [markdown]
# #### Re-checking the basic info of the 2019 funding dataset

# %%
funding_2020.info()

# %% [markdown]
# ### The cleaned 2020 Funding Dataset

# %%
funding_2020.head()

# %% [markdown]
# ## CLEANING THE 2021 FUNDING DATASET

# %% [markdown]
# ### Important notice for corrections
# Theses errors were noticed in the Data Understanding phase
# 
# ##### Label 98, 111 (FanPlay)
# No Location
# 
# Amount 1200000 was recorded under Stage
# 
# Investor(Upstarks) was recorded under Amount
# 
# ##### Label 241, 255 (MasterChow)
# Sector(Food & Beverages) was recorded under Location
# 
# Location (Hauz Khas) was recorded under Sector 
# 
# ##### Label 242, 256 (Fullife Healthcare)
# Amount of 22000000 was recorded under Investor
# 
# Investor (Morgan Stanley, Private Equity Asia) was recorded under Founder
# 
# Stage(Series C) was recorded under Amount
# 
# Sector (Pharmaceuticals) was recorded under Location
# 
# There was no location recorded
# 
# ##### Label 1100
# Sector - Online Media
# 
# ##### Label 1176(Peak)
# Location  -  Manchester
# 
# Sector  - Information Technology

# %% [markdown]
# ### CORRECTING THE IDENTIFIED ERRORS

# %% [markdown]
# #### LABEL 98, 111(FANPLAY)

# %%
funding_2021.loc[(98, 111), "Amount($)"] = "$1200000"
funding_2021.loc[(98, 111), "Stage"] = "Unknown"
funding_2021.loc[(98, 111), "Investor"] = "Upsparks"
funding_2021.loc[(98, 111), "HeadQuarter"] = "Unknown"

# %% [markdown]
# #### LABEL 241, 255(MASTERCHOW)

# %%
funding_2021.loc[(241, 255), "HeadQuarter"] = "Hauz Khas"
funding_2021.loc[(241, 255), "Sector"] = "Food & Beverages"

# %% [markdown]
# #### LABEL 257(MoEVing)

# %%
funding_2021.loc[257, "Amount($)"] = "$5000000"
funding_2021.loc[257, "HeadQuarter"] = "Gurugram"
funding_2021.loc[257, "Sector"] = "Electronic Vehicle"
funding_2021.loc[257, "Stage"] = "Seed"
funding_2021.loc[257, "Investor"] = "Anshuman Maheshwary, Dr Srihari Raju Kalidindi"

# %% [markdown]
# #### LABEL 242, 256(FULLIFE HEALTHCARE)

# %%
funding_2021.loc[(242, 256), "Amount($)"] = "$22000000"
funding_2021.loc[(242, 256), "Investor"] = "Morgan Stanley Private Equity Asia"
funding_2021.loc[(242, 256), "Stage"] = "Series C"
funding_2021.loc[(242, 256), "HeadQuarter"] = "Uknown"
funding_2021.loc[(242, 256), "Sector"] = "Pharmaceuticals"
funding_2021.loc[(242, 256), "Founders"] = "Unknown"       

# %% [markdown]
# #### LABEL 538 (LITTLE LEAP)

# %%
funding_2021.loc[538, "Amount($)"] = "$300000"
funding_2021.loc[538, "Investor"] = "ah! Ventures"
funding_2021.loc[538, "Stage"] = "Undisclosed"

# %% [markdown]
# #### LABEL 545 (ADMITKARD)

# %%
funding_2021.loc[545, "Amount($)"] = "$1000000"
funding_2021.loc[545, "Investor"] = "Unknown"
funding_2021.loc[545, "Stage"] = "Pre-series A"

# %% [markdown]
# #### LABEL 551 (BHyve)

# %%
funding_2021.loc[551, "Amount($)"] = "$300000"
funding_2021.loc[551, "Investor"] = "ITO Angel Network, LetsVenture, 100x.VC"
funding_2021.loc[551, "Stage"] = "Undisclosed"
funding_2021.loc[551, "Sector"] = "HR"

# %% [markdown]
# #### LABEL 674 (MYRE Capital)

# %%
funding_2021.loc[674, "Amount($)"] = "$6000000"
funding_2021.loc[674, "Stage"] = "Undisclosed"

# %% [markdown]
# #### LABEL 677 (Saarthi Pedagogy)

# %%
funding_2021.loc[677, "Amount($)"] = "$1000000"
funding_2021.loc[677, "Investor"] = "JITO Angel Network, LetsVenture"
funding_2021.loc[677, "Stage"] = "Undisclosed"

# %% [markdown]
# #### LABEL 1100(STOCHCAST)

# %%
funding_2021.loc[1100, "Investor"] = "Uknown"
funding_2021.loc[1100, "HeadQuarter"] = "Uknown"
funding_2021.loc[1100, "Sector"] = "Online Media"

# %% [markdown]
# #### LABEL 1148 (Godamwale)

# %%
funding_2021.loc[1148, "Amount($)"] = "1000000"
funding_2021.loc[1148, "Investor"] = "Undisclosed"
funding_2021.loc[1148, "Stage"] = "Seed"

# %% [markdown]
# #### LABEL 1176(PEAK)

# %%
funding_2021.loc[1176, "Sector"] = "Information Technology & Services"
funding_2021.loc[1100, "HeadQuarter"] = "Manchester"

# %% [markdown]
# ### REMOVING COLUMNS THAT ARE IRRELEANT TO OUR ANALYSIS

# %%
# Dropping the Founded column
funding_2021 = funding_2021.drop(columns="Founded", axis=1)

# Dropping the What it does column
funding_2021 = funding_2021.drop(columns="What it does", axis=1)

# Dropping the Founders column
funding_2021 = funding_2021.drop(columns="Founders", axis=1)

# %% [markdown]
# ### RENAMING COLUMNS TO CONFORM WITH THE REST OF DATA

# %%
funding_2021 = funding_2021.rename(columns={"Company/Brand" : "Company", "HeadQuarter" : "Location"})

# %% [markdown]
# ### WORKING ON THE COMPANY COLUMN

# %%
# Change names of Companies to make it consistent with other datasets
funding_2021["Company"] = funding_2021["Company"].replace("Vitra.ai", "Vitra AI")
funding_2021["Company"] = funding_2021["Company"].replace("Superpro.ai", "Superpro AI")
funding_2021["Company"] = funding_2021["Company"].replace("Factors.AI", "Factors AI")
funding_2021["Company"] = funding_2021["Company"].replace("Locale.ai", "Locale AI")
funding_2021["Company"] = funding_2021["Company"].replace("NimbleBox.ai", "NimbleBox AI")
funding_2021["Company"] = funding_2021["Company"].replace("infra.market", "Infra Market")
funding_2021["Company"] = funding_2021["Company"].replace("Infra.Market", "Infra Market")
funding_2021["Company"] = funding_2021["Company"].replace("Karkhana.io", "Karkhana")
funding_2021["Company"] = funding_2021["Company"].replace("Legalwiz.in", "Legalwiz")
funding_2021["Company"] = funding_2021["Company"].replace("Murf.ai", "Murf")
funding_2021["Company"] = funding_2021["Company"].replace("Eka.care", "Eka Care")
funding_2021["Company"] = funding_2021["Company"].replace("Crejo.Fun", "Crejo Fun")
funding_2021["Company"] = funding_2021["Company"].replace("BYJU'S", "Byju's")
funding_2021["Company"] = funding_2021["Company"].replace("BYJU’S", "Byju's")
funding_2021["Company"] = funding_2021["Company"].replace("Wherehouse.io", "Wherehouse")
funding_2021["Company"] = funding_2021["Company"].replace("saarthi.ai", "Saarthi AI")
funding_2021["Company"] = funding_2021["Company"].replace("CoffeeMug.ai", "CoffeeMug AI")
funding_2021["Company"] = funding_2021["Company"].replace("Pathfndr.io", "Pathfndr")
funding_2021["Company"] = funding_2021["Company"].replace("Apna.co", "Apna")
funding_2021["Company"] = funding_2021["Company"].replace("Betterhalf.ai", "Betterhalf AI")
funding_2021["Company"] = funding_2021["Company"].replace("Rezo.ai", "Rezo AI")
funding_2021["Company"] = funding_2021["Company"].replace("Enthu.ai", "Enthu AI")
funding_2021["Company"] = funding_2021["Company"].replace("SuperOps.ai", "SuperOps AI")
funding_2021["Company"] = funding_2021["Company"].replace("NoBroker.com", "NoBroker")
funding_2021["Company"] = funding_2021["Company"].replace("Phool.co", "Phool")
funding_2021["Company"] = funding_2021["Company"].replace("leap.club", "Leap Club")
funding_2021["Company"] = funding_2021["Company"].replace("Crater.Club", "Crater Club")
funding_2021["Company"] = funding_2021["Company"].replace("Toch.ai", "Toch AI")
funding_2021["Company"] = funding_2021["Company"].replace("ApplicateAI", "Applicate AI")
funding_2021["Company"] = funding_2021["Company"].replace("Wiggles.in", "Wiggles")
funding_2021["Company"] = funding_2021["Company"].replace("immunitoAI", "immunito AI")
funding_2021["Company"] = funding_2021["Company"].replace("Sugar.fit", "Sugar Fit")
funding_2021["Company"] = funding_2021["Company"].replace("NeuroPixel.AI", "NeuroPixel AI")

# %% [markdown]
# ### WORKING ON THE LOCATOIN COLUMN

# %%
# Fill NaN values with "Unknown"
funding_2021["Location"] = funding_2021["Location"].fillna("Uknown")

# Split City from State
funding_2021["Location"] = funding_2021["Location"].str.split(",").str[0]

# Change names to fit other datasets
funding_2021["Location"] = funding_2021["Location"].replace("Bangalore", "Bengaluru")
funding_2021["Location"] = funding_2021["Location"].replace("Faridabad, Haryana", "Haryana")
funding_2021["Location"] = funding_2021["Location"].replace("Computer Games", "Uknown")
funding_2021["Location"] = funding_2021["Location"].replace("Faridabad, Haryana", "Haryana")
funding_2021["Location"] = funding_2021["Location"].replace("Faridabad", "Haryana")

# %% [markdown]
# ### WORKING ON THE SECTOR COLUMN

# %% [markdown]
# #### Correcting errors in the names of sector

# %%
 
funding_2021["Sector"] = funding_2021["Sector"].replace("Helathcare", "Healthcare")
funding_2021["Sector"] = funding_2021["Sector"].replace("Information Technology", "IT")
funding_2021["Sector"] = funding_2021["Sector"].replace("Information Technology & Services", "IT")
funding_2021["Sector"] = funding_2021["Sector"].replace("Human Resources", "HR")
funding_2021["Sector"] = funding_2021["Sector"].replace("B2B Ecommerce", "B2B E-commerce")
funding_2021["Sector"] = funding_2021["Sector"].replace("HealthCare", "Healthcare")
funding_2021["Sector"] = funding_2021["Sector"].replace("Health care", "Healthcare")
funding_2021["Sector"] = funding_2021["Sector"].replace("Health Care", "Healthcare")
funding_2021["Sector"] = funding_2021["Sector"].replace("Heathcare", "Healthcare")

# %% [markdown]
# #### Remove Startup from the names of Sector to be consistent with other funding datasets

# %%

funding_2021["Sector"] = funding_2021["Sector"].str.replace("startup", "")
funding_2021["Sector"] = funding_2021["Sector"].str.replace("Startup", "")
funding_2021["Sector"] = funding_2021["Sector"].str.replace("tech", "Tech", regex=True)
funding_2021["Sector"] = funding_2021["Sector"].str.replace("company", "")

# %% [markdown]
# #### Replace '&' with "," to differenciate between sector

# %%
funding_2021["Sector"] = funding_2021["Sector"].str.replace("&", ",")

# %% [markdown]
# ### CLEANING THE INVESTOR COLUMN

# %%
#### Replace NaN values with "Undisclosed"
funding_2021["Investor"] = funding_2021["Investor"].fillna("Undisclosed")

funding_2021["Investor"] = funding_2021["Investor"].replace("http://100x.vc/", "100x.VC")
funding_2021["Investor"] = funding_2021["Investor"].replace("Sequoia", "Sequoia Capital")
funding_2021["Investor"] = funding_2021["Investor"].replace("2000000", "Undisclosed")


# %% [markdown]
# ### CLEANING THE AMOUNT COLUMN

# %% [markdown]
# #### Convert empty spaces to 0

# %%
funding_2021["Amount($)"] = funding_2021["Amount($)"].replace('', 0)

# %% [markdown]
# #### Fill NaN values with 0

# %%
funding_2021["Amount($)"] = funding_2021["Amount($)"].fillna(0)

# %% [markdown]
# #### Remove special signs "$" and ","

# %%
funding_2021["Amount($)"] = funding_2021["Amount($)"].str.replace("$", "")
funding_2021["Amount($)"] = funding_2021["Amount($)"].apply(lambda x: str(x).replace(',',''))

# %% [markdown]
# #### Replace "Undisclosed", "undisclosed" with 0

# %%
funding_2021["Amount($)"] = funding_2021["Amount($)"].replace("Undisclosed", 0)
funding_2021["Amount($)"] = funding_2021["Amount($)"].replace("undisclosed", 0)

# %% [markdown]
# #### Convert Amount column to a float

# %%
funding_2021["Amount($)"] = funding_2021["Amount($)"].astype(float)
funding_2021["Amount($)"].head()

# %% [markdown]
# ### CLEANING THE STAGE COLUMN

# %% [markdown]
# #### Fill NaN values with "Undisclosed"

# %%
funding_2021["Stage"] = funding_2021["Stage"].fillna("Undisclosed")

# %% [markdown]
# #### Correct names of stages to conform with other funding datasets

# %%
funding_2021["Stage"] = funding_2021["Stage"].replace("Unknown", "Undisclosed")

# %% [markdown]
# ### CLEANING DUPLICATES

# %% [markdown]
# #### Checking for Duplicates

# %%
funding_2021.duplicated().any()

# %% [markdown]
# #### viewing the occurrence of duplicates

# %%
funding_2021[funding_2021.duplicated()]

# %% [markdown]
# #### Special note on Duplicates
# 
# During the data understanding phase, the team already investigated and analyzed the duplicated entries.

# %% [markdown]
# #### Removing Duplicates

# %%
funding_2021 = funding_2021.drop_duplicates(subset=None, keep="first")

# %% [markdown]
# #### Cross-checking forduplicates

# %%
funding_2021.duplicated().any()

# %% [markdown]
# ### ADD FUNDING YEAR TO DATASET FOR FURTHER ANALYSIS

# %%
funding_2021["funding_year"] = 2021

# %% [markdown]
# #### Re-checking the basic info of dataset

# %%
funding_2021.info()

# %% [markdown]
# #### THE CLEANED FUNDING 2021 DATASET

# %%
funding_2021.head()

# %% [markdown]
# # MERGE ALL FUNIDNG DATASETS TO FORM ONE DATASET

# %%
indian_startup_funding = pd.concat([funding_2018, funding_2019, funding_2020, funding_2021])
indian_startup_funding = indian_startup_funding.reset_index(drop=True)

# %% [markdown]
# ### FURTHER CLEANING IN THE COMBINED DATASET

# %%
indian_startup_funding["Sector"] = indian_startup_funding["Sector"].replace("Health care", "Healthcare")
indian_startup_funding["Sector"] = indian_startup_funding["Sector"].replace("Health Care", "Healthcare")
indian_startup_funding["Sector"] = indian_startup_funding["Sector"].replace("Ecommerce", "E-commerce")
indian_startup_funding["Company"] = indian_startup_funding["Company"].replace("Oyo", "OYO")
indian_startup_funding["Company"] = indian_startup_funding["Company"].replace("Byju’s", "Byju's")
indian_startup_funding["Company"] = indian_startup_funding["Company"].replace("BYJU’S", "Byju's")
indian_startup_funding["Location"] = indian_startup_funding["Location"].replace("Gurugram", "Gurgaon")
indian_startup_funding["Investor"] = indian_startup_funding["Investor"].replace("Undisclosed", "Unknown")
indian_startup_funding["Stage"] = indian_startup_funding["Stage"].replace("Undisclosed", "Unknown")
indian_startup_funding["Sector"] = indian_startup_funding["Sector"].replace("Undisclosed", "Unknown")
indian_startup_funding["Stage"] = indian_startup_funding["Stage"].str.replace("Debt Financing", "Debt")
indian_startup_funding["Stage"] = indian_startup_funding["Stage"].str.replace("Debt Financing Financing", "Debt")
indian_startup_funding["Stage"] = indian_startup_funding["Stage"].str.replace("Bridge", "Bridge")
indian_startup_funding["Stage"] = indian_startup_funding["Stage"].str.replace("Pre-series A", "Pre-Series A")
indian_startup_funding["Stage"] = indian_startup_funding["Stage"].str.replace("Seed fund", "Seed")

# %% [markdown]
# #### The 2019 Dataset do not have an Investor column. Hence, the column is filled with NaN values. We replace NaN values with "Unknown"

# %%
indian_startup_funding["Investor"] = indian_startup_funding["Investor"].fillna("Unknown")

# %% [markdown]
# ### SAVE COMBINED, CLEANED DATASET TO A NEW CSV FILE

# %%
indian_startup_funding.to_csv("indian_startup_funding.csv", index=False)

# %%
indian_startup_funding.head()

# %% [markdown]
# #### Checking the basic info of the new dataset

# %%
indian_startup_funding.info()

# %% [markdown]
# #### Checking the basic statistics of the new dataset

# %%
indian_startup_funding.describe(include="all").transpose()

# %% [markdown]
# #### Checking duplicated values in the new dataset

# %%
indian_startup_funding.duplicated().any()

# %% [markdown]
# # ANALYSIS

# %% [markdown]
# ### Load merged dataset

# %%
indian_startup_funding = pd.read_csv("indian_startup_funding.csv")
indian_startup_funding.head()

# %% [markdown]
# ## THE TOTAL NUMBER OF STARTUPS FUNDED AND TOTAL AMOUNT RECEIVED BY START-UPS AS FUNDING

# %%

print("Total number of startups funded for the period is " ,len(indian_startup_funding["Company"].unique()))

# %%
print("Total funding for the period is US$" ,indian_startup_funding["Amount($)"].sum())

# %% [markdown]
# ## Q1.  What Industry/Sector received the most and least funding from investors?
# 
# We check the ten(10) industries that received the most funding from investors. Also we check additonal ten(10) that received the least funding from investors.

# %% [markdown]
# ### Top ten(10) industries with the most funding

# %%
most_funded_industry = indian_startup_funding.groupby("Sector")["Amount($)"].sum()
most_funded_industry = most_funded_industry.sort_values(ascending=False).reset_index().head(10)
most_funded_industry['Amount($)']=most_funded_industry['Amount($)'].apply(lambda x: math.ceil(x))
most_funded_industry

# %%
ten_top_industries = indian_startup_funding.groupby("Sector")["Amount($)"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(15, 10))
plt.barh(ten_top_industries.index, ten_top_industries.values, color="violet")
plt.title("TOP TEN(10) SECTORS WITH HIGHEST FUNDING", fontsize=25)
plt.xlabel("Amount($'Billion)", fontsize=20)
plt.ylabel("Sector", fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.gca().invert_yaxis()
plt.show()



# %% [markdown]
# ### Ten(10) sectors with the least funding from investors

# %%
least_funded_industry = pd.DataFrame(indian_startup_funding.groupby("Sector")["Amount($)"].sum())
least_funded_industry = least_funded_industry.sort_values(by="Amount($)", ascending=False).tail(156)
least_funded_industry['Amount($)'] = least_funded_industry['Amount($)'].apply(lambda x: math.ceil(x))

# %%
# Remove 0 from Amount column. This is because NaN and undisclosed amounts were replaced with 0

least_Funded_industry = least_funded_industry[(least_funded_industry["Amount($)"] != 0)]
least_Funded_industry

# %% [markdown]
# ## Q2.  What are the top five (5) cities with the most start-ups?
# 
# We outline the top five (5) cities that have the highest start-up establishments

# %%
# Remove Uknown from Location columns
df = indian_startup_funding[indian_startup_funding["Location"]!="Unknown"]

# Create Dataframe to show five(5) cities with most startups
top_five_cities = pd.DataFrame(df["Location"].value_counts().head())
top_five_cities

# %%
top_5_cities = df["Location"].value_counts().head() 

plt.figure(figsize=(10, 5))
plt.pie(top_5_cities, labels=df["Location"].head(), data=df["Location"].value_counts())
plt.title("TOP FIVE(5) CITIES WITH MOST START-UPS", fontsize=20)
plt.show()

# %% [markdown]
# ## Q3. What are the top ten(10) startups with the most funding?
#  

# %% [markdown]
# We look at the ten(10) startups with the most funding

# %%
top_startups = indian_startup_funding.groupby("Company")["Amount($)"].sum()
top_startups = top_startups.sort_values(ascending=False).reset_index()
top_startups["Amount($)"] = top_startups["Amount($)"].apply(lambda x: math.ceil(x))
top_startups.head(10)

# %%
ten_top_startups = indian_startup_funding.groupby("Company")["Amount($)"].sum()
ten_top_startups = ten_top_startups.sort_values(ascending=False).head(10)

plt.figure(figsize=(15, 10))
plt.barh(ten_top_startups.index, ten_top_startups.values)
plt.title("TOP TEN START-UPS WITH HIGHEST FUNDING", fontsize=25)
plt.xlabel("Amount($'Billion)", fontsize=20)
plt.ylabel("Sector", fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.gca().invert_yaxis()
plt.show()


# %% [markdown]
# ## Q4. What are the top ten(10) investors by number of investments?

# %% [markdown]
# We look at the top ten(10) investors who made the highest number of investments.

# %%
# Remove Unknown from Investor column for analysis
investors = indian_startup_funding[indian_startup_funding["Investor"]!="Unknown"]

top_10_investors = pd.DataFrame(investors["Investor"].value_counts().head(10))
top_10_investors

# %%
top_10_investors = investors["Investor"].value_counts().head(10)

plt.figure(figsize=(15, 10))
sns.barplot(top_10_investors.values, top_10_investors.index)
plt.title("TOP TEN(10) INVESTORS BY NUMBER OF FUNDS", fontsize=25)
plt.xlabel("Number of Funds", fontsize=20)
plt.ylabel("Investors", fontsize=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

# %% [markdown]
# ## 5. What is the trend of funding in the Indian start-up ecosystem in the referenced year?
# 
# We seek to discover the trend of funding to know if funding is appreciating, reducing or stable.

# %%
funding_trend = indian_startup_funding.groupby("funding_year")["Amount($)"].sum()
funding_trend = funding_trend.reset_index()
funding_trend["Amount($)"] = funding_trend["Amount($)"].apply(lambda x: math.ceil(x))
funding_trend

# %%
trend = indian_startup_funding.groupby("funding_year")["Amount($)"].sum()

plt.figure(figsize=(15, 7))

plt.plot(trend.index, trend.values, marker="o")
plt.title("YEARLY FUNDING TREND", fontsize=25)
plt.xlabel("Funding Year", fontsize=15)
plt.ylabel("Amount($'Billion)", fontsize=15)
plt.xticks(trend.index, fontsize=15, rotation=45)
plt.yticks(fontsize=15)
plt.show()

# %% [markdown]
# #### Calculating the percentage change in funding respectively with the funding years

# %%
# The total yearly funds was from our earlier calculations in the funding trend.
funding_2018 = 6429010902
funding_2019 = 3335433200
funding_2020 = 90930476656
funding_2021 = 179407526000

print(f"Percentage Change in 2019 was {(((funding_2019 - funding_2018) / funding_2019) * 100):.2f}%")
print(f"Percentage Change in 2020 was {(((funding_2020 - funding_2019) / funding_2020) * 100):.2f}%")
print(f"Percentage Change in 2021 was {(((funding_2021 - funding_2020) / funding_2021) * 100):.2f}%")

# %% [markdown]
# ## Q6. Which stage of funding did startups receive the most funds?
# 
# We analyze the stage of investment where investors released the most funds to start-ups.

# %%
# Remove unknown from stage column for analysis
stage = indian_startup_funding[indian_startup_funding["Stage"] != "Unknown"]

funded_stage = indian_startup_funding.groupby(stage["Stage"])["Amount($)"].sum()
funded_stage = funded_stage.sort_values(ascending=False).reset_index().head(10)
funded_stage["Amount($)"] = funded_stage["Amount($)"].apply(lambda x: math.ceil(x))
funded_stage

# %%
plt.figure(figsize=(15, 10))

fundedstage = indian_startup_funding.groupby(stage["Stage"])["Amount($)"].sum().sort_values(ascending=False).head(10)

sns.barplot(fundedstage.index, fundedstage.values)
plt.title("FUNDING STAGES WITH MOST FUNDS", fontsize=20)
plt.xlabel("Funding Stage", fontsize=20)
plt.ylabel("Amount($'Billion)", fontsize=20)
plt.xticks(fontsize=20, rotation=80)
plt.yticks(fontsize=20)
plt.show()

# %% [markdown]
# ## Q7. Which Investors invested the biggest funds in identified Sectors
# 
# We seek to find out the leading investors who made huge investments in sectors. It is worthy to note that the Investor column is highly likely to contain multiple investors

# %%
# Remove "Unknown" from the Investor column

invest = indian_startup_funding[indian_startup_funding["Investor"] != "Unknown"]

# %%
investors = indian_startup_funding.groupby([(invest["Investor"]), "Sector"])["Amount($)"].sum().apply(lambda x: math.ceil(x))
inv = investors.sort_values(ascending=False).reset_index()
inv.head()

# %% [markdown]
# ## Q8. Which Cities received the highest funding
# 
# Here, we seek to know the cities that received the highest funding from investors.

# %%
# Remove unknown values from the Location column

city = indian_startup_funding[indian_startup_funding["Location"] != "Unknown"]

# %%
city_funding = indian_startup_funding.groupby(city["Location"])["Amount($)"].sum()
city_funding = city_funding.sort_values(ascending=False).reset_index()
city_funding["Amount($)"] = city_funding["Amount($)"].apply(lambda x: math.ceil(x))

# %%
# Remove California from values in Location column since we are only concerned about cities in India

city_Funding = city_funding[city_funding["Location"] != "California"]
city_Funding.head(10)

# %%
plt.figure(figsize=(15, 10))
sns.barplot(x="Location", y="Amount($)", data=city_Funding.head(10))
plt.title("CITIES WITH HIGHEST FUNDS", fontsize=20)
plt.xlabel("Cities(India)", fontsize=20)
plt.ylabel("Amount($'Billion)", fontsize=20)
plt.xticks(fontsize=15, rotation=80)
plt.yticks(fontsize=15)
plt.show()

# %% [markdown]
# ### Q10. Average amount a startup is likely to receive as funding
# 
# We want to know the average amount our startup is likely to receive as total funding throughout the entire stages of funding

# %%
number_of_startups = indian_startup_funding["Company"].count()
total_funding = indian_startup_funding["Amount($)"].sum()

# %%
print(f"Average Amount a startup is likely to receive as funding is US${(total_funding / number_of_startups):.2f}")

# %% [markdown]
# ## Q11. Average amount a startup is likely to receive as Seed Fund
# 
# We try to acertain the amount our startup is likely to receive at the beginning stages as a seed fund.

# %%
seed_amount = (indian_startup_funding[indian_startup_funding.Stage == "Seed"])["Amount($)"].sum()
seed_startups = len((indian_startup_funding[indian_startup_funding.Stage == "Seed"]))
average_seed_amount = seed_amount / seed_startups

# %%
print(f"Average Amount a startup is likely to receive as Seed Fund is US${average_seed_amount:.2f}")

# %% [markdown]
# # INSIGHTS

# %% [markdown]
# ### The following are the insights that we gained from our analysis

# %% [markdown]
# There are 2200 unique startups funded for the period and total funding received by startups was 
# US$ 280,102,446,757.83
# 
# 1. The top sectors that received the most funding were;
# - FinTech
# - Retail
# - EdTech
# 
# 2. The top cities were most startups were been established were:
# - Bengaluru(919)
# - Mumbai(468)
# - Gurgaon(318)
# - New Delhi(318)
# 
# 3. These startups received the most funding from investors:
# - Alteria Capital
# - Reliance
# - Byju's
# 
# 4. These were the top investors who made the highest number of investments
# - Inflection Point Ventures
# - Venture Catalysts
# - Mumbai Angel Network
# 
# 5. From our analysis we found out that funding trend was generally positive.
# - In 2019, funding drastically reduced at a rate of 92.74%
# - In 2020, there was an appreciation of funding. Investors increased funding at rate of 96.33%
# - In 2021, the funding momentum rose again by 49.31%
# 
# 6. The commonst investment stage that investors made the highest number of funds available were:
# - Seed round
# - Series A
# - Pre-series A
# 
# 7. These funding stages are the one that investors made the most funds available:
# - Debt Financing
# - Series C
# - Series B
# - Series D
# 
# 8. These investors were the biggest investors who invested most funds in a particular sector:
# - Silver Lake, Mubadala Investment Company
# - Salesforce Ventures, Dragoneer Investment Company
# - Facebook, Googel, Silver Lake
# - Sequoia Capital
# 
# 9. These are the cities that received the highest amount in funding from investors:
# - Mumbai
# - Bengaluru
# - Gurgaon
# - New Delhi

# %% [markdown]
# # RECOMMENDATIONS

# %% [markdown]
# The Indian start-up ecosystem is experiencing an increasing momnetum. The timing for penetration into the ecosystem is right. 
# 
# From our analysis, the trend of funding has been increasing a steady rate. With a total number of startups for the recorded period being 2200, the average amount a startup is likely to receive as total fund is US$ 98,212,639.12. <br />This means that competition for funding is not very intense. Investors are ready to invest in promising startups.
# 
# We therefore recommend the following;
# 
# - The company should consider establlishing in Bengaluru, Mumbai, New Delhi and Gurgaon. These cities have the most startups. A startup in these cities is also likely to receive significant amount of funding.
# 
# 
# - The company is right to seek funding in the early stages. Most investors favored investing during the Seed and Series A rounds. The average amount our company is likely to recieve as seed fund is 
# US$ 1,509,049.45
# 
# 
# - The company should consider seeking funding from Sequoia Capital, Inflection Point Ventures, Venture Catalysts, Silver Lake, Mumbai Angel Network and Venture Catalysts. These investors invested in a couple of startups and raised higher amount of funds.
# 
# 
# - The company should consider establishing a startup in Fintech, Retail, E-commerce and EdTech as these sectors are most favored by investors with higher number of investments and huge inflow of funds.

# %%



