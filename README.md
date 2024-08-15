# SQL Data Retriever

A Python application that uses Streamlit and generative AI to convert natural language questions into SQL queries and retrieve data from an SQLite database.

## Overview

The SQL Data Retriever app allows users to input questions in plain English, which are then translated into SQL queries using advanced generative AI. The app retrieves and displays data from an SQLite database based on these queries, making it easier for users to gain insights without needing to write SQL code.

## Features

- **Natural Language Processing**: Converts questions into complex SQL queries.
- **Supports Complex Queries**: Handles ranking, partitioning, window functions, set operations, date/time queries, and subqueries.
- **User-Friendly Interface**: Built with Streamlit for an intuitive user experience.
- **Real-Time Data Retrieval**: Executes queries and displays results in real-time.

## Technologies Used

- **Python**: Core language for development.
- **Streamlit**: For building the interactive web interface.
- **SQLite**: Database management system.
- **Google Generative AI**: To generate SQL queries from natural language questions.

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/sql-data-retriever.git
    ```

2. **Navigate to the Project Directory**

    ```bash
    cd sql-data-retriever
    ```

3. **Install Required Packages**

    Make sure you have Python installed. Then, install the required packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**

    Create a `.env` file in the project root and add your Google API key:

    ```plaintext
    API_KEY=your_google_api_key
    ```

## Usage

1. **Run the Streamlit App**

    ```bash
    streamlit run app.py
    ```

2. **Open the App**

    The app will be available at `http://localhost:8501`. Open this URL in your web browser.

3. **Input Your Question**

    Enter a natural language question related to the data in the SQLite database.

4. **View Results**

    The app will display the results of the data generated through the SQL query from your question.
