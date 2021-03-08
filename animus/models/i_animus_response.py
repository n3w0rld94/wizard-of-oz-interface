from typing import TypedDict


class Animus_Response: 
    """#### Interface for Animus proto Error class
        #### Attributes:
            `success (bool)`: The outcome of the operation. True if it succeeded.
            `code (int)`: The code of the response.
            `description (str)`: The description of the outcome (or error message if failed)
    """
    success: bool
    code: int
    description: str


class Animus_Robot_Search_Response:
    """#### Interface to the Animus robots search results
        ##### Attributes:
            `robots (list)`: List of discovered robots
            `localSearchError (Animus_Response)`: The outcome of the search on the local network
            `remoteSearchError (Animus_Response)`: The outcome of the remote search
    """
    robots: list
    localSearchError: Animus_Response
    remoteSearchError: Animus_Response