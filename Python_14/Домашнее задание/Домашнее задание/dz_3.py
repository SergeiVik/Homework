# Задача 4
class SystemTransformation:
    count = 0

    @staticmethod
    def transformation_kg(kg):
        SystemTransformation.count += 1
        return f"Футы {kg * 2.2}"

    @staticmethod
    def transformation_m(m):
        SystemTransformation.count += 1
        return f"Ярды {m * 1.09}"

    @staticmethod
    def transformation_sm(sm):
        SystemTransformation.count += 1
        return f"Дюймы {sm * 0.39}"

    @staticmethod
    def transformation_l(l):
        SystemTransformation.count += 1
        return f"Галлоны {l * 0.22}"

    @staticmethod
    def get_count_transformation():
        return SystemTransformation.count


print(SystemTransformation.transformation_m(100))
print(SystemTransformation.get_count_transformation())
