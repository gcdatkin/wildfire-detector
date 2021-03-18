# wildfire-detector
A wildfire and wildfire hotspot detection system using TensorFlow and CatBoost.  
  
***
  
The program first uses image classification (Keras CNN) to identify the presence of a wildfire in a given satellite image.  
  
If no fire is detected, the application will then query the National Oceanic and Atmospheric Administration for weather data from the surrounding area and time given.  
  
It will use this data to make a prediction (using CatBoost) about whether the given location is potential wildfire hotspot. Hotspots are defined as locations that have had recent wildfires.
  
***
  
To use the program, you will need the following dependencies installed:
- NumPy
- pandas
- PIL
- scikit-learn
- tensorflow
- CatBoost
