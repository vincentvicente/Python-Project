## NAME: QIYUAN ZHU
## DATE: 12/06/2023
## EMAIL ID: zhu.qiyu@northeastern.edu
from datetime import datetime
import time
from User import User
from Appointment import Appointment
from AppointmentDiary import AppointmentDiary

# Define the Time class
class Time:
    """Represents time in hours, minutes, and AM/PM format."""

    def __init__(self, hours, minutes, am_pm):
        self.hours = hours
        self.minutes = minutes
        self.am_pm = am_pm


# Define the Date class
class Date:
    """Represents date with attributes for year, month, and day."""

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


# Function to add a new user
def add_new_user(users):
    """Adds a new user to the system."""
    new_username = input("Enter the new username: ").lower()

    # Check for valid characters in the username
    if not all(char.isalnum() or char in ['.', '_'] for char in new_username):
        print("Error: Invalid characters in username.")
        return

    # Check for existing username
    if new_username in users:
        print("Error: User already exists.")
    else:
        users[new_username] = User(new_username)
        print(f"User '{new_username}' added successfully.")


# Function to delete an existing user
def delete_user(users):
    """Deletes an existing user from the system."""
    username = input("Enter the username to be deleted: ").lower()

    if username in users:
        del users[username]
        print(f"User '{username}' deleted successfully.")
    else:
        print("Error: User not found.")


# Function to add a new user
def add_new_user(users):
    """Adds a new user to the system."""
    new_username = input("Enter the new username: ").lower()

    # Check for valid characters in the username
    if not all(char.isalnum() or char in ['.', '_'] for char in new_username):
        print("Error: Invalid characters in username.")
        return

    # Check for existing username
    if new_username in users:
        print("Error: User already exists.")
    else:
        users[new_username] = User(new_username)
        print(f"User '{new_username}' added successfully.")


# Function to delete an existing user
def delete_user(users):
    """Deletes an existing user from the system."""
    username = input("Enter the username to be deleted: ").lower()

    if username in users:
        del users[username]
        print(f"User '{username}' deleted successfully.")
    else:
        print("Error: User not found.")


# Function to list existing users
def list_users(users):
    """Lists all existing users."""
    if not users:
        print("No existing users.")
        return

    print("Existing users:")
    for username in sorted(users):
        print(username)


