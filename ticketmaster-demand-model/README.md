[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/9NdxGEaf)
# MY472-AT24-final

The instructions are available in the file [MY472-AT24-final-instructions.md](/MY472-AT24-final-instructions.md).


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
