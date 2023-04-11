from time_class import Time, build_from_minutes
from utils import high_value_time
import random

current_users = 0
total_arrives = 0
arrive_times_total = Time(0, 0)
leave_times_total = Time(0, 0)
time = Time(0, 0)

next_arrive_time = Time(0, 0)
next_leave_time = high_value_time()


def run_simulation(first_arrive, end_simulation_time):
    global next_arrive_time
    global next_leave_time
    next_arrive_time = first_arrive

    while time < end_simulation_time:
        run_simulation_2()

    if current_users != 0:
        next_arrive_time = high_value_time()

    while current_users != 0:
        run_simulation_2()

    average_stay = (leave_times_total - arrive_times_total).divide_time_in_parts(total_arrives)

    # Output
    print("The simulation ended at:", end_simulation_time)  # not sure about that, check later
    print("The system was fully empty at:", time)
    print("Total of users: ", total_arrives)
    print("The average stay in the system is:", average_stay)


def run_simulation_2():
    global time
    global next_arrive_time
    global next_leave_time
    if next_arrive_time <= next_leave_time:
        time = next_arrive_time
        increment_current_users()
        sum_time_to_total_arrive_times()
        increment_total_arrives()

        get_next_arrive_time()
        print("llegada: ", time)
        if current_users == 1:
            get_next_leave_time()
    else:
        time = next_leave_time
        sum_time_to_total_leave_times()
        decrement_current_users()

        if current_users > 0:
            get_next_leave_time()
        else:
            next_leave_time = high_value_time()
        print("salida: ", time)


def get_next_arrive_time():
    global next_arrive_time
    random_number = random.randint(10, 30)
    next_arrive_time = next_arrive_time + build_from_minutes(random_number)


def get_next_leave_time():
    global next_leave_time
    global time
    random_number = random.randint(20, 40)
    next_leave_time = time + build_from_minutes(random_number)


def sum_time_to_total_leave_times():
    global leave_times_total
    global time
    leave_times_total = leave_times_total + time


def sum_time_to_total_arrive_times():
    global arrive_times_total
    global time
    arrive_times_total = arrive_times_total + time


def decrement_current_users():
    global current_users
    current_users -= 1


def increment_current_users():
    global current_users
    current_users += 1


def increment_total_arrives():
    global total_arrives
    total_arrives += 1
