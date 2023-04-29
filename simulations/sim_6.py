from time_class import Time, build_from_minutes
import random

TC: Time

IA_FDP: tuple[int, int]
TA_FDP: tuple[int, int]

CLL: int
T: Time
TPLL: Time
TE: Time
STE: Time
STA: Time
STO: Time
TA: Time

PTE: Time


def run_simulation_6(simulation_duration):
    set_initial_conditions()

    while T < simulation_duration:
        arrive_routine()

    calculate_PTE()
    print("Cantidad de personas total:", CLL)
    print("Promedio de tiempo de espera en la cola:", PTE)


def set_initial_conditions():
    global CLL, T, TPLL, TA_FDP, IA_FDP, TE, STE, STA, STO, TC, TA
    CLL = 0
    TC = Time(0, 0)
    T = Time(0, 0)
    TA = Time(0, 0)
    TPLL = Time(0, 0)
    IA_FDP = (5, 20)
    TA_FDP = (10, 20)  # Vamos a usar una equiprobable para no calcular la función de gauss
    TE = Time(0, 0)
    STE = Time(0, 0)
    STA = Time(0, 0)


def arrive_routine():
    global T
    T = TPLL
    calculate_TPLL()
    regrets = regret_routine()
    if not regrets:
        calculate_TA()
        sum_TA()
        increment_CLL()
        if TC < T:
            idleTimeRoutine()
        else:
            waitRoutine()

        print("Calculated TA:", TA)
        print("Input: ", T)


def regret_routine():
    print("TIME: ", T)
    print("TC: ", TC)
    if (TC - T) < Time(0, 10):
        return False
    r = random.random()
    if (TC - T) > Time(0, 20):
        if r <= 0.1:
            return False
        else:
            return True
    if r <= 0.6:
        return False
    else:
        return True


def idleTimeRoutine():
    global STO, TC
    STO = STO + (T - TC)
    TC = T + TA


def waitRoutine():
    pass


def sum_TA():
    global STA
    STA = STA + TA


def sum_TE():
    global STE
    STE = STE + TE


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
