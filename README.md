# Introduction
This program is designed to manage an appointment system for multiple users. 

It supports various operations such as `adding users`, `scheduling appointments`, `canceling appointments`, and `checking appointments`.

# Execution
1. Clone the repository or download the program files to your local machine.

2. Ensure all the required files for different classes (User, Time, Date, Appointment, AppointmentDiary) are in the same directory.

3. Navigate to the directory where the program files are located.

4. Run the following command to start the program:
```commandline
python main.py
```
Once the program starts, follow the on-screen instructions to add users, schedule appointments, and perform other actions.

Expected Input Formats:
```
Date: YYYY-MM-DD
Time: HH:MM AM/PM
```
Example Use:
> To schedule an appointment for the user neu on 2023-04-16 from 9:30 AM to 10:10 AM, follow the on-screen prompts after selecting the "Schedule an appointment" option.

## Known Issues 
### Current Issues:
* No persistent data storage across runs: 
User data and appointment diaries do not persist once the program exits. This means all data will be lost when the system is restarted. However, this is not a requirement of the assignment, so it is acceptable behavior. If I had more time, I would implement file-based storage to persist user data.
* Potential Solutions:
To address the persistence issue, I would implement file-based storage, perhaps using JSON or a SQLite database to store the user and appointment data. When the program starts, it could read the data from the file and repopulate the user and appointment data structures.

## Classes Overview
This program consists of the following core classes:

### 1. `User`:
Represents a user of the system with the following attributes:

* username: The user's name.
* appointment_diary: An instance of the AppointmentDiary class to manage this user's appointments.
### 2. `Time`:
Handles time in hours and minutes with AM/PM notation, containing:

`hours`: The hour of the appointment.

`minutes`: The minutes of the appointment.

`am_pm`: The period (AM or PM) of the time.
### 3. `Date`
Represents a specific date, containing:

`year`: The year of the appointment.

`month`: The month of the appointment.

`day`: The day of the appointment.

### 4. `Appointment`
Represents an individual appointment, containing:

`date`: The date of the appointment.

`start_time`: The start time of the appointment.

`end_time`: The end time of the appointment.

`purpose`: The purpose of the appointment.
### 5. `AppointmentDiary`
Maintains a list of all appointments for a user, providing methods to:
* Schedule new appointments.
* Cancel existing appointments.
* Check if an appointment exists at a specific time.
* Retrieve the purpose of an appointment.
* Reschedule appointments.