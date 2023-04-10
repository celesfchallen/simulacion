from time_class import Time
import sys

current_users = 0
total_arrives = 0
arrive_times_total = Time(0, 0)
leaves_times_total = Time(0, 0)


def run_simulation(first_arrive, end_simulation_time):
    next_arrive_time = first_arrive
    next_leave_time = Time(sys.maxsize, 59)  # Set tps to a high value
    time = Time(0, 0)

    while time < end_simulation_time:
        if next_arrive_time <= next_leave_time:
            time = next_arrive_time
            next_arrive_time = next_arrive_time + Time(0, 20)
            increment_current_users()
            global arrive_times_total
            arrive_times_total = arrive_times_total + time
            increment_total_arrives()
            print("llegada: ", time)
            if current_users == 1:
                next_leave_time = time + Time(0, 30)
        else:
            time = next_leave_time
            decrement_current_users()
            if current_users > 0:
                next_leave_time = next_leave_time + Time(0,30)
            else:
                next_leave_time = Time(sys.maxsize, 59)
            print("salida: ", time)


    # Step 3: Output the value of T
    print("The value of T is:", time)
    print(current_users)
    print(arrive_times_total)


def simulate(next_arrive_time, next_leave_time, time):
    if next_arrive_time <= next_leave_time:
        time = next_arrive_time
        increment_current_users()
        global arrive_times_total
        arrive_times_total = arrive_times_total + next_arrive_time
        print(time)
        print(arrive_times_total)
    else:
        time = time + next_leave_time
        decrement_current_users()
    return time


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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
