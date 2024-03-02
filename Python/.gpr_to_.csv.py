import rasterio
import numpy as np
import pandas as pd

# Open the .gpr file
with rasterio.open('input.gpr') as src:
    # Read the data
    data = src.read(1)

    # Convert the data to a DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to Excel
    df.to_excel('output.xlsx', index=False)


# pip install rasterio
