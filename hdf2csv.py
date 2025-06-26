# HDF5 to CSV File Converter
# Author: Biomedical Eng. Ariel Viña-González, MSc [Ph.D. candidate]

# Usage Note: The script must be run in the same directory as the HDF5 files.

import h5py
import pandas as pd
import numpy as np
from pathlib import Path

def hdf5_table_to_csv(hdf5_path, table_path, csv_path, decode="utf-8"):
    """
    Exports a compound dataset from within an HDF5 file to CSV.

    Parameters
    ----------
    hdf5_path : str | Path
        Source .hdf5 file.
    table_path : str
        Internal path to the dataset (e.g., '/data_collection/events/experiment/MessageEvent').
    csv_path : str | Path
        Destination .csv file.
    decode : str
        Encoding used to convert bytes→str.
    """
    hdf5_path, csv_path = Path(hdf5_path), Path(csv_path)

    with h5py.File(hdf5_path, "r") as f:
        if table_path not in f:
            raise KeyError(f"'{table_path}' does not exist in {hdf5_path}")
        ds = f[table_path]

        # Ensure it is a compound dataset
        if ds.dtype.names is None:
            raise TypeError(f"'{table_path}' is not a compound table")

        arr = ds[:]                  # load the entire array

    # Build a dictionary column by column
    data = {}
    for name in arr.dtype.names:
        col = arr[name]

        # === 1. Fixed-length byte fields (dtype 'Sxx') =========================
        if np.issubdtype(col.dtype, np.bytes_):
            data[name] = np.char.decode(col, decode)   # faster than list-comprehension

        # === 2. 'object' fields with loose bytes (vlen strings) =========
        elif col.dtype == object and isinstance(col[0], (bytes, bytearray)):
            data[name] = [x.decode(decode, errors="replace") for x in col]

        # === 3. Other types: numeric, bool, native str ==================
        else:
            data[name] = col

    pd.DataFrame(data).to_csv(csv_path, index=False)
    print(f"Exported '{table_path}' → {csv_path.resolve()}")

# Generate the .csv files

# Example: export the eye-tracker's message table
hdf5_table_to_csv("eyetracker_sub1.hdf5",      # <----- change this ID 
                  "/data_collection/events/experiment/MessageEvent",
                  "MessageEvent.csv")

# Export the binocular sample records
hdf5_table_to_csv("eyetracker_sub1.hdf5",      # <----- change this ID 
                  "/data_collection/events/eyetracker/BinocularEyeSampleEvent",
                  "BinocularEyeSampleEvent.csv")
