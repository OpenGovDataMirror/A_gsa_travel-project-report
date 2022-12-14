#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 06:44:31 2019

@author: austinpeel
"""


segment_columns = {
 '21 Days' : {'description':'whether ticket was bought more than 21 days ago','source':'','type':'','keep':True},
 'Business_x' :{'description':'if business class','source':'','type':'','keep':False},
 'CPP Business_x' : {'description':'if a CPP business class','source':'','type':'','keep':False},
 'DG_x' : {'description':'if a DG class ticket','source':'','type':'','keep':True},
 'DashCA_x' : {'description':'if a _CA  ticket','source':'','type':'','keep':True},
 'First_x' :  {'description':'if a first class  ticket','source':'','type':'','keep':False},
 'Geocoded_City1' : {'description':'','source':'','type':'','keep':False},
 'Geocoded_City2' : {'description':'','source':'','type':'','keep':False},
 'Other_x' : {'description':'unresticed airfare ticket','source':'','type':'','keep':True},
 'YCA_x' : {'description':'if YCA ticket far','source':'','type':'','keep':True},
 'Year' : {'description':'','source':'','type':'','keep':True},
 'agency_name' : {'description':'','source':'','type':'','keep':False},
 'airline_carrier' : {'description':'airline short name','source':'','type':'','keep':False},
 'airline_carrier_name' : {'description':'airline long name','source':'','type':'','keep':True},
 'airport_1' : {'description':'','source':'','type':'','keep':False},
 'airport_2' : {'description':'','source':'','type':'','keep':False},
 'airportid_1' : {'description':'','source':'','type':'','keep':False},
 'airportid_2' : {'description':'','source':'','type':'','keep':False},
 'awarded' : {'description':'whether the route was awarded a city-pair contract','source':'','type':'','keep':True},
 'base_fare': {'description':'base fair not including taxes or fees','source':'','type':'','keep':True},
 'bi_direction_o___d_descript': {'description':'','source':'','type':'','keep':False},
 'bi_directional_o___d_code': {'description':'','source':'','type':'','keep':False},
 'cabin_svc_class_of_segment': {'description':'class of service','source':'','type':'','keep':True},
 'carrier_lg': {'description':'the airline with the most flights for route','source':'','type':'','keep':True},
 'carrier_low': {'description':'the airline with the least flights for route','source':'','type':'','keep':False},
 'city1': {'description':'','source':'','type':'','keep':False},
 'city2': {'description':'','source':'','type':'','keep':False},
 'city_pair_code': {'description':'city pair route','source':'','type':'','keep':True},
 'city_pair_description': {'description':'','source':'','type':'','keep':False},
 'citymarketid_1': {'description':'','source':'','type':'','keep':False},
 'citymarketid_2': {'description':'','source':'','type':'','keep':False},
 'continent_to_continent': {'description':'','source':'','type':'','keep':False},
 'count_x': {'description':'','source':'','type':'','keep':False},
 'country_to_country': {'description':'','source':'','type':'','keep':False},
 'department': {'description':'','source':'','type':'','keep':False},
 'destination_city_code': {'description':'destination code','source':'','type':'','keep':True},
 'destination_city_name': {'description':'','source':'','type':'','keep':False},
 'destination_continent': {'description':'','source':'','type':'','keep':False},
 'destination_country': {'description':'','source':'','type':'','keep':False},
 'domestic_international_indicator_of_segment': {'description':'','source':'','type':'','keep':False},
 'extcabinclass': {'description':'','source':'','type':'','keep':False},
 'fare': {'description':'the average non government consumers paid for fare by aggregated by quarter','source':'Dept of Transportation','type':'','keep':True},
 'fare_lg': {'description':'largest fare for consumers paid by quarter','source':'Dept of Transportation','type':'','keep':True},
 'fare_low': {'description':'the lowest consumers paid per quarter per route','source':'Dept of Transportation','type':'','keep':True},
 'fare_type': {'description':'the fare used','source':'','type':'','keep':True},
 'first_of_month_invoice_date': {'description':'','source':'','type':'','keep':False},
 'fiscal_quarter_invoice_date': {'description':'','source':'','type':'','keep':False},
 'fiscal_year_invoice_date': {'description':'','source':'','type':'','keep':False},
 'invoice_number': {'description':'','source':'','type':'','keep':False},
 'large_ms': {'description':'market share by the largest airline for route','source':'','type':'','keep':True},
 'legcntr': {'description':'','source':'','type':'','keep':False},
 'legplusmin': {'description':'','source':'','type':'','keep':False},
 'lf_ms': {'description':'','source':'','type':'','keep':False},
 'no_of_segments': {'description':'number of total segments traveller went on','source':'','type':'','keep':True},
 'nsmiles': {'description':'miles of flight','source':'','type':'','keep':True},
 'organization': {'description':'','source':'','type':'','keep':False},
 'origin_city_code': {'description':'origin code','source':'','type':'','keep':True},
 'origin_city_name': {'description':'','source':'','type':'','keep':False},
 'origin_continent': {'description':'','source':'','type':'','keep':False},
 'origin_country': {'description':'','source':'','type':'','keep':False},
 'paid_fare_including_taxes_and_fees': {'description':'the actual government paid for flight','source':'','type':'','keep':True},
 'passengers': {'description':'average passangers per quarter per route','source':'','type':'','keep':True},
 'plusmin': {'description':'','source':'','type':'','keep':False},
 'pnr': {'description':'','source':'','type':'','keep':False},
 'predominant_fare_basis_code': {'description':'','source':'','type':'','keep':False},
 'quarter': {'description':'the quarter of year travelled','source':'','type':'','keep':True},
 'reckey': {'description':'','source':'','type':'','keep':False},
 'segment_arrival_date': {'description':'','source':'','type':'','keep':False},
 'segment_departure_date': {'description':'','source':'','type':'','keep':True},
 'segment_exchange_indicator': {'description':'','source':'','type':'','keep':False},
 'segment_level_transaction_id': {'description':'','source':'','type':'','keep':False},
 'segment_refund_indicator': {'description':'','source':'','type':'','keep':False},
 'segment_sequence_number': {'description':'','source':'','type':'','keep':False},
 'tbl': {'description':'','source':'','type':'','keep':False},
 'tbl1apk': {'description':'','source':'','type':'','keep':False},
 'ticket_booking_date': {'description':'','source':'','type':'','keep':False},
 'ticket_exchange_indicator': {'description':'if ticket was exchanged','source':'','type':'','keep':True},
 'ticket_invoice_date': {'description':'','source':'','type':'','keep':False},
 'ticket_number': {'description':'','source':'','type':'','keep':True},
 'ticket_origin_airport': {'description':'','source':'','type':'','keep':False},
 'ticket_refund_indicator': {'description':'','source':'','type':'','keep':False},
 'ticketing_adv_booking_group': {'description':'how many days prior to book ticket','source':'','type':'','keep':True},
 'ticketing_departure_date': {'description':'','source':'','type':'','keep':False},
 'total_taxes': {'description':'total taxes paid','source':'','type':'','keep':True},
 'transaction_id': {'description':'','source':'','type':'','keep':False},
 'trip_departure_day_of_week': {'description':'','source':'','type':'','keep':False},
 'ITEM_NUM': {'description':'','source':'','type':'','keep':False},
 'AWARD_YEAR': {'description':'','source':'','type':'','keep':False},
 'ORIGIN_AIRPORT_ABBREV': {'description':'','source':'','type':'','keep':False},
 'DESTINATION_AIRPORT_ABBREV': {'description':'','source':'','type':'','keep':False},
 'ORIGIN_CITY_NAME': {'description':'','source':'','type':'','keep':False},
 'ORIGIN_STATE': {'description':'','source':'','type':'','keep':False},
 'ORIGIN_COUNTRY': {'description':'','source':'','type':'','keep':False},
 'DESTINATION_CITY_NAME': {'description':'','source':'','type':'','keep':False},
 'DESTINATION_STATE': {'description':'','source':'','type':'','keep':False},
 'DESTINATION_COUNTRY': {'description':'','source':'','type':'','keep':False},
 'AIRLINE_ABBREV': {'description':'','source':'','type':'','keep':False},
 'AWARDED_SERV': {'description':'','source':'','type':'','keep':False},
 'PAX_COUNT': {'description':'the government-wide passanger count per quarter','source':'city pair','type':'','keep':True},
 'YCA_FARE': {'description':'the YCA contract award amount for route ','source':'city pair','type':'','keep':True},
 'XCA_FARE': {'description':'the _DC contract award amount for route','source':'city pair','type':'','keep':True},
 'BUSINESS_FARE': {'description':'','source':'','type':'','keep':False},
 'ORIGIN_AIRPORT_LOCATION': {'description':'','source':'','type':'','keep':False},
 'DESTINATION_AIRPORT_LOCATION': {'description':'','source':'','type':'','keep':False},
 'ORIGIN_CITY_STATE_AIRPORT': {'description':'','source':'','type':'','keep':False},
 'DESTINATION_CITY_STATE_AIRPORT': {'description':'','source':'','type':'','keep':False},
 'EFFECTIVE_DATE': {'description':'','source':'','type':'','keep':False},
 'EXPIRATION_DATE': {'description':'','source':'','type':'','keep':False},
 'no_CA_award': {'description':'if contract had no _CA award for route','source':'custom','type':'','keep':True},
 'daily_demand': {'description':'an attempt at getting the amount of demand daily for route','source':'custom','type':'','keep':True},
 'DashCA_y': {'description':'','source':'','type':'','keep':False},
 'YCA_y': {'description':'','source':'','type':'','keep':False},
 'DG_y': {'description':'','source':'','type':'','keep':False},
 'Other_y': {'description':'','source':'','type':'','keep':True},
 'CPP Business_y': {'description':'','source':'','type':'','keep':False},
 'Business_y': {'description':'','source':'','type':'','keep':False},
 'First_y': {'description':'','source':'','type':'','keep':False},
 'count_y': {'description':'','source':'','type':'','keep':False},
 'dash_per_mile': {'description':'contract cost per mile (not actual)','source':'','type':'','keep':True},
 'YCA_per_mile': {'description':'contract cost per mile (not actual)','source':'','type':'','keep':True},
 'cost_per_mile': {'description':'Actual cost per mile travelled','source':'','type':'','keep':True},
 'city_pair_ratio': {'description':'the ratio of _CA to YCA fare per route','source':'','type':'','keep':True},
 'ticket': {'description':'','source':'','type':'','keep':False},
 'market_share_log': {'description':'','source':'','type':'','keep':True},
 'booking_advanced_days': {'description':'number of days purchased in advanced','source':'','type':'','keep':True},
 'Travel Authorization Number': {'description':'','source':'','type':'','keep':False},
 'Organization': {'description':'','source':'','type':'','keep':False},
 'EMAIL': {'description':'','source':'','type':'','keep':True},
 'Trip Type': {'description':'','source':'','type':'','keep':False},
 'Purpose': {'description':'','source':'','type':'','keep':True},
 'FILEDATE': {'description':'','source':'','type':'','keep':False},
 'AGYSUB_DESC': {'description':'','source':'','type':'','keep':False},
 'PAYPLAN_CODE': {'description':'','source':'','type':'','keep':False},
 'GRADE_CODE': {'description':'','source':'','type':'','keep':False},
 'grade': {'description':'','source':'','type':'','keep':True},
 'region': {'description':'','source':'','type':'','keep':True},
 'bureau': {'description':'','source':'','type':'','keep':True},
 'month': {'description':'month of departure','source':'','type':'','keep':True},
 'day_of_week': {'description':'day of week of departure','source':'reservation','type':'','keep':True},
 'self_booking_indicator': {'description':'booked online or on phone','source':'reservation','type':'','keep':True},
 'booking_days_log': {'description':'log of days','source':'reservation','type':'','keep':True},
 'booking_days_standarized': {'description':'standarized transformation of booking lead time','source':'reservation','type':'','keep':True},

 }


#for transactions
       
aggregate_fields = {
'air_extra_total' :'air extra voucher',
'fees_total' : 'fees voucher',
'transporation_total' : 'transportation voucher',
'lodging_total' : 'lodging voucher',
'meals_total' : 'meals voucher',
'rental_car_total' :'rental voucher',
'local_transport_total' : 'local transportation voucher' ,
'air_extra_card' : 'airline extra transaction report',
'transportation_card' : 'transportation transaction report',
'local_transport_card' : 'local transportation transaction report',
'fees_card' : 'fees transaction report',
'rental_card' :'rental transaction report'
}



transaction_columns= {

 'Employee Email Address': {'description':'email address','source':'voucher','type':'','keep':True},
 'FY': {'description':'year of travel','source':'voucher','type':'','keep':True},
 'Total Amount': {'description':'total amount of travel cost','source':'voucher','type':'','keep':False},
 'Baggage Fees': {'description':'total baggage fees','source':'voucher','type':'air extra','keep':False},
 'Charge Card Fees': {'description':'fees on card','source':'voucher','type':'fees','keep':False},
 'Airline Flight_total': {'description':'total cost of airflight','source':'voucher','type':'transportation','keep':False},
 'Bus_total': {'description':'total spent on bus','source':'voucher','type':'transportation','keep':False},
 'Train_total': {'description':'total spent on train','source':'voucher','type':'transportation','keep':False},
 'Communication Serv_total': {'description':'','source':'','type':'','keep':False},
 'Foreign Travel': {'description':'','source':'','type':'','keep':False},
 'Laundry_total': {'description':'','source':'','type':'','keep':False},
 'Lodging_total': {'description':'Total Spent on Lodging','source':'voucher','type':'lodging','keep':False},
 'Lodging Resort Fee': {'description':'resort fee','source':'voucher','type':'lodging','keep':False},
 'Lodging Tax': {'description':'lodging tax','source':'voucher','type':'lodging','keep':False},
 'Lodging-PerDiem': {'description':'','source':'','type':'','keep':False},
 'M&IE-PerDiem_total': {'description':'Meals and Incidentals','source':'voucher','type':'meals','keep':False},
 'Meals Actuals': {'description':'','source':'voucher','type':'meals','keep':False},
 'Mileage - Private Airplane': {'description':'','source':'voucher','type':'POV','keep':False},
 'Mileage - Priv Auto (Advantageous)': {'description':'','source':'voucher','type':'POV','keep':False},
 'Mileage - Priv Auto (GOV Avail/Not Used)': {'description':'','source':'voucher','type':'POV','keep':False},
 'Mileage - Priv Motorcycle': {'description':'','source':'voucher','type':'POV','keep':False},
 'Misc Expense_total': {'description':'','source':'voucher','type':'misc','keep':True},
 'Registration Fees_total': {'description':'','source':'voucher','type':'fees','keep':False},
 'Rental Car_total': {'description':'','source':'voucher','type':'rental','keep':False},
 'Rental Car - Gasoline_total': {'description':'','source':'voucher','type':'rental','keep':False},
 'Rental Car - Optional Equipment': {'description':'','source':'voucher','type':'rental','keep':False},
 'Spec Med Needs Empl': {'description':'','source':'','type':'','keep':False},
 'Service Fees': {'description':'','source':'','type':'fees','keep':False},
 'Highway/Bridge Tolls_total': {'description':'','source':'voucher','type':'local transportation','keep':False},
 'Limousine Service': {'description':'','source':'voucher','type':'local transportation','keep':False},
 'Parking_total': {'description':'','source':'voucher','type':'local transportation','keep':False},
 'Public Transportation_total': {'description':'voucher','source':'','type':'local transportation','keep':False},
 'Seat Selection Fee': {'description':'','source':'voucher','type':'air extra','keep':False},
 'Shuttle - Air': {'description':'','source':'voucher','type':'local transportation','keep':False},
 'Shuttle - Ground': {'description':'','source':'voucher','type':'local transportation','keep':False},
 'Taxi_total': {'description':'','source':'voucher','type':'local transportation','keep':False},
 'Transxn Fees_total': {'description':'','source':'voucher','type':'fees','keep':False},
 'Travel Transxn Fees_total': {'description':'','source':'voucher','type':'fees','keep':False},
 'daysTravelled': {'description':'','source':'','type':'','keep':False},
 'trip_count': {'description':'amount of trips individual travelled in fiscal year','source':'voucher','type':'','keep':True},
 'Airline Flight_card': {'description':'amount of money put on card for ariline expenses, usually seat and baggage upgrades','source':'transaction report','type':'airline extra','keep':False},
 'Bus_card': {'description':'bus transportation on credit card','source':'transaction report','type':'transportation','keep':False},
 'Cash Disburse': {'description':'','source':'transaction report','type':'','keep':True},
 'Communication Serv_card': {'description':'','source':'transaction report','type':'','keep':False},
 'Highway/Bridge Tolls_card': {'description':'','source':'transaction report','type':'local transportation','keep':False},
 'Laundry_card': {'description':'','source':'transaction report','type':'','keep':False},
 'Lodging_card': {'description':'','source':'transaction report','type':'lodging','keep':True},
 'M&IE-PerDiem_card': {'description':'','source':'transaction report','type':'meals','keep':True},
 'Misc Expense_card': {'description':'','source':'transaction report','type':'misc','keep':True},
 'Parking_card': {'description':'','source':'transaction report','type':'local transportation','keep':False},
 'Public Transportation_card': {'description':'','source':'transaction report','type':'','keep':False},
 'Registration Fees_card': {'description':'','source':'transaction report','type':'fees','keep':False},
 'Rental Car_card': {'description':'','source':'transaction report','type':'rental','keep':False},
 'Rental Car - Gasoline_card': {'description':'transaction report','source':'transaction report','type':'rental','keep':False},
 'Taxi_card': {'description':'','source':'transaction report','type':'local transportation','keep':False},
 'Train_card': {'description':'','source':'transaction report','type':'transporation','keep':False},
 'Transxn Fees_card': {'description':'','source':'transaction report','type':'fees','keep':False},
 'Travel Transxn Fees_card': {'description':'','source':'transaction report','type':'fees','keep':False},
 'days': {'description':'days travelled total','source':'custom','type':'','keep':True},
 'air_extra_total': {'description':'baggage and seat selection cost on vouchers','source':'custom','type':'','keep':True},
 'air_extra_total_per_day': {'description':'baggage and seat selection per day of travel','source':'','type':'','keep':False},
 'fees_total': {'description':'total fees incurred','source':'','type':'','keep':True},
 'fees_total_per_day': {'description':'total fees per day of travel','source':'','type':'','keep':True},
 'transporation_total': {'description':'total transportation cost origin + destination','source':'','type':'','keep':True},
 'transporation_total_per_day': {'description':'','source':'custom','type':'','keep':False},
 'lodging_total': {'description':'lodging total','source':'custom','type':'','keep':True},
 'lodging_total_per_day': {'description':'lodging spendt per day of travel','source':'custom','type':'','keep':True},
 'meals_total': {'description':'meals and incendtals total cost','source':'custom','type':'','keep':True},
 'meals_total_per_day': {'description':'meal cost per day of travel','source':'custom','type':'','keep':True},
 'rental_car_total': {'description':'rental cost','source':'custom','type':'','keep':True},
 'rental_car_total_per_day': {'description':'rental cost per day of travel','source':'custom','type':'','keep':True},
 'local_transport_total': {'description':'local transportation cost','source':'custom','type':'','keep':True},
 'local_transport_total_per_day': {'description':'local transportation per day of travel','source':'custom','type':'','keep':True},
 'air_extra_card': {'description':'baggage and seat selection on card','source':'custom','type':'','keep':True},
 'air_extra_card_per_day': {'description':'baggage and seat selection on card per day','source':'custom','type':'','keep':False},
 'transportation_card': {'description':'transportation cost on card','source':'custom','type':'','keep':True},
 'transportation_card_per_day': {'description':'transportation cost per day of travel','source':'custom','type':'','keep':True},
 'local_transport_card': {'description':'local transport on card','source':'custom','type':'','keep':True},
 'local_transport_card_per_day': {'description':'local transport on card per day of travel','source':'custom','type':'','keep':True},
 'fees_card': {'description':'fees captured on card','source':'custom','type':'','keep':True},
 'fees_card_per_day': {'description':'fees on card per day','source':'custom','type':'','keep':True},
 'rental_card': {'description':'rental card cost on card','source':'custom','type':'','keep':True},
 'rental_card_per_day': {'description':'rental card cost per day','source':'custom','type':'','keep':True},
 
 }


trip_columns = [
'fiscal_year',
 'booking_date',
 'city_pair_code',
 'compare_fare',
 'continent_to_continent',
 'country_to_country',
 'destination_city_name',
 'destination_country',
 'domestic_international_indicator',
 'fare_type',
 'lowest_available_fare',
 'no_of_tickets',
 'number_of_segments',
 'origin_city_name',
 'origin_country',
 'round_trip_indicator',
 'self_booking_indicator',
 'ticket_departure_date',
 'total_flight_miles',
 'total_taxes_amount',
 'trip_departure_day_of_week',
 'trip_duration',
 'refund',
 'exchange',
 'base_fare',
 'paid_fare_including_taxes_and_fees',
 'total_taxes',
 'refunded_amount',
 'EMAIL',
 'Trip Return Date',
 'Trip Departure Date',
 'Current Status',
 'Trip Type',
 'Purpose',
 'TDY Location',
 'Total Amount',
 'FILEDATE',
 'AGYSUB_DESC',
 'PAYPLAN_CODE',
 'GRADE_CODE',
 'Hotel Reservation Start Date',
 'Hotel Reservation End Date',
 'Advance Purchase Window',
 'Confirmation Number_x',
 'Rate Code',
 'Fedroom Rate IND',
 'Hotel Property',
 'Hotel Vendor',
 'Hotel Vendor Family',
 'Hotel Property Location',
 'Hotel Property Country',
 'Total Number of Nights',
 'Total Rooms',
 'Nightly Rate(Excl Taxes)',
 'Total Hotel Reservation Spend',
 'Organization',
 'ONLINE/OFFLINE_y',
 'Booking Source_y',
 'Rental Car Vendor',
 'Rental Car Type',
 'Rental Car City/Location',
 'Rental Car Country',
 'Total Days',
 'Total Rental Cars',
 'Total Rental Car Spend',
 'Rental Car Daily Rate(Excl Tax)']