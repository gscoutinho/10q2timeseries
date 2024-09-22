# SEC 10-Q Data Transformer

This package transforms 10-Q data obtained from the SEC EDGAR database into pandas DataFrames suitable for machine learning applications.

## Features

- Fetches 10-Q data using a company's stock ticker.
- Transforms the data into a structured pandas DataFrame.
- Indexes the DataFrame by timestamps (filing end dates).
- Columns represent parameters from the 10-Q forms.
- Values correspond to 'USD' fields from the data.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/GabrielCoutinhoEng/sec_10q_transformer.git
