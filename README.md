

# `eda_toolkit`

## Overview

`eda_toolkit` is a comprehensive tool designed for Exploratory Data Analysis (EDA) using Python and Streamlit. This repository provides functionalities for uploading, visualizing, and analyzing datasets from CSV and Excel files. Key features include interactive data displays, various statistical analyses, visualization options, and dataset management tools specifically tailored for data insights. Ideal for data analysts and researchers looking to gain quick insights from their data.

## Features

- **File Upload**: Upload datasets in CSV or Excel formats.
- **Data Display**: View data in a table format with basic statistics (mean, median, standard deviation).
- **Initial Data Analysis**: Generate basic statistical analysis and visualizations like line charts, bar charts, and pie charts.
- **Analysis Suggestions**: Recommendations for suitable analysis methods based on column data types.
- **Dataset Management**: Features to filter and sort data by categories, dates, or item codes.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/eda_toolkit.git
   cd eda_toolkit
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv env
   source env/bin/activate  # For macOS/Linux
   env\Scripts\activate     # For Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Create a `.env` file** with necessary environment variables:

   ```ini
   DATABASE_URL=sqlite:///mydatabase.db
   SECRET_KEY=mysecretkey
   ```

2. **Run the Streamlit application**:

   ```bash
   streamlit run main.py
   ```

## File Structure

- **`app.py`**: Main application file with functionality for uploading, displaying, and analyzing data.
- **`main.py`**: Entry point to start the Streamlit app.
- **`upload.py`**: Functions for handling file uploads.
- **`display.py`**: Functions for displaying data tables and statistics.
- **`visualization.py`**: Functions for generating charts and visualizations.
- **`recommendations.py`**: Functions for providing analysis suggestions.
- **`management.py`**: Functions for managing and filtering datasets.
- **`.env`**: File for environment variables.
- **`requirements.txt`**: List of Python dependencies.
- **`sample_data.csv`**: Example dataset for testing.

## Contributing

If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to your branch.
4. Open a pull request to the main repository.

## License

## Contact

For any questions or feedback, please contact paris.u2528@gmail.com

---

