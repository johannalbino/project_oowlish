from concurrent.futures import ThreadPoolExecutor, as_completed

import pandas as pd
from core.google_maps_service import GoogleMapsAPIService
from oowlish.settings import FILES_IMPORT


def parallel_process(number_runner, input_list, function_exec, args_extract_functions):

    executor_list = list()
    result_list = list()

    with ThreadPoolExecutor(max_workers=number_runner) as executor_services:
        for data in input_list:
            args_data = args_extract_functions(data)
            executor_list.append(
                executor_services.submit(function_exec, *args_data)
            )
        for future in as_completed(executor_list):
            result = future.result()
            result_list.append(result)

    return result_list


def get_data_gmaps(data):
    result_gmaps = GoogleMapsAPIService().get_data_by_city_name(data['city'])
    has_rooftop = [loc for loc in result_gmaps if loc['geometry']['location_type'] == "ROOFTOP"]
    has_range_interpolated = [loc for loc in result_gmaps if loc['geometry']['location_type'] == "RANGE_INTERPOLATED"]
    has_geometric = [loc for loc in result_gmaps if loc['geometry']['location_type'] == "GEOMETRIC_CENTER"]
    has_approximate = [loc for loc in result_gmaps if loc['geometry']['location_type'] == "APPROXIMATE"]

    if len(has_rooftop) > 0:
        lat, lng = has_rooftop[0]['geometry']['location']['lat'], has_rooftop[0]['geometry']['location']['lng']
    elif len(has_range_interpolated) > 0:
        lat, lng = has_range_interpolated[0]['geometry']['location']['lat'], has_range_interpolated[0]['geometry']['location']['lng']
    elif len(has_geometric) > 0:
        lat, lng = has_geometric[0]['geometry']['location']['lat'], has_geometric[0]['geometry']['location']['lng']
    elif len(has_approximate) > 0:
        lat, lng = has_approximate[0]['geometry']['location']['lat'], has_approximate[0]['geometry']['location']['lng']
    else:
        lat, lng = 0, 0
    data.update({
        "latitude": lat,
        "longitude": lng
    })
    return data


def processing_file():
    file_data = pd.read_csv(f"{FILES_IMPORT}/customers.csv")
    header = list(file_data.columns.values)

    file_data = [dict(zip(header, list(row[1].values))) for row in file_data.iterrows()]
    new_data = parallel_process(100, file_data, get_data_gmaps, lambda x: [x])
    not_found_location = [not_f for not_f in new_data if not_f['latitude'] == 0 and not_f['longitude'] == 0]
    return new_data, not_found_location