# Function to schedule an appointment
def schedule_appointment(users):
    """Schedules an appointment for a user."""
    username = input("Enter username: ").lower()

    if username not in users:
        print("Error: Invalid user.")
        return

    date_entry = input("Enter the date (YYYY-MM-DD) for the appointment: ")
    try:
        date = datetime.strptime(date_entry, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    time_entry = input("Enter the start time (HH:MM AM/PM) for the appointment: ")
    try:
        start_time = datetime.strptime(time_entry, "%I:%M %p").time()
    except ValueError:
        print("Invalid time format. Please use HH:MM AM/PM.")
        return

    end_time_entry = input("Enter the end time (HH:MM AM/PM) for the appointment: ")
    try:
        end_time = datetime.strptime(end_time_entry, "%I:%M %p").time()
    except ValueError:
        print("Invalid time format. Please use HH:MM AM/PM.")
        return

    purpose = input("Enter the purpose of the appointment: ")

    new_appointment = Appointment(date, start_time, end_time, purpose)
    users[username].appointment_diary.add_appointment(new_appointment)
    print("Appointment scheduled successfully.")


# Function to cancel an appointment
def cancel_appointment(users):
    """Cancels an appointment for a user."""
    username = input("Enter username: ").lower()

    if username not in users:
        print("Error: Invalid user.")
        return

    date_entry = input("Enter the date (YYYY-MM-DD) of the appointment to cancel: ")
    try:
        date = datetime.strptime(date_entry, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    start_time_entry = input("Enter the start time (HH:MM AM/PM) of the appointment to cancel: ")
    try:
        start_time = datetime.strptime(start_time_entry, "%I:%M %p").time()
    except ValueError:
        print("Invalid time format. Please use HH:MM AM/PM.")
        return

    found = False
    for appointment in users[username].appointment_diary.appointments:
        if appointment.date == date and appointment.start_time == start_time:
            users[username].appointment_diary.appointments.remove(appointment)
            print("Appointment canceled successfully.")
            found = True
            break

    if not found:
        print("No matching appointment found.")


# Function to retrieve purpose of an appointment
def retrieve_purpose(users):
    """Retrieves the purpose of an appointment for a user."""
    username = input("Enter username: ").lower()

    if username not in users:
        print("Error: Invalid user.")
        return

    date_entry = input("Enter the date (YYYY-MM-DD) of the appointment: ")
    try:
        date = datetime.strptime(date_entry, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    time_entry = input("Enter the start time (HH:MM AM/PM) of the appointment: ")
    try:
        time = datetime.strptime(time_entry, "%I:%M %p").time()
    except ValueError:
        print("Invalid time format. Please use HH:MM AM/PM.")
        return

    found = False
    for appointment in users[username].appointment_diary.appointments:
        if appointment.date == date and appointment.start_time == time:
            print(f"Purpose of the appointment: {appointment.purpose}")
            found = True
            break

    if not found:
        print("No matching appointment found.")


def reschedule_appointment(users):
    """Reschedules an existing appointment for a user."""
    username = input("Enter username: ").lower()

    if username not in users:
        print("Error: Invalid user.")
        return

    date_entry = input("Enter the current date (YYYY-MM-DD) of the appointment: ")
    try:
        date = datetime.strptime(date_entry, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    start_time_entry = input("Enter the current start time (HH:MM AM/PM) of the appointment: ")
    try:
        start_time = datetime.strptime(start_time_entry, "%I:%M %p").time()
    except ValueError:
        print("Invalid time format. Please use HH:MM AM/PM.")
        return

    for appointment in users[username].appointment_diary.appointments:
        if appointment.date == date and appointment.start_time == start_time:
            new_date_entry = input("Enter the new date (YYYY-MM-DD) for the appointment: ")
            try:
                new_date = datetime.strptime(new_date_entry, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                return

            new_start_time_entry = input("Enter the new start time (HH:MM AM/PM) for the appointment: ")
            try:
                new_start_time = datetime.strptime(new_start_time_entry, "%I:%M %p").time()
            except ValueError:
                print("Invalid time format. Please use HH:MM AM/PM.")
                return

            new_end_time_entry = input("Enter the new end time (HH:MM AM/PM) for the appointment: ")
            try:
                new_end_time = datetime.strptime(new_end_time_entry, "%I:%M %p").time()
            except ValueError:
                print("Invalid time format. Please use HH:MM AM/PM.")
                return

            new_purpose = input("Enter the new purpose for the appointment: ")

            # Update the appointment details
            appointment.date = new_date
            appointment.start_time = new_start_time
            appointment.end_time = new_end_time
            appointment.purpose = new_purpose

            print("Appointment rescheduled successfully.")
            return

    print("No appointment found!")


# Function to check for an appointment on a certain date and time
def check_appointment(users):
    """Checks for an appointment on a specific date and time for a user."""
    username = input("Enter username: ").lower()

    if username not in users:
        print("Error: Invalid user.")
        return

    date_entry = input("Enter the date (YYYY-MM-DD) to check: ")
    try:
        date = datetime.strptime(date_entry, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    time_entry = input("Enter the time (HH:MM AM/PM) to check: ")
    try:
        time = datetime.strptime(time_entry, "%I:%M %p").time()
    except ValueError:
        print("Invalid time format. Please use HH:MM AM/PM.")
        return

    found = False
    for appointment in users[username].appointment_diary.appointments:
        if appointment.date == date and appointment.start_time == time:
            print(f"Appointment found on {date} between {appointment.start_time} to {appointment.end_time}.")
            found = True
            break

    if not found:
        print("No appointment found.")

def main():
    users = {}

    while True:
        print("Welcome to Appointment Management System! What would you like to do?")
        print("• [a] Add new user")
        print("• [d] Delete an existing user")
        print("• [l] List existing users")
        print("• [s] Schedule an appointment")
        print("• [c] Cancel an appointment")
        print("• [f] Check for appointment on certain date and time")
        print("• [p] Retrieve purpose of an appointment")
        print("• [r] Reschedule an existing appointment")
        print("• [x] Exit the system")

        choice = input("Enter choice: ").lower()

        if choice == 'a':
            add_new_user(users)
            time.sleep(1)  # Delay for 1 second after completing the operation
        elif choice == 'd':
            delete_user(users)
            time.sleep(1)
        elif choice == 'l':
            list_users(users)
            time.sleep(1)
        elif choice == 's':
            schedule_appointment(users)
            time.sleep(1)
        elif choice == 'c':
            cancel_appointment(users)
            time.sleep(1)
        elif choice == 'f':
            check_appointment(users)
            time.sleep(1)
        elif choice == 'p':
            retrieve_purpose(users)
            time.sleep(1)
        elif choice == 'r':
            reschedule_appointment(users)
            time.sleep(1)
        elif choice == 'x':
            print("Goodbye!")
            break
        else:
            print("Invalid Option")


if __name__ == "__main__":
    main()
