# Logging Means - Capture details, Which are useful while debugging
# and show the user details about execution of program.

# Warning to the users
# Information to the users
# Errors, Critical Errors user.

import logging

def test_print_logs():
    LOGGER = logging.getLogger(__name__)

    # Intentional logging to user
    LOGGER.info("This is the information")
    LOGGER.warning("this is Warning Logs")
    LOGGER.error("This is Error Logs")
    LOGGER.critical("This is Critical Logs")
