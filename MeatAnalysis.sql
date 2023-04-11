-- define the table
CREATE TABLE MeatData
(id serial,
location varchar,
indicator varchar,
subject varchar,
measure varchar,
frequency varchar,
time varchar,
value numeric
);

-- describe the table
\d meatdata

-- load in the csv of the DATA
COPY meatdata(id, location, indicator, subject, measure, frequency, time, value) -- copy into the meatdata table
FROM '/Users/kollintrujillo/Downloads/meat_consumption.csv' -- put your own directory to the file here.
DELIMITER ','
CSV HEADER;

-- will read COUNT 12160 if successful.

-- List the meat types we have in the dataset
SELECT DISTINCT subject
FROM meatdata;


-- Get value with Group by meat TYPE. 
SELECT SUM(value), 
		   subject
FROM meatdata
GROUP BY subject;

-- Get meat consumption per location, which is country
SELECT SUM(value), 
		   subject
FROM meatdata
GROUP BY subject,
		 location;

-- Total meat consumption in kg per capita per country
SELECT location,
	   subject,
	   measure,
	   SUM(value)
FROM meatdata
WHERE measure = 'KG_CAP'
GROUP BY subject,
		 location,
		 measure
ORDER BY location;