# 🪙 Live Cryptocurrency Dashboard

A real-time cryptocurrency dashboard that displays live market data for the top 10 cryptocurrencies by market capitalization, fetched from the CoinGecko API.

*[Live Demo Link](https://cryptodashboardlive-eejx4koj7t5wvkyeuou5hz.streamlit.app/)*



## About The Project

This application provides a clean, user-friendly interface for monitoring the cryptocurrency market. It features auto-refreshing data to ensure the prices, 24-hour changes, and market caps are always up-to-date. The project was initially converted from a Flask application, demonstrating the ability to adapt and rebuild web apps in different frameworks.

---

### Key Features

* Live Data: Integrates with the CoinGecko API for real-time market data.
* Auto-Refresh: The dashboard automatically updates every 60 seconds.
* Polished UI: Uses Streamlit's native components (st.dataframe, column_config) for a clean and professional display of financial data.
* Custom Formatting: Displays large numbers in a human-readable format (e.g., $500.5M, $2.1B).

---

### Technologies Used

* Language: Python
* Framework: Streamlit
* Libraries: Pandas, Requests, streamlit-autorefresh

---

### Setup and Local Installation

To run this project locally, follow these steps:

1.  Clone the repository:
    bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    
2.  Create a Conda environment:
    bash
    conda create -n crypto_env python=3.9
    conda activate crypto_env
    
3.  Install dependencies:
    bash
    pip install -r requirements.txt
    
4.  Run the app:
    bash
    streamlit run app.py
