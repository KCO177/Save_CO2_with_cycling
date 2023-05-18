import pandas as pd

class data_strava:

    def strava_csv():
        strava_data = pd.read_csv('C:/Users/START/PycharmProjects/CO2 saver/export_109512466/activities.csv')
        df = pd.DataFrame(strava_data)
        strava_df_filtered = df[['Activity Date', 'Activity Type', 'Elapsed Time', 'Distance']]
        #print(strava_df_filtered)
        filtered_ride = strava_df_filtered[strava_df_filtered['Activity Type'].str.contains('Ride')]
        filtered_ride_to_job = filtered_ride[filtered_ride['Distance'] < 20]
        total_distance = filtered_ride_to_job['Distance'].sum()
        total_time = (filtered_ride_to_job['Elapsed Time'].sum()) / 3600

        #print(filtered_ride)
        #print('total distance ', total_distance, 'time')
        #print('total time elapsed ', total_time, 'hours')
        data = [total_distance, total_time]
        return (data)

class CO2_calculator:

    def one_km_weigth(km):
        # weigth [g] CO2 for 1 litr
        #litr_nafta = 2640
        litr_benzin = 2390
        cena_ben = 36.7
        avg_l = 6.5 #AVG consumption of your car for 100 km

        one_km = litr_benzin*avg_l/100
        total_km = round((km/100) * avg_l, 2)
        print('total consuption', total_km)
        total = round(one_km * km/1000, 2)
        price = round(cena_ben * total_km, 2)
        print('for one km: ',one_km, 'g of CO2')
        print('for all rides you save: ', total, 'kg of CO2')
        print('you save', total_km, 'l in price:', price, 'Kc')
        #print('today you save', total, 'kg of CO2')
        #print('you should save', week,'kg in week')

    def cal_hour(duration):
        #from mountain bike moderate cycling
        minute_cycling = 791/60
        total_cal = round(duration*minute_cycling, 2)
        print('you burn total', total_cal,'cal')
        #print('you should burn additional', total_cal*5,'cal in one week' )

#add your common car route distance


km_into_the_job = 12.4*2*4
min_into_the_job = 120

print('for job travels:')
print('green km into the job',km_into_the_job, 'km')
CO2_calculator.one_km_weigth(km_into_the_job)
CO2_calculator.cal_hour(min_into_the_job*4)
print('-----------------------')


data = data_strava.strava_csv()
tot_km = round(data[0])
tot_dur = round(data[1])
print('allover rides to job:')
print('You ride total: ', tot_km , 'km')
print('In duration: ', tot_dur, 'hours')
CO2_calculator.one_km_weigth(tot_km)
CO2_calculator.cal_hour(tot_dur*60)




