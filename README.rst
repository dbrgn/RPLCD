RPLCD
#####

A Python 2/3 Raspberry PI Character LCD library for the Hitachi HD44780
controller.

Tested with the 20x4 LCD that is sold for example by `adafruit.com
<http://www.adafruit.com/products/198>`_ or `mikroshop.ch
<http://mikroshop.ch/LED_LCD.html?gruppe=7&artikel=84>`_.

.. image:: https://raw.github.com/dbrgn/RPLCD/master/photo.jpg
    :alt: Photo of 20x4 LCD in action

This library is inspired by Adafruit Industries' CharLCD_ library as well as by
Arduino's LiquidCrystal_ library.

The GPIO access is provided by the great RPIO_ library.


Goals
=====

- Simple to use API
- Support for both 4 bit and 8 bit modes
- Python 2/3 compatible


Installing
==========

(**TLDR**: Use ``pip install RPLCD``)

Prerequisites
-------------

As prerequisite to build the RPIO_ dependency, you need the ``python-dev``
package. And to install the package itself, you'll want to use ``pip``. Both
should already be installed on a regular Raspbian image. Otherwise, install
them::

    $ sudo apt-get install python-dev python-pip

Virtualenv Installation
-----------------------

I would recommend you to always use virtualenv_ and virtualenvwrapper when
developing Python applications. This way, you have an isolated environment for
each project, which prevents package version conflicts.

To install virtualenv and virtualenvwrapper::

    $ sudo apt-get install virtualenvwrapper

Log out and back in to activate the virtualenvwrapper scripts. Then create a
new virtualenv::

    $ mkvirtualenv myproject

To enable the virtualenv, use ``workon myproject`` and to disable it use
``deactivate``.

Then install the RPLCD library with its dependencies::

    $ pip install RPLCD

Systemwide Installation
-----------------------

If you want you can also skip the virtualenv part and install the library
system-wide. In that case just run pip as root::

    $ sudo pip install RPLCD

Manual Installation
-------------------

You can also install the library manually without pip. Either just copy the
scripts to your working directory and import them, or download the repository
and run ``python setup.py install`` to install it into your Python package
directory.


Wiring
======

The standard wiring configuration uses the following pins (BOARD numbering
scheme):

- RS: 15
- RW: 18
- E: 16
- Data 4-7: 21, 22, 23, 24


API
===

Init, Setup, Teardown
---------------------

.. sourcecode:: python

    import RPIO
    from RPLCD import CharLCD

    # Initialize LCD
    lcd = CharLCD(pin_rs=15, pin_e=16, pins_data=[21, 22, 23, 24],
                  numbering_mode=RPIO.BOARD)
    lcd.setup(cols=20, rows=4, dotsize=8)

    # (...)

    lcd.close(clear=True)

Properties
----------

- ``display_enabled`` -> ``True`` / ``False``
- ``cursor_pos`` -> ``(row, col)``
- ``text_align_mode`` -> ``Alignment.left`` / ``Alignment.right``
- ``write_shift_mode`` -> ``ShiftMode.cursor`` / ``ShiftMode.display``
- ``cursor_mode`` -> ``CursorMode.hide`` / ``CursorMode.line`` / ``CursorMode.blink``

High Level Functions
--------------------

- ``write_string(value)``: Write the specified string to the display. You can
  use newline and carriage return characters.
- ``clear()``: Overwrite display with blank characters and reset cursor position.
- ``home()``: Set cursor to initial position and reset any shifting.
- ``shift_display(amount)``: Shift the display. Use negative amounts to shift
  left and positive amounts to shift right.

Mid Level Functions
-------------------

- ``write(value)``: Send a raw command to the LCD.
- ``command(value)``: Write a raw byte to the LCD.


Testing
=======

To test your display, please run the ``test.py`` script and confirm/verify each
step with the enter key. If you don't use the standard wiring, make sure to add
your pin numbers to the ``CharLCD`` constructor in ``test.py``.


Resources
=========

- TC2004A-01 Data Sheet: http://www.adafruit.com/datasheets/TC2004A-01.pdf
- HD44780U Data Sheet: http://www.adafruit.com/datasheets/HD44780.pdf


License
=======

This code is licensed under the MIT license, see the `LICENSE file
<https://github.com/dbrgn/RPLCD/blob/master/LICENSE>`_ or `tldrlegal
<http://www.tldrlegal.com/license/mit-license>`_ for more information. 


.. _rpio: https://github.com/metachris/RPIO
.. _charlcd: https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_CharLCD
.. _liquidcrystal: http://arduino.cc/en/Reference/LiquidCrystal
.. _virtualenv: http://blog.dbrgn.ch/2012/9/18/virtualenv-quickstart/
