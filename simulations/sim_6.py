from time_class import Time, build_from_minutes
import random

TC: Time

IA_FDP: tuple[int, int]
TA_FDP: tuple[int, int]

CLL: int
T: Time
TPLL: Time
STE: Time
STA: Time
STO: Time
TA: Time
CE15: int

PE: Time
PPS: Time
PTA: Time
PTO: int
PE15: int
CARR: int
CARR20: int


def run_simulation_6(simulation_duration):
    global T
    set_initial_conditions()

    while T < simulation_duration:
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

    calculate_results()
    show_results()


def set_initial_conditions():
    global CLL, T, TPLL, TA_FDP, IA_FDP, STE, STA, STO, TC, TA, CE15, CARR, CARR20
    CLL = 0
    TC = Time(0, 0)
    T = Time(0, 0)
    TA = Time(0, 0)
    TPLL = Time(0, 0)
    IA_FDP = (5, 20)
    TA_FDP = (10, 20)  # Vamos a usar una equiprobable para no calcular la función de gauss
    STE = Time(0, 0)
    STA = Time(0, 0)
    STO = Time(0, 0)
    CE15 = 0
    CARR = 0
    CARR20 = 0


def regret_routine():
    if (TC - T) < Time(0, 10):
        return False
    r = random.random()
    if (TC - T) > Time(0, 20):
        if r <= 0.1:
            increment_CE15()
            return False
        else:
            increment_CARR20()
            increment_CARR()
            return True
    if r <= 0.6:
        if (TC - T) > Time(0, 15):
            increment_CE15()
        return False
    else:
        increment_CARR()
        return True


def idleTimeRoutine():
    global STO, TC
    STO = STO + (T - TC)
    TC = T + TA


def waitRoutine():
    global TC, STE
    STE = STE + (TC - T)
    TC = TC + TA


def sum_TA():
    global STA
    STA = STA + TA


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


def increment_CE15():
    global CE15
    CE15 += 1


def increment_CARR():
    global CARR
    CARR += 1


def increment_CARR20():
    global CARR20
    CARR20 += 1


def calculate_results():
    global PPS, PTA, PE, PTO, PE15
    PPS = (STE + STA).divide_time_in_parts(CLL)
    PTA = STA.divide_time_in_parts(CLL)
    PE = STE.divide_time_in_parts(CLL)
    PTO = (STO.to_minutes() * 100 / TC.to_minutes()).__trunc__()
    PE15 = ((CE15 * 100) / CLL).__trunc__()


def show_results():
    print("Cantidad de personas total:", CLL)
    print("Promedio de permanencia en el sistema:", PPS)
    print("Promedio de tiempo de atención:", PTA)
    print("Promedio de tiempo de espera en la cola:", PE)
    print("Porcentaje de tiempo ocioso: " + str(PTO) + "%")
    print("Porcentaje que esperaron más de 15' respecto del total atendidas: " + str(PE15) + "%")



