from callback import Callback


class CLI:
    menu_items_raw = (
        "Next page",
        "Previous page",
        "Change number of displayed rows",
        "Search for a keyword",
        "Search for a schedule code",
        "Refresh cookies",
        "End program",
    )
    menu_item_wrappers = ("[", "]")

    input_prompt = "Please make a selection: "
    input_prompt_continue = "Press Enter to continue. . ."
    input_callbacks = {
        "0": Callback.end_program,
        "1": Callback._,
        "2": Callback._,
        "3": Callback._,
        "4": Callback._,
        "5": Callback._,
        "6": Callback._,
    }

    @classmethod
    def show_menu(cls) -> None:
        items = cls.menu_items_raw
        wrappers = cls.menu_item_wrappers
        start, stop = wrappers

        ## Add item numbers
        items = tuple(
            f"{start}{ct % len(items)}{stop} {item}"
            for ct, item in enumerate(items, start=1)
        )

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

        input(cls.input_prompt_continue)
