import datetime
import random
import string


def generate_code():
    s = ""
    for i in range(5):
        s += random.choice(string.digits + string.ascii_uppercase + '-')
    return s




def generate_reg_number():
    literals = "аомклнве"
    return "{0}{1}{2}".format(random.choice(literals), random.randint(100, 999), ''.join(random.choices(literals, k=2)))


def generate_model():
    templateTable = f'insert into "Model" ("ModelId", "ModelTitle", "EngineVolume", "MaxSpeed", "DoorCount", "PlaceCount") values \n'
    templateValues = "(default, {0}, {1}, {2}, {3}, {4})"

    data = [[f"'Model {i}'", random.randint(1, 3) + random.randint(1, 9) / 10, random.randint(30, 350),
             4 if random.randint(1, 3) > 1 else 2, 5 if random.randint(1, 3) > 1 else 8] for i in range(1, 16)]
    return templateTable + ', \n'.join([templateValues.format(*d) for d in data])


def generate_car():
    templateTable = f'insert into "Car" ("CarId", "ModelId", "TransmissionNumber", "RegNumber", "BodyNumber", "EngineNumber", "ReleaseDate", "ColorId") values \n'
    templateValues = "(default, {0}, '{1}', '{2}', '{3}', '{4}', '{5}', {6})"

    data = [[random.randint(1, 12), generate_code(), generate_reg_number(), generate_code(), generate_code(),
             datetime.date(2000, 10, 5) + datetime.timedelta(days=random.randint(-1000, 1000)), random.randint(1, 5)]
            for i in range(1, 16)]

    return templateTable + ', \n'.join([templateValues.format(*d) for d in data])


def generate_employees():
    templateTable = f'insert into "Employees" ("EmployeeId", "LastName", "Name", "Patronymic", "Birthday", "Phone") values  \n'
    templateValues = "(default, '{0}', '{1}', '{2}', '{3}', '{4}')"
    names = ["Иван", "Сергей", "Алексей", "Михаил"]
    lastnames = ["Иванов", "Сергеев", "Алексеев", "Михайлов"]
    patronymics = ["Иванович", "Сергеевич", "Алексеевич", "Михайлович"]

    data = [[random.choice(names), random.choice(lastnames), random.choice(patronymics),
             datetime.date(1990, 10, 5) + datetime.timedelta(days=random.randint(-5000, 5000)),
             "+79" + str(random.randint(123456789, 999999999))]
            for i in range(1, 16)]

    return templateTable + ', \n'.join([templateValues.format(*d) for d in data])


def generate_customers():
    templateTable = f'insert into "Customer" ("CustomerId", "LastName", "Name", "Patronymic", "CustomerTitle", "PassportData", "PhoneNumber") values  \n'
    templateValues = "(default, '{0}', '{1}', '{2}', '{3}', {4}, '{5}')"
    names = ["Иван", "Сергей", "Алексей", "Михаил"]
    lastnames = ["Иванов", "Сергеев", "Алексеев", "Михайлов"]
    patronymics = ["Иванович", "Сергеевич", "Алексеевич", "Михайлович"]

    companies = ["", "", "ООО Канарейка", "ООО Компания", "ООО БД"]

    data = []
    for i in range(1, 16):
        data.append(
            [random.choice(names), random.choice(lastnames), random.choice(patronymics), random.choice(companies),
             random.randint(1000000001, 9999999999), "+79" + str(random.randint(123456789, 999999999))])

    return templateTable + ', \n'.join([templateValues.format(*d) for d in data])


def generate_additional_services():
    templateTable = f'insert into "AdditionalServices" ("ServiceId", "Title", "PricePerDay") values  \n'
    templateValues = "(default, '{0}', {1})"
    titles1 = ["Очистка", "Улучшение", "Полировка"]
    titles2 = ["Окон", "Кресел", "Руля"]

    data = []
    for i in range(1, 16):
        data.append(
            [f"{random.choice(titles1)} {random.choice(titles2)}", random.randint(1000, 10000)])

    return templateTable + ', \n'.join([templateValues.format(*d) for d in data])


def generate_color():
    templateTable = f'insert into "Color" ("ColorId", "ColorTitle") values  \n'
    templateValues = "(default, '{0}')"
    colors = ["Зеленый", "Красный", "Синий", "Желтый", "Лиловый", "Сербурмалиновый", "Фиолетовый", "Изумрудный",
              "Черный", "Белый"]

    data = []
    for i in range(1, 10):
        data.append([colors[i]])
    return templateTable + ', \n'.join([templateValues.format(*d) for d in data])


def generate_contracts():
    templateTable = f'insert into "Contract" ("ContractNumber", "CustomerId", "EmployeeId", "CarId", "BeginDate", "DayCount", "ServiceId", "Cost") values  \n'
    templateValues = "(default, {0}, {1}, {2}, '{3}', {4}, {5}, {6})"

    data = []
    for i in range(1, 16):
        data.append([random.randint(1, 15), random.randint(1, 15), random.randint(1, 15),
                     datetime.date(2023, 4, 1) + datetime.timedelta(days=random.randint(-10, 20)),
                     random.randint(1, 30), random.randint(1, 15), random.randint(1000, 50000)])
    return templateTable + ', \n'.join([templateValues.format(*d) for d in data])

print("-- Заполняем таблицу Models\n", generate_model(), ';\n')
print("-- Заполняем таблицу Color\n", generate_color(), ';\n')
print("-- Заполняем таблицу Car\n", generate_car(), ';\n')
print("-- Заполняем таблицу Employees\n", generate_employees(), ';\n')
print("-- Заполняем таблицу Customer\n", generate_customers(), ';\n')
print("-- Заполняем таблицу AdditionalServices\n", generate_additional_services(), ';\n')
print("-- Заполняем таблицу Contracts \n", generate_contracts(), ';\n')
