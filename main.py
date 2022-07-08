class InputCallback:
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
        "0": InputCallback.end_program,
        "1": InputCallback._,
        "2": InputCallback._,
        "3": InputCallback._,
        "4": InputCallback._,
        "5": InputCallback._,
        "6": InputCallback._,
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
        callback = cls.input_callbacks.get(selection, InputCallback.invalid)
        callback()

        input(cls.input_prompt_continue)


def main():
    while True:
        CLI.show_menu()

        selection = CLI.get_input()
        print()

        CLI.activate_behavior(selection)
        print()


if __name__ == "__main__":
    main()
