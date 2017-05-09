# Changelog

This project follows semantic versioning.

Possible log types:

- `[add]` for new features.
- `[chg]` for changes in existing functionality.
- `[dep]` for once-stable features removed in upcoming releases.
- `[rem]` for deprecated features removed in this release.
- `[fix]` for any bug fixes.
- `[sec]` to invite users to upgrade in case of vulnerabilities.

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
