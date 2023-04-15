from time_class import Time, build_from_minutes
from utils import high_value_time
import random

NS = 0
CLL = 0
STLL = Time(0, 0)
STS = Time(0, 0)
ITO = Time(0, 0)
STO = Time(0, 0)
T = Time(0, 0)
simulation_start_time = Time(0, 0)

TPLL = Time(0, 0)
TPS = high_value_time()

first_value_output_range = 0
second_value_output_range = 10

IA = (0, 0)
TA = (0, 0)


def run_simulation_1(first_input, end_simulation_time, ia, ta):
    global TPLL

    initialize_variables(first_input, ia, ta)

    while T < end_simulation_time:
        run_simulation()

    if NS != 0:
        TPLL = high_value_time()

    while NS != 0:
        run_simulation()

    PPS = calculate_PPS()
    PTO = calculate_PTO()

    print("The simulation started at: " + str(simulation_start_time) + " and ended at: " + str(end_simulation_time))
    # not sure about that, check later
    print("The system was fully empty at:", T)
    print("Total of users: ", CLL)
    print("The average stay in the system is:", PPS)
    print("Total idle time:", STO)
    print("The percentage of idle time is: %" + str(PTO))


def initialize_variables(first_input, ia, ta):
    global simulation_start_time, TPLL, ITO, TA, IA
    simulation_start_time = first_input
    TPLL = first_input
    ITO = first_input  # para que no me tome el primer user como idle time, dsp ver otra manera
    IA = ia
    TA = ta


def calculate_PTO():
    return (STO.to_minutes() * 100 / (T - simulation_start_time).to_minutes()).__trunc__()


def calculate_PPS():
    return (STS - STLL).divide_time_in_parts(CLL)


def run_simulation():
    global T, TPS
    if TPLL <= TPS:
        T = TPLL
        increment_NS()
        sum_time_to_STLL()
        increment_CLL()

        calculate_TPLL()
        print("Input: ", T)
        if NS == 1:
            calculate_TPS()
            end_ITO()
    else:
        T = TPS
        sum_time_to_STS()
        decrement_NS()

        if NS > 0:
            calculate_TPS()
        else:
            start_ITO()
            TPS = high_value_time()
        print("Output: ", T)


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
