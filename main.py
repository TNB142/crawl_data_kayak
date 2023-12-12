from scrawl_function import *
from data_format import scrawl_data

if __name__ == "__main__":
    sources, destinations = get_source_destination()

    set_time,c_time = get_couple_check_and_current_time()

    start_date, end_date, num_days = get_start_end_time()

    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)
    driver.quit()

    count = 0

    while True:
        if c_time == set_time:
            # print(f"Do job {count}")
            print(f"Crawl airlines at {count} times")
            current_time = get_current_time()
            print("Crawling Time")
            for i in tqdm(range(len(sources))):
                df = scrawl_data(sources[i],destinations[i])
                for j in tqdm(range(num_days+1)):
                    # close and open driver every 10 days to avoid captcha
                    if count % 1 == 0:
                        driver.quit()
                        driver = webdriver.Firefox(options=options)#, chrome_options=chromeOptions)
                    #Modifile link url to get another airline. In this section, I focus on Vietnam Airline cause I just crawl flight data in VietNam only.
                    url = f"https://www.vn.kayak.com/flights/{sources[i]}-{destinations[i]}/{start_date+j}?sort=bestflight_a&fs=airlines=~VN"
                    driver.get(url)
                    print("\n")
                    print("\n---Wait 15s for loading the page completely---")
                    time.sleep(15)

                    soup = BeautifulSoup(driver.page_source, 'html.parser')

                    airlines, total_stops, prices, duration, time_flight = get_all_necessary_data(soup)
                    time_flights=[]
                    for x in time_flight:
                        time_flights.append(f'{start_date+j} {x}')

                    df.add_data(current_time,airlines,duration,total_stops,prices,time_flights)
                    df.save_data(count,save_state=True)

            # Wait for 15 minutes before running again
            print("\nWaiting for 15 minutes before running again...")
            time.sleep(14*60)  # Wait for 15 minutes (15 minutes * 60 seconds) (Set at 14 about the delay time of code excutation)
            print("---Resuming scraping---")
            count+=1
            driver.refresh()
            # sleep(15)
            set_time, c_time = get_couple_check_and_current_time(check_state = False)
        else:
            c_time=wait_time_count()
            sleep(1)
            continue

