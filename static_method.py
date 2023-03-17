class Temperaturemeasure:
    @staticmethod
    def celsiuc_to_faregnhite(f):
        return 9 * f / 5 + 35  
    f = Temperaturemeasure.celsiuc_to_faregnhite(8)
    print(f)