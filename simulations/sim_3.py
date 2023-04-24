from time_class import Time, build_from_minutes
from utils import high_value_time
import random

NS: int

IA: tuple[int, int]
TA: tuple[int, int]

CLL: int
T: Time
TPLL: Time
TPS: Time
TE: Time


def run_simulation_3(simulation_duration):
    global TPLL

    set_initial_conditions()

    while T < simulation_duration:
        run_simulation()

    if NS != 0:
        empty_system()


def set_initial_conditions():
    global NS, CLL, T, TPLL, TPS, TA, IA, TE
    NS = 0
    CLL = 0
    T = Time(0, 0)
    TPLL = Time(0, 0)
    TPS = high_value_time()
    IA = (0, 10)
    TA = (10, 20)
    TE = Time(0, 0)


def run_simulation():
    if TPLL <= TPS:
        arrive_routine()
    else:
        leave_routine()


def arrive_routine():
    global T
    T = TPLL
    calculate_TPLL()
    regrets = regret_routine()
    calculate_TA()
    if not regrets:
        increment_NS()
        increment_CLL()
        print("Input: ", T)
        if NS == 1:
            calculate_TA()


def regret_routine():
    if TE < Time(0, 10):
        return False
    r = random.random()
    if TE > Time(0, 20):
        if r <= 0.1:
            return False
        else:
            return True
    if r <= 0.6:
        return False
    else:
        return True


def leave_routine():
    global T, TPS
    T = TPS
    decrement_NS()
    if NS > 0:
        calculate_TA()
    else:
        TPS = high_value_time()
    print("Output: ", T)


def empty_system():
    global TPLL
    TPLL = high_value_time()
    while NS != 0:
        run_simulation()


def calculate_TPLL():
    global TPLL
    random_number = random.randint(IA[0], IA[1])
    TPLL = TPLL + build_from_minutes(random_number)


def calculate_TA():
    global TPS
    random_number = random.randint(TA[0], TA[1])
    TPS = T + build_from_minutes(random_number)


def decrement_NS():
    global NS
    NS -= 1


def increment_NS():
    global NS
    NS += 1


def increment_CLL():
    global CLL
    CLL += 1
