from time_class import Time, build_from_minutes
from utils import high_value_time
import random

NS: int

IA: tuple[int, int]
TA: tuple[int, int]

PPS: Time
PTO: int

STLL: Time
STS: Time
CLL: int
ITO: Time
STO: Time
T: Time
TPLL: Time
TPS: Time


def run_simulation_1(simulation_duration):
    global TPLL

    set_initial_conditions()

    while T < simulation_duration:
        run_simulation()

    if NS != 0:
        empty_system()

    calculate_results()
    show_results()


def set_initial_conditions():
    global NS, CLL, STLL, STS, ITO, STO, T, TPLL, TPS, TA, IA
    NS = 0
    CLL = 0
    STLL = Time(0, 0)
    STS = Time(0, 0)
    ITO = Time(0, 0)
    STO = Time(0, 0)
    T = Time(0, 0)
    TPLL = Time(0, 0)
    TPS = high_value_time()
    IA = (0, 10)
    TA = (10, 20)


def run_simulation():
    if TPLL <= TPS:
        arrive_routine()
    else:
        leave_routine()


def arrive_routine():
    global T
    T = TPLL
    calculate_TPLL()
    sum_time_to_STLL()
    increment_NS()
    increment_CLL()
    print("Input: ", T)
    if NS == 1:
        calculate_TPS()
        end_ITO()


def leave_routine():
    global T, TPS
    T = TPS
    sum_time_to_STS()
    decrement_NS()
    if NS > 0:
        calculate_TPS()
    else:
        start_ITO()
        TPS = high_value_time()
    print("Output: ", T)


def empty_system():
    global TPLL
    TPLL = high_value_time()
    while NS != 0:
        run_simulation()


def calculate_results():
    global PPS, PTO
    PPS = calculate_PPS()
    PTO = calculate_PTO()


def show_results():
    print("The system was fully empty after:", T)
    print("Total of users: ", CLL)
    print("The average stay in the system is:", PPS)
    print("Total idle time:", STO)
    print("The percentage of idle time is: %" + str(PTO))


def calculate_PTO():
    return (STO.to_minutes() * 100 / T.to_minutes()).__trunc__()


def calculate_PPS():
    return (STS - STLL).divide_time_in_parts(CLL)


def start_ITO():
    global ITO
    ITO = T


def end_ITO():
    global STO
    STO = STO + (T - ITO)


def calculate_TPLL():
    global TPLL
    random_number = random.randint(IA[0], IA[1])
    TPLL = TPLL + build_from_minutes(random_number)


def calculate_TPS():
    global TPS
    random_number = random.randint(TA[0], TA[1])
    TPS = T + build_from_minutes(random_number)


def sum_time_to_STS():
    global STS
    STS = STS + T


def sum_time_to_STLL():
    global STLL
    STLL = STLL + T


def decrement_NS():
    global NS
    NS -= 1


def increment_NS():
    global NS
    NS += 1


def increment_CLL():
    global CLL
    CLL += 1
