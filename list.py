import pandas as pd
import numpy as np

#dictionary of lists
dict={'first score':[100,90,np.nan,95],
      'second score':[30,45,56,np.nan],
      'third score':[np.nan,40,80,98]}

#creating a dataframe from list
df=pd.DataFrame(dict)

#using replace() function
df.replace({100:35,np.nan:1})
