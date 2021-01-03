# census-tract-automation

Census Tract Automation README

By: Michael Ivison

Purpose of program: Python script that automates population of temperature normals for census tracts in a table. The script automates through each unique ID in the census tract layer, extracts the average temperature normal by overlaying a raster, adds a field in the census tract table representing the month, and populates the table.
Note: Successful run of script will require the proper workspace path on the user’s computer.

Input parameters:
1.	Census Tract
 a.	Created as variable census_tract
2.	Temperature data
 a.	Created as a list variable temp_norm

Intermediate parameters:

1.	An empty list for temporary temperature data
 a.	Created as a list variable temp_values
2.	A variable for MEAN temperature data that is created during the Extract by Mask tool
 a.	Created as a variable temp_mean
3.	A variable to keep track of what month is being iterated through
 a.	Created as a variable count
 
Output parameters:
1.	An empty field that is created in the census tract layer using the Add Field tool
 a.	Created as a variable avgTemp
 b.	Assigned as type “FLOAT” using variable avgTempType
