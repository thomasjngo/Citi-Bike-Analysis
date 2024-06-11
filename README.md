# Citi Bike Analysis (Randomized-Samples)

## Objective ##
To analyze the Citi Bike usage data in New York City from 2015 and 2020 to observe any noticable trends in the data.

**Data Preprocessing:**
* Data is extracted from 27 CSV files downloaded from [Citi Bike](https://citibikenyc.com/system-data)'s System Database for [2020](https://s3.amazonaws.com/tripdata/2020-citibike-tripdata.zip). (csv's should be placed in the resources folder)
* Data was randomly sampled to meet the 15,000,000 row maximum allowed by Tableau Public software.
* Trip time was provided in seconds and then converted into minutes to make the data more suitable for creation of visualizations.
* Distance was calculated using the longitude and latitude data and then calling the function `DISTANCE([Origin],[Destination],'km')` to calculate the distance of each bike ride.

![CSV Data](Resources/csvdata.PNG)

## Main Dashboard ##
All the longitude and latitude data was used to call the function `makepoint([Start Station Latitude],[Start Station Longitude])` and `makepoint([End Station Latitude],[End Station Longitude])` so that each bike ride could be traced using `Makeline([Origin],[Destination])`. Data was then grouped by the start station name so that all the routes radiated out of a singular point like a flower. This helps give an idea of the final destination points.

![Main Dashboard](Resources/routestaken.PNG)

## Bike Usage Trends by Month ##
The data was arranged by month to show the general trend of usage during the year. There is a large spike during the summer which suggests that people are more likely to rent bikes when the weather is hot possibly to avoid being out in the heat as long as possible. Surprisingly there is no observable impact of stay-at-home orders due to the COVID-19 pandemic during this time.

![Bike Usage](Resources/bikeusage.PNG)

## User Breakdown ##
Subscribers used the service over three times more than normal customers. However, the data suggests that subscribers used the service more frequently but for shorter trips compared to normal users.

![User Breakdown](Resources/usertype.PNG)

## Start/End Stations ##
The start and end stations were grouped by their count in the dataset. The most popular start stations tend to be near areas where subway stations are too far away to reach by walking. End stations show a similar trend as they are often in the outskirts of the city away form any nearby subway stations. 

![Start Stations](Resources/startstations.PNG)

The stations were then color coded and sized according be their rank in the dataset. Filters were added to show include/exclude each month. In the summer, there is a heavier concentration of start stations near the coasts suggesting people tend to frequent the piers more often (possibly due to cooler climate). End station data also shows similar trends as the start station. There is additional evidence that bikes are being rented to cross the major bridges in the city as there is a heavier concentration of end points outside the city.

![Bubble Plot](Resources/bubbleplot.PNG)

## Average Bike Trip Distance ##
The average distance traveled per bike trip is concentrated around 2km.

![Line Graph](Resources/linegraph.PNG)

# Bikes Likely to be Repaired ##
The dataset was then sorted by total distance traveled for the year and then filtered to show the bikes that have been used for 3km or more. These are most likely to need repair in the future. Most bikes traveled 1.5km or less.

![Bike Repair](Resources/bikerepair.PNG)
