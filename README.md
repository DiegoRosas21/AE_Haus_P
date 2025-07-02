# Hausdorff Distance for Areas of Endemism (Shapefiles)

This project contains Python scripts to calculate the Hausdorff distance matrix between a set of polygon shapefile files (Areas of Endemism). The Hausdorff distance measures how far apart two geometries are from each other.

The script processes all shapefiles in a directory, calculates pairwise distances, and saves the results to a CSV file.

## Features

- Automatic loading of all `.shp` files from a directory.
- Geometry unification by layer for efficient calculation.
- Hausdorff distance matrix calculation.
- Export of results matrix to a CSV file.
- **Alternative version (`main1.py`)** with progress bars for better user experience during long processes.

## Available Scripts

- **`main.py`**: The base and functional version of the script.
- **`main1.py`**: A version that uses the `tqdm` library to display progress bars during data loading, processing, and result saving. This script is recommended for large datasets.

## Data

- **`data/`**: This folder contains the original data used to obtain the results for the article (provided as a .zip file that needs to be extracted).
- **`data_ex/`**: This folder contains a small dataset for demonstration purposes.

## Requirements

- Python 3.8 or higher
- Libraries listed in `requirements.txt`.

## Usage

1.  **Prepare your data**: Place your shapefile files (`.shp` and their associated files `.dbf`, `.shx`, etc.) in the `data_ex` folder, or create a new folder and update the `directory` variable in the script.

2.  **Configure the script (Optional)**:
    If you want to use a different data folder or change the output file name, you can modify the following lines at the beginning of the script (`main.py` or `main1.py`):
    ```python
    # Path to the directory where the shapefiles are located
    directory = 'data_ex' # Change to 'data' or your custom folder

    # Path and name of the CSV file where results will be saved.
    output_file = 'dist_ex.csv' # You can change the output file name
    ```

3.  **Run the script**

4.  **Review the results**: Once the process is finished, you will find the CSV file (by default, `dist_ex.csv`) in the main directory.

## Example Output

The resulting CSV file (data_ex) will look like this:

```
,Austroriparianprv,Chihuahuanprv,Oregonianprv
Austroriparianprv,0,27.016049229381334,46.66163362381724
Chihuahuanprv,27.016049229381334,0,30.50748108358096
Oregonianprv,46.66163362381724,30.50748108358096,0
```
