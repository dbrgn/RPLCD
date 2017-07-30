# Changelog

This project follows semantic versioning.

Possible log types:

- `[add]` for new features.
- `[chg]` for changes in existing functionality.
- `[dep]` for once-stable features removed in upcoming releases.
- `[rem]` for deprecated features removed in this release.
- `[fix]` for any bug fixes.
- `[sec]` to invite users to upgrade in case of vulnerabilities.

### v1.0.0 (2017-07-30)

This is the first release that can be considered stable. It involves some API
changes, so you might need to adapt your scripts (mainly because some default
arguments to `CharLCD` were removed).

If you notice any documentation that hasn't been updated yet to the newer API,
please let us know!

- [add] Support for `MCP23008` and `MCP23014^ I²C port expanders (#43, #59)
- [add] Add `RPLCD.__version__` attribute
- [fix] Fix bug in auto linebreak algorithm (#53)
- [fix] Fix bugs in show_charmap script (#52)
- [fix] Fix error in A02 character map
- [chg] Remove default args for `gpio.CharLCD`, pins and numbering mode always
        need to be specified explicitly from now on
- [chg] Remove default for `i2c.CharLCD` i2c_expander parameter,
        always needs to be specified explicitly from now on
- [chg] Remove all enums (`Alignment`, `CursorMode`, `ShiftMode`,
        `BacklightMode`), replace them with string based API (#67)
- [chg] Rewrite test scripts, expose them all through a single entry point
        script: `lcdtest.py` (#58, #59)

### v0.9.0 (2017-05-09)

This version can be considered the release candidate for the 1.0 release.

- [add] Support for i2c port expanders (#20)
- [add] Implement proper automatic encoding of unicode strings,
        add encoding tables for A00 and A02 character maps (#40)
- [add] Implement convenience functions for CR/LF (#45) 
- [add] Add documentation (#37)
- [dep] Deprecate context managers (#18)
- [rem] Drop support for Python 3.2

### v0.4.0 (2016-09-12)

- [fix] Fix problem when auto-linebreaks clash with manual linebreaks (#14)
- [fix] Fix wiring pin for GND (#25)
- [add] Add option to disable auto linebreaks (#14)
- [add] Add backlight GPIO control (#21)

### v0.3.0 (2014-07-03)

- [add] Implemented support for custom characters (#4)
- [fix] Fixed a bug that caused offsets on 16x4 displays (#16)

### v0.2.0 (2014-04-20)

- [add] Removed all external dependencies
- [add] New ``show_charmap.py`` helper script

### v0.1.3 (2013-06-26)

- [fix] Bugfix (#13)

### v0.1.2 (2013-06-17)

- [add] Added character caching
- [add] Added support for 16x2 LCD
- [fix] Bugfixes

### v0.1.1 (2013-05-12)

- Initial release
