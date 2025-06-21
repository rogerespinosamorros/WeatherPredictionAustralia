# WeatherPredictionAustralia

## Sources
1. Bureau of Meteorology (BoM – Australia)
Official national weather and climate agency.

Provides:

ACORN-SAT (high-quality station data)

National temperature and rainfall anomaly maps

Climate summaries and seasonal reports

Source: http://www.bom.gov.au

🌐 2. Climate Change in Australia (CCiA – CSIRO & BoM)
Joint portal from CSIRO and BoM offering:

Climate projections and scenarios

Historical gridded datasets (NetCDF format)

Site: https://www.climatechangeinaustralia.gov.au

🏛️ 3. data.gov.au
Australian government open data portal.

We found:

CSV file of annual temperature anomaly (1910–2020) from the State of the Environment Report

Example dataset: CLI_001.csv

🌍 4. NOAA / NCEI (USA)
Source of the Global Historical Climatology Network – Monthly (GHCN-M v4) dataset.

Internationally trusted for long-term, standardized temperature records.

What we used:

ghcnm.tavg.latest.qcu.dat (temperature)

ghcnm.tavg.latest.qcu.inv (station metadata)

FTP: https://www.ncei.noaa.gov/pub/data/ghcn/v4/