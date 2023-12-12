# Crawl Data from KAYAK

This project involves crawling flight data from KAYAK. The following tasks will be performed:

## Setup Environment

Git clone

```
git clone https://github.com/TNB142/crawl_data_kayak.git
```

Create active virtual environment

```
cd crawl_data_kayak
.\venv\Scripts\activate.bat
```

Run scrawling

```
python main.py
```

## Features

### main.py

**At default configuration, the flight search parameters are set as follows:**

- **Sources:** ['SGN', 'SGN']
- **Destinations:** ['DAD', 'HAN']
- **Start Date:** '2023-12-21' (date of search initiation)
- **End Date:** '2023-12-21' (to determine the number of search dates)

**Additional Information:**

- **Browser to Crawl:** Firefox with headless option
- **URL:** `f"https://www.vn.kayak.com/flights/{sources[i]}-{destinations[i]}/{start_date+j}?sort=bestflight_a&fs=airlines=~VN"`, where "a&fs=airlines=~VN" filters results for only Vietnam Airlines.
- **Set Time (set_time):** Time at which crawling begins
- **Current Time (c_time):** The current time, with the timezone set to VN.

_Note: Please verify and adjust the code as needed, and ensure it follows the Markdown format._

### scrawl_function.py

**Get Information on Kayak Website using BeautifulSoup (bs4) to Parse HTML Format:**

- **get_airlines():** Retrieves airlines information.
- **get_total_stops():** Retrieves stops information.
- **get_price():** Retrieves prices information.
- **get_time_flight():** Retrieves time to departing information.
- **get_duration():** Retrieves duration time of the journey.

**Set Up Sources, Destinations, and Crawling DateTime:**

- **get_source_destination():** Retrieves sources and destinations variables. Modify it to obtain your desired data.
- **get_start_end_time():** Retrieves start_time and end_time variables. Modify it to obtain your desired data. Input format is %Y-%M-%d.

_Note: Ensure you modify the functions according to your specific requirements and input formats._
