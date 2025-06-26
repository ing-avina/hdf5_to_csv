# HDF5 to CSV Converter

A simple Python script to convert compound datasets within HDF5 files to CSV format.

## About This Script
This script provides a straightforward way to extract specific tabular data (compound datasets) from HDF5 files and save them as human-readable CSV files. It was originally developed to process eye-tracker data recorded in HDF5 format but is generic enough to work with any HDF5 file containing compound datasets.

The script is particularly useful for data analysis workflows where CSV is a more convenient format for tools like Pandas, R, Excel, or for sharing with colleagues.

## Features
Targeted Extraction: Extracts a specific dataset from an HDF5 file using its internal path.

Handles String Decoding: Correctly decodes byte strings (both fixed-length Sxx and variable-length objects) into standard UTF-8 strings, a common requirement for scientific data files.

Dependency-based: Uses well-known libraries like h5py for HDF5 interaction and pandas for robust CSV creation.

Easy to Use: Simply configure the file paths at the bottom of the script and run.

## Requirements
Python 3.6+, h5py, pandas, numpy

You can install the required libraries using pip:  pip install h5py pandas numpy

## Usage
Placement: Place the script in the same directory as your HDF5 file(s).

Configuration: Open the script and modify the parameters in the hdf5_table_to_csv() function calls at the end of the file:

hdf5_path: Your source HDF5 file (e.g., "eyetracker_sub1.hdf5").

table_path: The internal path to the dataset you want to convert (e.g., "/data_collection/events/experiment/MessageEvent").

csv_path: The name of the output CSV file (e.g., "MessageEvent.csv").

## Example configuration from the script:

Python

### Example 1: Export the message event table from the eye-tracker
hdf5_table_to_csv("eyetracker_sub1.hdf5",      # <--- Change this ID
                  "/data_collection/events/experiment/MessageEvent",
                  "MessageEvent.csv")

### Example 2: Export binocular sample logs
hdf5_table_to_csv("eyetracker_sub1.hdf5",      # <--- Change this ID
                  "/data_collection/events/eyetracker/BinocularEyeSampleEvent",
                  "BinocularEyeSampleEvent.csv")

The script will generate the corresponding CSV files in the same directory.
