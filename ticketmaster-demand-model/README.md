

# Ticketmaster Demand Analysis – Understanding Event Attendance Challenges

This project required me to simulate a real-world data science task for an organization struggling to meet a core objective. I chose **Prompt 3**, assuming the role of a junior data scientist hired by a large event organization (e.g., Ticketmaster) that is facing difficulties in maximizing event attendance. My task was to compile and prepare new real-world data that could be used in future analyses to better understand audience behavior and improve turnout.

### Project Overview

The goal of this project was to collect, clean, and structure data that could help diagnose potential reasons why attendance at live events might be lower than expected. The focus was on identifying geographical, demographic, and event-related factors that influence demand.

### Primary Data Source

- **Ticketmaster API**: The primary data for this report was collected using the Ticketmaster Discovery API, which provides detailed information on upcoming events. This dataset includes event details (e.g., names, dates, prices, venues, genres). At time of analysis, data was collected for events in the United States scheduled between January 22, 2025, and December 30, 2025.

### Secondary Data Source

- **U.S. Census Bureau API**:To supplement the primary data, I collected state-level median household income data from a publicly accessible Wikipedia page hosting US Census Data. This provides a socioeconomic dimension for analyzing event ticket affordability across states. 2024 census data was unavailable, so median household incomes for 2025 were projected using compound growth.


### Technologies Used

- **R** and RMarkdown
- **APIs**: Ticketmaster Discovery API, U.S. Census Bureau API
- **Libraries**: `httr`, `jsonlite`, `tidyverse`, `dplyr`, `ggplot2`, `sf`


This repository contains the **data, code, and outputs** for analyzing event pricing, distribution, and affordability using **Ticketmaster event data** and **supplementary income data**.

---

## 1. Data (`data/`) - Stored on Google Drive  

**Note:** The raw and processed datasets **are NOT stored in this repository** due to GitHub file size limitations.  
Instead, they are **automatically downloaded** from **Google Drive** if not found locally.

🔗 **[Google Drive Link](https://drive.google.com/drive/folders/15DqYdFKfxjGo4M8ALNLGr1NESapbc9UQ?usp=sharing)** – Files can also be manually downloaded if needed.

### Data Files:
- **`ticketmaster_events.csv`** – Raw event data retrieved from the **Ticketmaster API** (pre-scraped).  
  *Stored on Google Drive.*
- **`ticketmaster_events.sqlite`** – **SQLite database** containing processed event metrics (aggregated and cleaned data).  
  *Stored on Google Drive.*
- **`shapefiles/`** – Geospatial files from the **US Census Bureau** for state-level mapping.
- **`filtered_income_table.csv`** – Scraped **state-level income data** (Projected for 2025, sourced from Wikipedia).

---

## 2. Graphs (`graphs/`) - Stored in Repository  

Contains **visual outputs** from the analysis, including both **static and interactive** visualizations.

- **Static Visualizations** – `.png` files for **heatmaps, bar charts**, and other graphical outputs.
- **Interactive Visualizations** – `.html` files for **interactive charts**.

---

## 3. Report  
- **`MY472-AT24-final-report.Rmd`** – R Markdown file containing the **full code, analysis, and report**.  
- **`MY472-AT24-final-report.html`** – **HTML file** containing the report (generated from `.Rmd`).  
- **`MY472-AT24-final-instructions.md`** – **Instructions** for replication and submission details.

---

## 4. Handling Large Files  

GitHub has **file size limitations**, so large files (**CSV, SQLite database**) are stored in **Google Drive** instead.  
This ensures **faster cloning** and **efficient reproducibility**.

### How to Download Data:
- The script **automatically downloads** the required files if they do not exist locally.
- Alternatively, you can **manually download** the files from **Google Drive**.

---

## 5. Re-Scraping the Ticketmaster API  

If you wish to **re-fetch data** from the **Ticketmaster API**:

1. The **API scraping script** is **included but disabled** by default to **prevent excessive API requests**.
2. If needed, **uncomment** the API block in the script and **run it manually**.
