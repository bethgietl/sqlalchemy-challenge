# sqlalchemy-challenge

The sqlalchemy challenge started with importing sqlalchemy. Next I created the base sqlite database bath, the connection, reflected the database into ORM classes and then saved the references. 

I viewed and inspected the calsses that automap found to determine the data types I was working with. 

The most interesting parts of the assignment were: 
    1. using the dt.date and dt.timedelta functions I craeted a 'year_ago' varialbe that I was able to filter and retrieve the precipitation resuts for the last 12 months. I created a dataframe with the filtered date results and plotted the data using matplotlib. 
    
    2. next, I found the most active station. I created the statement and grouped by the station and then ordered the results in descending order. The results showed that Station USC00519281 had 2772 rows. I created a dataframe filtering by the most active weather station during a 1 year timeframe. I used the dataframe to create a histogram shoing the tempatures and frequency in the dataframe. 
    
    3. the last part of the assginment, I designed a FLask API based on the queries I developed in python. The most impressive section was when I returned a JSON list of tempature data (min, max, avg) based on a 'start_date' and 'end_date' range that a that is established by a user. I did this with the def function and setting the 'start' and 'end' to 'None', then I created the statement calculating the min, max and average tempatures and created the date range using the filter function stating the date range by calling the date in the statement is > the start date that the user inputs and < the end date. I created a list to return with the start, end dates plus the tempature stats (min, max, average tempatures. 

