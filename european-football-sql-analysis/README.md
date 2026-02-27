# European Football Data Analysis with SQL

## Project Overview

This project focuses on the analysis of European football match data using SQL and Python.

The objective is to extract, transform and analyze structured relational data in order to answer business-oriented analytical questions related to:

- League performance
- Team consistency
- Goal statistics
- Seasonal trends
- Player attributes
- Offensive efficiency

The project demonstrates advanced SQL querying skills combined with Python-based data visualization and analysis.

---

## Dataset Description

The database contains historical football data including:

- Countries
- Leagues
- Teams
- Matches
- Players
- Player attributes

The relational structure allows the use of complex JOIN operations to reconstruct match contexts and performance indicators.

---

## Key Analytical Questions

The analysis answers the following types of questions:

### 1. League and Country Analysis
- Identification of leagues by country
- Filtering competitions by country (e.g. Netherlands)

### 2. Team Analysis
- Extraction of team data
- Top teams per season
- Offensive statistics

### 3. Match-Level Analysis
- Home vs Away goals
- Seasonal evolution of average goals
- Country-based performance trends

### 4. Advanced Seasonal Aggregations
For selected countries (Spain, Germany, France, Italy, England):

- Number of stages per season
- Number of teams
- Average home goals
- Average away goals
- Goal difference
- Total goals per season

### 5. Team Consistency Analysis (Variance Approach)

A variance-based approach was implemented to measure offensive consistency:

- Extraction of match-level home goals for selected teams
- Calculation of:
  - Mean goals per match
  - Variance of goals scored
- Identification of the most consistent offensive team

This allows performance evaluation beyond simple goal totals.

### 6. Player Physical & Performance Analysis

Using Player and Player_Attributes tables:

- Height distribution (rounded values)
- Average overall rating by height
- Average potential
- Average weight

SQL aggregations were used to group and summarize player characteristics.

### 7. Extended Analysis – Weather Impact (API Integration)

The project also explores how external factors such as weather conditions could impact match results using external API data.

This demonstrates the ability to extend relational analysis with external data sources.

---

## Technical Stack

- SQL (JOIN, GROUP BY, HAVING, CASE, subqueries)
- Python
- Pandas
- Matplotlib
- CSV file handling
- REST API integration (Weather API)

---

## SQL Concepts Demonstrated

- INNER JOIN
- LEFT JOIN
- Aggregation functions (COUNT, SUM, AVG)
- GROUP BY
- HAVING
- CASE statements
- Subqueries
- Data filtering
- Sorting and limiting results

---

## Key Insights

- Offensive consistency can be more predictive than total goals scored.
- Seasonal goal averages vary significantly by country.
- Some leagues demonstrate higher scoring variability over time.
- Variance analysis provides a more robust metric for performance stability.

---

## Business Relevance

This project simulates real-world sports analytics use cases:

- Performance benchmarking
- Team stability measurement
- Tactical evaluation
- Data-driven decision support

The analytical methods used here are transferable to other industries such as:

- Sales performance analysis
- Financial volatility analysis
- Operational efficiency monitoring

---

## Project Structure
european-football-sql-analysis/
│
├── football_sql_analysis_europe.ipynb
├── variance_buts_2014_2015.csv
├── README.md
└── requirements.txt