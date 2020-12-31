#-------------------------------------------------------------------------------
# Name:        Census_Tract_Automation
# Purpose:     Python script that automates population of temperature normals
#              for census tracts in a table
#
# Author:      Mike Ivison
#
# Created:     29/12/2020
# Copyright:   (c) Mike Ivison 2020
# Licence:     <Home user>
#-------------------------------------------------------------------------------

#Import arcpy, define workspace, check out Spatial Analysis extension
import arcpy
arcpy.env.workspace = r'E:/Documents/GIS_Portfolio/Python/AutomationProject'
arcpy.CheckOutExtension('Spatial')

#Define variables
census_tract = r'E:/Documents/GIS_Portfolio/Python/AutomationProject/tl_2018_30_tract/tl_2018_30_tract.shp'
temp_norm = [
r'E:\Documents\GIS_Portfolio\Python\AutomationProject\Normals\Normals.gdb\TMEAN000001_normal' ,
r'E:\Documents\GIS_Portfolio\Python\AutomationProject\Normals\Normals.gdb\TMEAN000002_normal',
r'E:\Documents\GIS_Portfolio\Python\AutomationProject\Normals\Normals.gdb\TMEAN000003_normal',
r'E:\Documents\GIS_Portfolio\Python\AutomationProject\Normals\Normals.gdb\TMEAN000004_normal',
r'E:\Documents\GIS_Portfolio\Python\AutomationProject\Normals\Normals.gdb\TMEAN000005_normal',
r'E:\Documents\GIS_Portfolio\Python\AutomationProject\Normals\Normals.gdb\TMEAN000006_normal',
r'E:\Documents\GIS_Portfolio\Python\AutomationProject\Normals\Normals.gdb\TMEAN000007_normal',
r'E:\Documents\GIS_Portfolio\Python\AutomationProject\Normals\Normals.gdb\TMEAN000008_normal',
r'E:\Documents\GIS_Portfolio\Python\AutomationProject\Normals\Normals.gdb\TMEAN000009_normal',
r'E:\Documents\GIS_Portfolio\Python\AutomationProject\Normals\Normals.gdb\TMEAN000010_normal',
r'E:\Documents\GIS_Portfolio\Python\AutomationProject\Normals\Normals.gdb\TMEAN000011_normal',
r'E:\Documents\GIS_Portfolio\Python\AutomationProject\Normals\Normals.gdb\TMEAN000012_normal',
]
avgTemp = 'AvgTemp'
avgTempType = 'FLOAT'
count = 0

#From census_tract shapefile (tl_2018_30_tract), create a layer named census_tract_layer
arcpy.MakeFeatureLayer_management(census_tract, "census_tract_layer")

#For every census tract, create a mask of temperature values --> use Raster Properties to calculate the mean temperature value for that census tract --> append mean temperature value to temp_values list.
for month in temp_norm:
    temp_values = []
    with arcpy.da.SearchCursor(census_tract, ['FID']) as cursor:
        for fid in cursor:
            arcpy.SelectLayerByAttribute_management("census_tract_layer", "NEW_SELECTION", """ "FID" = {}""".format(fid[0]))
            outExtractByMask = arcpy.sa.ExtractByMask(month, "census_tract_layer")
            temp_mean = arcpy.GetRasterProperties_management(outExtractByMask, 'MEAN')
            temp_values.append(float(temp_mean.getOutput(0)))
        count = count + 1 #this creates a unique value for each field that is added to the census_tract table

    #Delete any stored fid or cursor data for better memory performance. No longer needed.
    del fid
    del cursor

    #Add a field to census_tract table named avgT_x of type FLOAT where x represents the count variable that keeps track of the month.
    arcpy.SelectLayerByAttribute_management('census_tract_layer', 'CLEAR_SELECTION')
    arcpy.AddField_management(census_tract, "avgTemp_{0}".format(count), avgTempType)

    #For every census tract in census_tract --> populate avgT field with temp_values list created earlier.
    cursor = arcpy.UpdateCursor(census_tract)

    x = 0
    for row in cursor:
        row.setValue("avgTemp_{0}".format(count), temp_values[x])
        cursor.updateRow(row)
        x += 1

    #Delete any stored row or cursor data for better memory performance. No longer needed.
    del cursor
    del row