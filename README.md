![Static Badge](https://img.shields.io/badge/python_version-3.12-blue?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/Django_version-4.2-orange?style=for-the-badge)

# Best Hotel

<img src="./bestHotel/static/bestHotelApp/images/example.png">

## Description
Best Hotel is a simple hotel search application that allows users to search for hotels based on specific locations. It provides a user-friendly interface to enter the location and view the search results.

The application is built using Django.

## Installation
1. Clone the repository
2. Navigate to the project directory
3. Create a virtual environment
````
python -m venv venv
````
4. Activate the virtual environment
````
# For Windows
venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate
````
5. Install the required packages
````
pip install -r requirements.txt
````
6. Run the makefile
> [!NOTE]
> This file contains all the commands to run the application. It will simply ask you to create a superuser and then run the server.
````
make run
````

## Environment Variables for CSV Import

To import the remote CSV files (using HTTP authentication), set the following environment variables :

- `BEST_HOTEL_USERNAME` : HTTP username
- `BEST_HOTEL_PASSWORD` : HTTP password

Example (macOS/Linux):
```zsh
export BEST_HOTEL_USERNAME="your-username"
export BEST_HOTEL_PASSWORD="your-password"
```

If these variables are not set, you will be prompted for them when running the import command.

## Automated Daily Import (Cron job)

This project uses [django-crontab](https://github.com/kraiz/django-crontab) to schedule the daily import of hotel and city data from remote CSV files.

- The import runs every day at 2:00 AM automatically.
- The cron job is registered automatically when you run `make run`.

> [!NOTE]
> Make sure your environment variables `BEST_HOTEL_USERNAME` and `BEST_HOTEL_PASSWORD` are set in the environment where the cron runs.
