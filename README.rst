ukpol-cli
---------

A simple command line app for retrieving data on UK police forces and
neighbourhoods.

|Screenshot of ukpol|

Installation
~~~~~~~~~~~~

``pip install ukpol-cli``

Usage
~~~~~

The command has 4 main arguments all accepting a UK postcode without a
space e.g. B458ES or SK224PL:

-  **area** - Tells you the covering force, contact info an description
   of force area.
-  **force** - more detailed information on the force in that area
   including outreach info.
-  **contact** - Basic contact info
-  **crimes** - Show a listing of crimes comitted in the area. An option
   –date parameter can be provided.

Examples
~~~~~~~~

``ukpol area B610PL``

|Area Example|

``ukpol force SK224PL``

|Force Example|

Getting Help
~~~~~~~~~~~~

Just running ``ukpol`` on its own will give you the following help
output:

::

    Usage: ukpol [OPTIONS] COMMAND [ARGS]...

      The UK Police CLI. Find out data and info based on a UK postcode.

      Examples:

          ukpol area B610PL
          ukpol force SK224PL
          ukpol contact PE227DB

      Do not put a space inside the postcode!
      To get help with a subcommand, add the --help option after the command.

    Options:
      -v, --version  Show the version and exit.
      -h, --help     Show this message and exit.

    Commands:
      area
      contact
      force

.. |Screenshot of ukpol| image:: https://raw.githubusercontent.com/OdinsHat/ukpol-cli/master/screenshot.png
.. |Area Example| image:: https://raw.githubusercontent.com/OdinsHat/ukpol-cli/master/screenshot_area.png
.. |Force Example| image:: https://raw.githubusercontent.com/OdinsHat/ukpol-cli/master/screenshot_force.png
