from time_class import Time, build_from_minutes
import sys

current_users = 0
total_arrives = 0
arrive_times_total = Time(0, 0)
leave_times_total = Time(0, 0)
time = Time(0, 0)

next_arrive_time = Time(0, 0)
next_leave_time = Time(sys.maxsize, 59)  # Set next_leave_time to a high value


def run_simulation(first_arrive, end_simulation_time):
    global next_arrive_time
    global next_leave_time
    next_arrive_time = first_arrive

    while time < end_simulation_time:
        run_simulation_2()

    if current_users != 0:
        next_arrive_time = Time(sys.maxsize, 59)

    while current_users != 0:
        run_simulation_2()

    average_stay = (leave_times_total - arrive_times_total).divide_time_in_parts(total_arrives)

    # Output
    print("The value of T is:", time)
    print("Current users: ", current_users)
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
            next_leave_time = Time(sys.maxsize, 59)
        print("salida: ", time)


def get_next_arrive_time():
    global next_arrive_time
    next_arrive_time = next_arrive_time + build_from_minutes(20)


def get_next_leave_time():
    global next_leave_time
    global time
    next_leave_time = time + build_from_minutes(30)


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


if __name__ == '__main__':
    run_simulation(Time(8, 0), Time(12, 0))

