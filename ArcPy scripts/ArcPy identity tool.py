# Identity.py
# Description: Simple example showing use of Identity tool
 
# Import system modules
import arcpy
from arcpy import env 

# Set the workspace
env.workspace = "C:\Users\ASUS\Desktop\SPATIAL ANALYSE\lab4"

# Set local parameters
inFeatures = "roads_2007_layer"
idFeatures = "pop"
outFeatures = "identity_deneme"

# Process: Use the Identity function
arcpy.Identity_analysis (inFeatures, idFeatures, outFeatures)
