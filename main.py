import numpy
from loguru import logger


def rascheti():
    # ВХОДНЫЕ ПАРАМЕТРЫ
    n_1 = 1
    n_2 = 2
    L = 200 * (10 ** (-3))  # м
    d = (10 ** (-3)) / 100  # м/шт
    delta_x_1 = 27 * (10 ** (-3))  # м
    delta_x_2 = 57 * (10 ** (-3))  # м

    logger.info(f"\nВходные параметры:\n"
                f"L: {L}\n"
                f"d: {d}\n"
                f"delta_x_1: {delta_x_1}\n"
                f"delta_x_2: {delta_x_2}")

    # НАХОЖДЕНИЕ УГЛА
    f_1 = numpy.arctan((delta_x_1) / (2 * L))  # радианы
    f_2 = numpy.arctan((delta_x_2) / (2 * L))  # радианы
    logger.info(f"\nРасчет углов:\n"
                f"Угол f_1: {f_1} радиан\n"
                f"Угол f_2: {f_2} радиан")

    # ТАНГЕНСЫ И СИНУСЫ УГЛОВ
    f_1_tan = numpy.tan(f_1)
    f_2_tan = numpy.tan(f_2)
    f_1_sin = numpy.sin(f_1)
    f_2_sin = numpy.sin(f_2)
    logger.info(f"\nТангенсы и синусы углов:\n"
                f"\n"
                f"Тангес угла между 1-м максимумом: {f_1_tan} радиан\n"
                f"Тангес угла между 2-м максимумом: {f_2_tan} радиан\n"
                f"\n"
                f"Синус угла между 1-м максимумом: {f_1_sin} радиан\n"
                f"Синус угла между 2-м максимумом: {f_2_sin} радиан\n")

    # РАСЧЕТ ДЛИНЫ ВОЛНЫ
    lamda_1 = numpy.divide(numpy.dot(d, f_1_sin), n_1)  # divide - деление, dot - скалярное произведение
    lamda_2 = numpy.divide(numpy.dot(d, f_2_sin), n_2)

    logger.info(f"\nИзмерение длины волны:\n"
                f"Длина волны при измерении по 1-м максимумам: {numpy.format_float_scientific(lamda_1, precision=5)}\n"
                f"Длина волны при измерении по 2-м максимумам: {numpy.format_float_scientific(lamda_2, precision=5)}")

    # РАСЧЕТ СРЕДНЕГО ЗНАЧЕНИЯ ДЛИНЫ ВОЛНЫ
    sred_lamda = numpy.mean([lamda_1, lamda_2])
    logger.info(f"\nСрднее значение длины волны: {numpy.format_float_scientific(sred_lamda, precision=5)}")

    # РАСЧЕТ СРЕДНЕЙ АБСОЛЮТНОЙ ОШИБКИ
    otklon_lamda_1 = numpy.absolute(sred_lamda - lamda_1)
    otklon_lamda_2 = numpy.absolute(sred_lamda - lamda_2)
    sred_otklon = numpy.mean([otklon_lamda_1, otklon_lamda_2])
    logger.info(f"\nОтклонение значений от среднего: \n"
                f"Для первого измерения: {numpy.format_float_scientific(otklon_lamda_1, precision=5)}\n"
                f"Для второго значения: {numpy.format_float_scientific(otklon_lamda_2, precision=5)}\n"
                f"Средняя абсолютная ошибка: {numpy.format_float_scientific(sred_otklon, precision=5)}")


if __name__ == '__main__':
    rascheti()
