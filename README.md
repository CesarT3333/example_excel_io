# Example excel io

## Objective:

- This project aims to generate an `excel` file with a specific name according to the date and environment
- Read a list of banks to be processed and check if will process PAs or PEs or both.

## Run

````sh
python main.py 
````

### Parameters

- `--env` or `-e`: Set environment
- `--inputFile` or `-i`: Set input file

#### Example

````sh
python main.py --env dev -i resources/input/data.json
````