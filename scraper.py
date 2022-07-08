from requests import Session
from bs4 import BeautifulSoup


class Scraper:
    ## URL strings
    url = (url := {"base": "https://registrar.cvsu.edu.ph"}) | {
        "info": f"{url['base']}/parts/dtsubject.php",
        ## TODO: Use proper URL encoding? `urllib.parse`
        # "sched": f"{url['base']}/studentlist.php?schedcode=",
    }

    ## `requests` session
    sesh = Session()

    ## Result parameters
    ## TODO: Set these as properties?
    ## TODO: Make class instantiable? (i.e. remove `@classmethod` decors and set `cls` to `self`)
    page = 1
    length = 20
    keyword = ""

    page_min = 1
    page_increments = 1

    @classmethod
    def set_next_page(cls) -> bool:
        cls.page += cls.page_increments

        return True

    @classmethod
    def set_previous_page(cls) -> bool:
        if cls.page == cls.page_min:
            return False

        cls.page -= cls.page_increments
        return True

    @classmethod
    def get_start_effective(cls) -> int:
        return cls.length * (cls.page - 1)

    @classmethod
    def get_response(cls) -> object:
        start, length, keyword = [
            str(_) for _ in (cls.get_start_effective(), cls.length, cls.keyword)
        ]

        data = {
            "start": start,
            "length": length,
            "search[value]": keyword,
        }

        response = cls.sesh.post(
            cls.url["info"],
            data=data,
        )

        return response

    @staticmethod
    def get_element_text(element_string) -> object:
        return BeautifulSoup(element_string, "html.parser").get_text()

    @classmethod
    def initialize_connection(cls) -> None:
        cls.sesh.get(cls.url["base"])

    @classmethod
    def renew_session(cls) -> None:
        cls.sesh = Session()
        cls.initialize_connection()


## Perform a GET on the base URL
## Needed for record retrieval to work properly
## Initializes the cookies...?
Scraper.initialize_connection()


if __name__ == "__main__":
    res = Scraper.get_response()
    print(res)

    breakpoint()
