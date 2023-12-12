import pandas as pd
import os
class scrawl_data:
    def __init__(self,source,destination):
        self.column_names = ["Airline", "Source", "Destination","Duration" ,"Total stops", "Price","Time_flight","Search_time"]
        self.df = pd.DataFrame(columns = self.column_names)
        self.source = source
        self.destination = destination
    def get_data(self):
        return self.df
    def add_data(self,current_time,airlines,duration,total_stops,prices,time_flights):
        self.df = self.df._append(pd.DataFrame({
            'Search_time':current_time,
            'Airline': airlines,
            'Duration': duration,
            'Total stops' : total_stops,
            'Price' : prices,
            'Time_flight' :time_flights,
                                    }))
        self.df['Source'] = self.source
        self.df['Destination'] = self.destination
        self.df = self.df.replace('\n','', regex=True)
        self.df = self.df.reset_index(drop = True)
        # print(self.df[['Airline','Price','Time_flight']])
        # return self.df

    def column_names_(self):
        print(self.column_names)

    def save_data(self,count,save_state=False):
        print(self.df[['Airline','Price','Time_flight']])
        path_save = './save_data/'
        folder_name = f'{self.source}_{self.destination}'
        if save_state:
            if os.path.exists(f"{path_save}{folder_name}"):
                self.df.to_csv(f"{path_save}{folder_name}/{self.source}_{self.destination}_{count}.csv",index=False)
                print(f"Succesfully saved {self.source} => {self.destination} route as {self.source}_{self.destination}_{count}.csv ")
            else:
                # if the demo_folder directory is not present
                # then create it.
                os.makedirs(f"{path_save}{folder_name}")
                self.df.to_csv(f"{path_save}{folder_name}/{self.source}_{self.destination}_{count}.csv",index=False)
                print(f"Succesfully saved {self.source} => {self.destination} route as {self.source}_{self.destination}_{count}.csv ")
        else:
            print("save_state parameter is current False. Set save_state = True to save data")

