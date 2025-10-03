Complaint Type Analysis

Step 1: Load the dataset

I used the trimmed dataset `nyc_311_2024.csv` that only includes incidents opened in 2024.

Command I used to filter:
```bash
grep "2024" 311_Service_Requests_from_2010_to_Present_20250928.csv > nyc_311_2024.csv

Step 2: Inspect the data

I opened the dataset in Jupyter Notebook and assigned column names manually since the raw file had many unnamed columns.
import pandas as pd
df = pd.read_csv("nyc_311_2024.csv", header=None, low_memory=False)

Step 3: Find most common complaint types

I counted complaint types to see which appeared most often.

Illegal Parking            517532
Noise - Residential        391278
HEAT/HOT WATER             280304
Noise - Street/Sidewalk    173886
Blocked Driveway           173238
UNSANITARY CONDITION       137856
PLUMBING                    74600
Street Condition            73784
PAINT/PLASTER               72591
Abandoned Vehicle           71558

The most common complaint type in 2024 is Illegal Parking.

Step 4: Compare Jan–Feb vs Jun–Jul 2024

I plotted the number of “Illegal Parking” complaints for January–February and June–July.
	•	Jan–Feb had a high volume of complaints.
	•	Jun–Jul also had many complaints, but the level was noticeably different (trend visible in bar chart).
