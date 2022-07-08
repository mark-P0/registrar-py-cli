from cli import CLI


def main():
    while True:
        CLI.show_menu()

        selection = CLI.get_input()
        print()

        CLI.activate_behavior(selection)
        print()


if __name__ == "__main__":
    main()
