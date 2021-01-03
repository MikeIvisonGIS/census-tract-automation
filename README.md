# census-tract-automation

Census Tract Automation README

By: Michael Ivison

Purpose of program: Python script that automates population of temperature normals for census tracts in a table. The script automates through each unique ID in the census tract layer, extracts the average temperature normal by overlaying a raster, adds a field in the census tract table representing the month, and populates the table.
Note: Successful run of script will require the proper workspace path on the user’s computer.

Input parameters:

1. Census Tract
 a. Created as variable census_tract

2. Temperature data
 a. Created as a list variable temp_norm
