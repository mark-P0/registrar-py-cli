class Callback:
    @staticmethod
    def _():
        ...

    @staticmethod
    def end_program():
        print("Thank you very much!")
        raise SystemExit

    @staticmethod
    def invalid():
        print("You have made an invalid selection!")
