class CO2_calculator:

    def one_km_weigth(km):
        # weigth [g] CO2 for 1 litr
        litr_nafta = 2640
        litr_benzin = 2390


        avg_l = 6 #AVG consumption of your car for 100 km

        one_km = litr_benzin*avg_l/100
        total = round(one_km * km/1000, 2)
        week = round(total*5, 1)
        print('for one km: ',one_km, 'g of CO2')
        print('today you save', total, 'kg of CO2')
        print('you should save', week,'kg in week')

    def cal_hour(duration):
        #from mountain bike moderate cycling
        minute_cycling = 791/60
        total_cal = duration*minute_cycling
        print('you burn total', total_cal,'cal')
        print('you should burn additional', total_cal*5,'cal in one week' )

#add your common car route distance
CO2_calculator.one_km_weigth(12.8*2)
#add the duration fro czcling minutes
CO2_calculator.cal_hour(55+45)



