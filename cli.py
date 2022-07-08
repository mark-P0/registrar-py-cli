from callback import Callback
from scraper import Scraper


class CLI:
    menu_title = "University Registrar".upper()
    menu_items_raw = (
        "Next page",
        "Previous page",
        "Change number of displayed rows",
        "Search for a keyword",
        "Search for a schedule code",
        "Refresh session",
        "End program",
    )
    menu_item_wrappers = ("[", "]")

    input_prompt = "Please make a selection: "
    input_prompt_continue = "Press Enter to continue. . ."
    input_callbacks = {
        "1": Callback.next_page,
        "2": Callback.previous_page,
        "3": Callback.change_result_ct,
        "4": Callback.set_search_keyword,
        "5": Callback.search_schedule_code,
        "6": Callback.refresh_session,
        "0": Callback.end_program,
    }

    table_headers = (
        "Subject Code",
        "Subject Title",
        "Schedule Code",
        "Section",
        "Avl. Slots",
    )
    table_col_max_len = 24
    table_col_alignment = ">"
    table_col_sep = " " * 2

    @classmethod
    def create_string_table(
        cls,
        data: list[list[str]],
    ) -> str:
        ## Get maximum string lengths per column
        ## Get either that or a specified maximum length
        max_strlens = [
            min(
                len(max(col, key=len)),
                cls.table_col_max_len,
            )
            for col in zip(*data)
        ]

        ## Construct a row string template using the derived max lengths
        ## Each column will have a placeholder like "{:>10.24}"
        ##     >  → alignment
        ##     10 → Allotted space
        ##     24 → Absolute maximum
        template_str_raw = (
            f"{{:{cls.table_col_alignment}{max_strlens[0]}.{cls.table_col_max_len}}}",
            f"{{:{cls.table_col_alignment}{max_strlens[1]}.{cls.table_col_max_len}}}",
            f"{{:{cls.table_col_alignment}{max_strlens[2]}.{cls.table_col_max_len}}}",
            f"{{:{cls.table_col_alignment}{max_strlens[3]}.{cls.table_col_max_len}}}",
            f"{{:{cls.table_col_alignment}{max_strlens[4]}.{cls.table_col_max_len}}}",
        )
        template_str = cls.table_col_sep.join(template_str_raw)

        ## Apply template to each row of the given data
        # fmt: off
        table = "\n".join(
            template_str.format(*row)
            for row in data
        )
        return table
        # fmt: on

    @classmethod
    def show_data(cls) -> None:
        try:
            response = Scraper.get_response()
            json = response.json()
            data = json["data"]
        ## TODO: Make this catch-all more specific?
        except Exception as error:
            msg = [
                "An error has occurred. The connection might be rejected.",
                "You could try again.",
                f"[{error}]",
            ]
            print(*msg, sep="\n")
            data = []

        ## Parse text from HTML data
        for idx, row in enumerate(data):
            data[idx][0] = Scraper.get_element_text(row[0])

        ## Add column headers to data
        data = [cls.table_headers] + data

        ## Construct table as result
        result = cls.create_string_table(data)
        print(result)

    @classmethod
    def show_menu(cls) -> None:
        items = cls.menu_items_raw
        wrappers = cls.menu_item_wrappers
        start, stop = wrappers

        ## Add item numbers
        items = [
            f"{start}{ct % len(items)}{stop} {item}"
            for ct, item in enumerate(items, start=1)
        ]

        ## Add additional menu items
        items = [
            cls.menu_title,
            f"Current page number    → {Scraper.page}",
            f"No. of displayed items → {Scraper.length}",
            f"Keyword searching for  → {Scraper.keyword!r}",
            "",
        ] + items

        print(*items, sep="\n")

    @classmethod
    def get_input(cls) -> str:
        return input(cls.input_prompt)

    @classmethod
    def activate_behavior(
        cls,
        selection: str,
    ) -> None:
        callback = cls.input_callbacks.get(selection, Callback.invalid)
        callback()

    @classmethod
    def prompt_continue(cls) -> None:
        input(cls.input_prompt_continue)
