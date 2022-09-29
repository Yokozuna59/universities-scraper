from typing import List

BANNER_DOMAIN = "https://banner9-registration.kfupm.edu.sa"

banner_url = BANNER_DOMAIN + "/StudentRegistrationSsb/ssb/registration"
registration_status = (
    BANNER_DOMAIN + "/StudentRegistrationSsb/ssb/term/termSelection?mode=preReg"
)
registration_courses = (
    BANNER_DOMAIN
    + "/StudentRegistrationSsb/ssb/registration/registerPostSignIn?mode=registration"
)
term_schedules = (
    BANNER_DOMAIN
    + "/StudentRegistrationSsb/ssb/registrationHistory/registrationHistory"
)
search_courses = (
    BANNER_DOMAIN + "/StudentRegistrationSsb/ssb/term/termSelection?mode=search"
)
courses_catalog = (
    BANNER_DOMAIN + "/StudentRegistrationSsb/ssb/term/termSelection?mode=courseSearch"
)

urls = [
    registration_status,
    registration_courses,
    term_schedules,
    search_courses,
    courses_catalog,
]


class Banner9Course:
    def __init__(self) -> None:
        pass

    def to_dict(self) -> dict:
        pass


class Banner9Term:
    def __init__(self, term_code, description) -> None:
        self.__term_code = term_code
        self.__term_short_code = term_code[2:5]
        self.__description = description
        self.__courses = []  # type: List[dict]

    def get_term_code(self) -> str:
        return self.__term_code

    def get_term_description(self) -> str:
        return self.__description

    def add_course(self, course: Banner9Course) -> None:
        self.__courses.append(course.to_dict())

    def to_dict(self) -> dict:
        dictionary = {
            "termCode": self.__term_code,
            "termShortCode": self.__term_short_code,
            "description": self.__description,
            "courses": self.__courses,
        }
        return dictionary
