def create_log_file():
    from datetime import datetime
    import os 
    username = os.getlogin()
    now = datetime.now()
    year = now.year 
    month = now.month 
    day = now.day
    hours = now.hour
    minutes = now.minute
    seconds = now.second
    formatted_date = f'{day}-{month}-{year} {hours}:{minutes}:{seconds}'
    print(formatted_date)
    with open('log.txt', 'a') as file:
        file.write(f'{username} - {formatted_date} - Some checked the about the pages \n')

create_log_file()