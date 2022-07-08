from scraper import Scraper


class Callback:
    @staticmethod
    def _():
        ...

    @staticmethod
    def next_page():
        ...

    @staticmethod
    def previous_page():
        ...

    @staticmethod
    def change_result_ct():
        ...

    @staticmethod
    def set_search_keyword():
        ...

    @staticmethod
    def search_schedule_code():
        ...

    @staticmethod
    def refresh_session():
        ...

    @staticmethod
    def end_program():
        print("Thank you very much!")
        raise SystemExit

    @staticmethod
    def invalid():
        print("You have made an invalid selection!")
