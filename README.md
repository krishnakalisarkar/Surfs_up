# Surfs_up

**Analysis using SQL lite, SQL Alchemy and FLASK**

![image](https://d14fqx6aetz9ka.cloudfront.net/wp-content/uploads/2018/11/28130614/06-Owen-Wright-at-Pipeline-Hawaii-26th-NOV-2018-by-Pedro-Gomes-PED_5464_J.jpg)

## Overview of the Analysis:

The purpose of this analysis is to get an insight into the weather pattern in the Hawaiian Island of Oahu. This insight would give the stakeholders an idea of how profitable a Surf and Ice cream shop would succeed in that Island.  
* By sending queries using SQL Alchemy into the Hawaii SQLite database, it came into light that the database has two classes Measurements and Station. The Inspector function listed the columns under Measurement and Station as:  

|Measurement    | Station       | 
| ------------- |:-------------:|
| id.           | id.           |
| station       | station       |
| date          | name.         |
| prcp          | latitude      |
| tobs.         | longitude.    |
|               | elevation.    |

*List of columns under Measurement and Station.*

* Queries were sent to obtain the temperatures for the month of June and December.  
* Based on the data returned a histogram was created for visual representation of the data.  
* Some additional queries were also sent to look at the precipitation trend in the months of June and December.  
* A bar chart provided a good representation of the precipitation data.

## Results:

The table below shows temperature statistics from June and December.
### Temperature Summary Table:

|Statistics     | June          | December    |
| ------------- |:-------------:|:------------|
| count         | 1700          |1517.        |
| mean          | 74.9          |71.0.        |
| Minimum       | 64.0          |56.0	    |
| Maximum.      | 85.0          |83.0.        |

*Temperature statistics in June and December.*

* Looking at the table it is evident that the minimum temp in June is 64 F, which is higher than the minimum temp recorded in December 56 F.  
* The maximum temperature in June is 85F compared to December 83F.  
* The mean temperature in June is around 75F and 71F in December.

![june_dec_tobs]()

### Precipitation Summary Table:

|Statistics     |     June      | December    |
| ------------- |:-------------:|:------------|
| count         | 1574          |1405         |       
| mean          | 0.14          |0.21         |
| Minimum       | 0.0           |0.0          |
| Maximum.      | 4.43          |6.42         |

*Precipitation statistics in June and December.*

* The above table clearly shows there are more instances of rainfall recored in June (1574) compared to December (1405).  
* The maximum amount of rainfall recorded in June 4.43 and 6.42 in December.   
* The average rainfall recorded in June is 0.14 and 0.21 in December.

![june_dec_prcp]()

## Summary:

 The data generated from this analysis gives an insight to the Surf and Ice cream business stakeholders on the amount of precipitation and temperature patterns for the month of June and December. June, July and December are good choice for vacation in Hawaii as it coincides with summer vacation and winter vacation in USA and also around the world.   
 * The temperature shows that the maximum temp in June is around 85 F and the mean temperature is around 75F, which is ideal for both surfing in the big waves and also cooling off with an ice-cream.   
 * The mean precipitation is around 0.14, and maximum precipitation is 4.43, which is mot too much to prevent visitors from visiting the beaches and enjoying the waters and ice cream.  
 * Summer months are the best time to go surfing on the southern shores of the Hawaiian Islands.The sea is lot calmer and the waves are smaller, hence it is ideal for beginners to try surfing.  
 * The maximum temperature in December shows around 83F but winter months are the most wet months with maximum rainfall around 6.42 inches.   
 * For advanced surfers, December through and February sees the biggest and most powerful waves on the northern shores.  
 * This high waves in December calls for most of the surfing competitions happening around this time.  
        We can conclude this analysis by saying that the maximum temperature being around 83F and December being the surfing competition season, the stakeholders will have a good visitor crowd throughout the year specially around June and December as these are the holiday seasons and it coincides with the surfing competitions too. 
 
