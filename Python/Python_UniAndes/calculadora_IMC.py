
LB_KG = 0.45
M_PUL = 0.025

def calcular_BMI(peso_lb: float, altura_inch: float) -> float:
    try:
        v_kg = peso_lb * LB_KG
        mt_a = altura_inch * M_PUL

        # BMI = peso/(altura^2)
        bmi = v_kg / mt_a**2

        bmi = round(bmi, 2)

        return f'{bmi} kg/m'
    
    except ZeroDivisionError:
        return 'Error!... Division por cero'

p_lib = 130.07
a_pul = 66.53

print(calcular_BMI(p_lib, a_pul))
    