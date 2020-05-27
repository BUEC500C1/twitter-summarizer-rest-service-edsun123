"""
This file handles connections to the USGS API to retrieve data from the Waltham
gauge.

Link  to the web interface (not the api) 
https://waterdata.usgs.gov/nwis/uv?site_no=01104500
"""
import pandas as pd
import requests
from .keys import HTTPException

# Constants
USGS_URL = 'https://waterservices.usgs.gov/nwis/iv/'

# ~ ~ ~ ~


def get_usgs_data() -> pd.DataFrame:
    """This function  runs through the whole process for retrieving data from
    usgs: first we perform the request, and then we clean the data.

    Returns:
        Pandas Dataframe containing the usgs data.
    """
    res = request_to_usgs()
    df = parse_usgs_data(res)
    return df


def request_to_usgs() -> requests.models.Response:
    """
    Get a request from the USGS.

    Returns:
        Request Response containing the data from the request.
    """
    
    payload = {
        'format': 'json',
        'sites': '01104500',
        'period': 'P7D',
        'parameterCd': '00060,00065',
        'siteStatus': 'all'
    }
    
    res = requests.get(USGS_URL, params=payload)
    if res.status_code // 100 in [4, 5]:
        raise HTTPException(res.status_code)
    return res


def parse_usgs_data(res) -> pd.DataFrame:
    """
    Clean the response from the USGS API.

    Args:
        res: response object from USGS

    Returns:
        Pandas DataFrame containing the usgs data.
    """

    raw_data = res.json()

    discharge_volume = raw_data['value']['timeSeries'][0]['values'][0]['value']
    gage_height = raw_data['value']['timeSeries'][1]['values'][0]['value']

    data_list = [
        {
            'time': vol_entry['dateTime'],
            'stream_flow': vol_entry['value'],
            'gage_height': height_entry['value']
        }
        for vol_entry, height_entry
        in zip(discharge_volume, gage_height)
    ]

    df = pd.DataFrame(data_list)
    try:
        # Not time zone aware
        df['time'] = (
            pd.to_datetime(df['time'])  # Convert to Pandas datetime format
            .dt.tz_localize('UTC')  # This is UTC; define it as such
            .dt.tz_convert('US/Eastern')  # Take the UTC time and convert to EST
            .dt.tz_localize(None)  # Remove the timezone from the datetime
        )
    except TypeError:
        # Now try if already timezone aware
        df['time'] = pd.to_datetime(df['time']).dt.tz_localize(None)

    return df
