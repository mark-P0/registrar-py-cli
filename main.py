from cli import CLI


def main() -> None:
    while True:
        CLI.show_data()
        print()
        CLI.show_menu()

        selection = CLI.get_input()
        print()

        CLI.activate_behavior(selection)
        print()

        CLI.prompt_continue()
        print()


if __name__ == "__main__":
    main()
