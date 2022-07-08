from scraper import Scraper


class Callback:
    @staticmethod
    def next_page(increment: int = 1):
        previous = Scraper.page
        is_success = Scraper.set_next_page()
        current = Scraper.page

        if is_success:
            msg = f"Page changed from {previous} to {Scraper.page}."
        else:
            msg = f"Page change unsuccessful. [{previous=} {current=}]"
        print(msg)

    @staticmethod
    def previous_page(decrement: int = 1):
        previous = Scraper.page
        is_success = Scraper.set_previous_page()
        current = Scraper.page

        if is_success:
            msg = f"Page changed from {previous} to {Scraper.page}."
        else:
            msg = f"Page change unsuccessful. [{previous=} {current=}]"
        print(msg)

    @staticmethod
    def change_result_ct(prompt: str = "Enter number of rows desired: "):
        user_input = input(prompt)

        if user_input.isdigit():
            previous = Scraper.length
            Scraper.length = int(user_input)
            Scraper.page = Scraper.page_min

            msg = (
                f"Row display count changed from {previous} to {Scraper.length}.",
                f"Page number reset to {Scraper.page}.",
            )
            msg = "\n".join(msg)
        else:
            msg = f"Your input is invalid. Please try again. [Received: `{repr(user_input)}`]"
        print(msg)

    @staticmethod
    def set_search_keyword(prompt: str = "Enter keyword(s) to search for: "):
        user_input = input(prompt)

        Scraper.keyword = user_input
        Scraper.page = Scraper.page_min

        msg = (
            f"Search keyword set to {user_input!r}.",
            f"Page number reset to {Scraper.page}.",
        )
        msg = "\n".join(msg)
        print(msg)

    """
    @staticmethod
    def search_schedule_code():
        ...
    """

    @staticmethod
    def refresh_session():
        Scraper.renew_session()
        Scraper.page = Scraper.page_min

        msg = [
            "A new scraper session has been created.",
            f"Page number reset to {Scraper.page}.",
        ]
        msg = "\n".join(msg)
        print(msg)

    @staticmethod
    def end_program():
        print("Thank you very much!")
        raise SystemExit

    @staticmethod
    def invalid():
        print("You have made an invalid selection!")
