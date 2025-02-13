# Citi Bike Analysis (Randomized Samples)

[Tableau Link](https://public.tableau.com/app/profile/thomas.ngo3259/viz/AnAnalysisofNYCCitiBikeUsage2015vs_2020/Story1)

## Objective ##
To analyze the Citi Bike usage data in New York City from 2015 and 2020 to note any noticeable trends in the data.

## Data Preprocessing ##
* Data is extracted from CSV files downloaded from [Citi Bike](https://citibikenyc.com/system-data)'s System Database for [2015](https://s3.amazonaws.com/tripdata/2015-citibike-tripdata.zip) and [2020](https://s3.amazonaws.com/tripdata/2020-citibike-tripdata.zip).
* Place csv files in the `Resources` folder and then run `random_select.py` for processing.
* Data was randomly sampled to meet the file size requirements of Tableau Public software (currently set to 1,000,000 data points).
* Trip time was provided in seconds and then converted into minutes to make the data more suitable for creation of visualizations.
* Distance was calculated using the longitude and latitude data and then calling the function `DISTANCE` to calculate the distance of each bike ride in kilometers.

![CSV Data](Resources/csvdata.PNG)

## Main Dashboard ##
All the longitude and latitude data was used to call the function `makepoint` so that each bike ride could be traced using `makeline`. Data was then grouped by the start station name so that all the routes radiated out of a singular point like a flower. This helps give an idea of the route and final destination points.

![Main Dashboard](Resources/routestaken.PNG)

## Bike Usage Trends by Month ##
The data was arranged by month to show the general trend of usage during the year. Bike usage is up 2x overall but non-subscriber usage is up almost 5x during peak months from 2015 to 2020. This shows that there is a group of customers that may only rent a bike out of necessity instead of regular use.

![Bike Usage](Resources/bikeusage.PNG)

## User Breakdown ##
After filtering null values and the default year at sign up (1/1/1969), the age group that mosts uses the bikes are gen X and millenials for both subscribers and non-subscribers.

![User Breakdown](Resources/usertype.PNG)

## Start/End Stations ##
The start and end stations were grouped by their count in the dataset. The most popular start stations tend to be near areas where subway stations are too far away to reach by walking. End stations show a similar trend as they are often in the edges of the city. 

![Start Stations](Resources/startstations.PNG)

The stations were then color coded and sized according be their rank in the dataset. Filters were added to show include/exclude each month. In the summer, there is a heavier concentration of start stations near the coasts suggesting people tend to frequent the piers more often (possibly due to cooler climate). End station data also shows similar trends as the start station. There is additional evidence that bikes are being rented to cross the major bridges in the city as there is a heavier concentration of end points outside the city.

![Bubble Plot](Resources/bubbleplot.PNG)

## Average Bike Trip Distance ##
The average distance traveled per bike trip is concentrated around 2km.

![Line Graph](Resources/linegraph.PNG)

# Bikes Likely to be Repaired ##
The dataset was filtered to show the bikes that have been used more. These are most likely to need repair in the future. 

![Bike Repair](Resources/bikerepair.PNG)

## Conclusion ##
People are most likely to rent bikes during the summer months possibly due to the increasing heat and the desire to minimize travel time. The rentals are up overall in 2020 compared to 2015, but more can be done to capitalize on converting the non-subscribers into paying for the service long term. Additionally, there seems to be little impact on rentals from the COVID-19 pandemic suggesting that business will hold strong in the future.
