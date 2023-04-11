from time_class import Time, build_from_minutes
from utils import high_value_time
import random

current_users = 0
users_total = 0
input_time_total = Time(0, 0)
output_time_total = Time(0, 0)
idle_time_start = Time(0, 0)
total_idle_time = Time(0, 0)
time = Time(0, 0)

next_input_time = Time(0, 0)
next_output_time = high_value_time()


def run_simulation_1(first_input, end_simulation_time):
    global next_input_time
    global next_output_time
    global idle_time_start

    next_input_time = first_input
    idle_time_start = first_input  # para que no me tome el primer user como idle time, dsp ver otra manera

    while time < end_simulation_time:
        run_simulation()

    if current_users != 0:
        next_input_time = high_value_time()

    while current_users != 0:
        run_simulation()

    average_stay = calculate_average_stay()
    idle_time_percentage = calculate_idle_time_percentage()

    print("The simulation started at: " + str(first_input) + " and ended at: " + str(end_simulation_time))
    # not sure about that, check later
    print("The system was fully empty at:", time)
    print("Total of users: ", users_total)
    print("The average stay in the system is:", average_stay)
    print("Total idle time:", total_idle_time)
    print("The percentage of idle time is: %" + str(idle_time_percentage))


def calculate_idle_time_percentage():
    return (total_idle_time.to_minutes() * 100 / time.to_minutes()).__trunc__()
    # este calculo esta mal, no deberia usar el time si no la duracion de la simulacion


def calculate_average_stay():
    return (output_time_total - input_time_total).divide_time_in_parts(users_total)


def run_simulation():
    global time
    global next_output_time
    if next_input_time <= next_output_time:
        time = next_input_time
        increment_current_users()
        sum_time_to_total_input_time()
        increment_users_total()

        get_next_input_time()
        print("Input: ", time)
        if current_users == 1:
            get_next_output_time()
            end_idle_time()
    else:
        time = next_output_time
        sum_time_to_total_output_time()
        decrement_current_users()

        if current_users > 0:
            get_next_output_time()
        else:
            start_idle_time()
            next_output_time = high_value_time()
        print("Output: ", time)


def start_idle_time():
    global idle_time_start
    idle_time_start = time


def end_idle_time():
    global total_idle_time
    total_idle_time = total_idle_time + (time - idle_time_start)


def get_next_input_time():
    global next_input_time
    random_number = random.randint(25, 30)
    next_input_time = next_input_time + build_from_minutes(random_number)


def get_next_output_time():
    global next_output_time
    random_number = random.randint(10, 20)
    next_output_time = time + build_from_minutes(random_number)


def sum_time_to_total_output_time():
    global output_time_total
    output_time_total = output_time_total + time


def sum_time_to_total_input_time():
    global input_time_total
    input_time_total = input_time_total + time


def decrement_current_users():
    global current_users
    current_users -= 1


def increment_current_users():
    global current_users
    current_users += 1


def increment_users_total():
    global users_total
    users_total += 1
