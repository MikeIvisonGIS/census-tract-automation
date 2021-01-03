# census-tract-automation

### Census Tract Automation README

By: Michael Ivison

**Purpose of program:** Python script that automates population of temperature normals for census tracts in a table. The script automates through each unique ID in the census tract layer, extracts the average temperature normal by overlaying a raster, adds a field in the census tract table representing the month, and populates the table.
Note: Successful run of script will require the proper workspace path on the user’s computer.

**Input parameters:**

1. Census Tract
   - Created as a variable _census_tract_
2. Temperature data
   - Created as a list variable _temp_norm_

**Intermediate parameters:**

1. An empty list for temporary temperature data
   - Created as a list variable _temp_values_
2. A variable for MEAN temperature data that is created during the Extract by Mask tool
   - Created as a varaible _temp_mean_
3. A variable to keep track of what month is being iterated through
   - Created as a variable _count_

**Output parameters:**

1. An empty field that is created in the census tract layer used the Add Field tool
   - Created as a variable _avgTemp_
   - Assigned as type "FLOAT" using variable _avgTempType_
