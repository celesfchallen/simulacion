from time_class import Time, build_from_minutes
from utils import high_value_time
import random

TC: int

IA_FDP: tuple[int, int]
TA_FDP: tuple[int, int]

CLL: int
T: Time
TPLL: Time
TE: Time
TA: Time
STE: Time

PTE: Time


def run_simulation_3(simulation_duration):
    global TPLL

    set_initial_conditions()

    while T < simulation_duration:
        arrive_routine()

    calculate_PTE()
    print("Cantidad de personas total:", CLL)
    print("Promedio de tiempo de espera en la cola:", PTE)


def set_initial_conditions():
    global CLL, T, TPLL, TA_FDP, IA_FDP, TE, Calculated_TA, TA, STE
    CLL = 0
    T = Time(0, 0)
    TPLL = Time(0, 0)
    IA_FDP = (0, 10)
    TA_FDP = (10, 20)
    TE = Time(0, 0)
    Calculated_TA = []
    TA = Time(0, 0)
    STE = Time(0, 0)


def arrive_routine():
    global T
    T = TPLL
    calculate_TPLL()
    regrets = regret_routine()
    if not regrets:
        increment_CLL()
        calculate_TA()
        sum_TE()
        set_TA()

        print("Calculated TA:", TA)
        print("Input: ", T)


def regret_routine():
    print("TIME: ", T)
    print("TE: ", TE)
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


def sum_TE():
    global STE
    STE = STE + TE


def set_TPS():
    global TPS
    TPS = T + Calculated_TA[0]


def empty_system():
    global TPLL
    TPLL = high_value_time()
    while NS != 0:
        run_simulation()


def update_TE():
    global TE
    TE = TE - Calculated_TA[0]
    Calculated_TA.pop(0)


def set_TA():
    global TE
    Calculated_TA.append(TA)
    TE = TE + TA


def calculate_TPLL():
    global TPLL
    random_number = random.randint(IA_FDP[0], IA_FDP[1])
    TPLL = TPLL + build_from_minutes(random_number)


def calculate_TA():
    global TA
    random_number = random.randint(TA_FDP[0], TA_FDP[1])
    TA = build_from_minutes(random_number)


def increment_CLL():
    global CLL
    CLL += 1


def calculate_PTE():
    global PTE
    PTE = STE.divide_time_in_parts(CLL)
