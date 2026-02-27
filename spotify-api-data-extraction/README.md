# 🎵 Spotify API – Data Extraction Project

## 📌 Project Overview

This project demonstrates how to interact with the Spotify Web API using Python in order to extract, process, and structure music data.

The objective was to:

- Authenticate using the Spotify API (Client Credentials Flow)
- Retrieve artist information
- Search for albums and tracks
- Extract structured data from JSON responses
- Build a clean Pandas DataFrame
- Handle pagination (API limits)
- Convert raw data (milliseconds → readable duration)

---

## 🛠 Technologies Used

- Python
- Requests
- Pandas
- Spotify Web API
- JSON manipulation

---

## 🔐 Authentication

The project uses the **Client Credentials Flow** to obtain an access token from Spotify:

- Client ID
- Client Secret
- POST request to Spotify Accounts API
- Bearer token authentication

---

## 📊 Data Extracted

For example, for *The Beatles*, the following data was collected:

- Track ID
- Track Name
- Artists
- Album Name
- Release Date
- Duration (converted from ms to mm:ss)
- Popularity score

---

## 🔄 API Pagination Handling

Since Spotify limits results to 50 items per request, a pagination system using `limit` and `offset` parameters was implemented to retrieve all available tracks.

---

## 🧹 Data Cleaning

- JSON parsing
- Handling nested fields
- Joining multiple artists
- Duration conversion from milliseconds to readable format
- Creation of a structured Pandas DataFrame

---

## 📈 Example Output

| Track Name | Album | Duration | Popularity |
|------------|--------|----------|------------|
| Here Comes The Sun | Abbey Road | 3:05 | 86 |

---

## 📎 Key Learnings

- Understanding REST API architecture
- Managing authentication tokens
- Working with JSON structures
- Handling rate limits and API constraints
- Structuring raw API data into analytical format

---

## 🚀 Future Improvements (Optional)

- Export data to CSV
- Build a Streamlit dashboard
- Deploy as a FastAPI service