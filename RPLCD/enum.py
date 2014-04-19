# Copyright (C) 2004-2013 by Barry A. Warsaw
#
# This file is part of flufl.enum
#
# flufl.enum is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, version 3 of the License.
#
# flufl.enum is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with flufl.enum.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Barry Warsaw <barry@python.org>

"""Python enumerations."""

from __future__ import absolute_import, print_function, unicode_literals

import re
import sys
import warnings

from operator import itemgetter

COMMASPACE = ', '
SPACE = ' '
IDENTIFIER_RE = r'^[a-zA-Z_][a-zA-Z0-9_]*$'


class EnumMetaclass(type):
    """Meta class for Enums."""

    def __init__(cls, name, bases, attributes):
        """Create an Enum class.

        :param cls: The class being defined.
        :param name: The name of the class.
        :param bases: The class's base classes.
        :param attributes: The class attributes.
        """
        super(EnumMetaclass, cls).__init__(name, bases, attributes)
        # Store EnumValues here for easy access.
        cls._enums = {}
        # Figure out if this class has a custom factory for building enum
        # values.  The default is EnumValue, but the class (or one of its
        # bases) can declare a custom one with a special attribute.
        factory = attributes.get('__value_factory__')
        # Figure out the set of enum values on the base classes, to ensure
        # that we don't get any duplicate values.  At the same time, check the
        # base classes for the special attribute.
        for basecls in cls.__mro__:
            if hasattr(basecls, '_enums'):
                cls._enums.update(basecls._enums)
            if hasattr(basecls, '__value_factory__'):
                basecls_factory = basecls.__value_factory__
                if factory is not None and basecls_factory != factory:
                    raise TypeError(
                        'Conflicting enum factory in base class: {}'.format(
                            basecls_factory))
                factory = basecls_factory
        # Set the factory default if necessary.
        if factory is None:
            factory = EnumValue
        # For each class attribute, create an enum value and store that back
        # on the class instead of the original value.  Skip Python reserved
        # names.  Also add a mapping from the original value to the enum value
        # instance so we can return the same object on conversion.
        for attr in attributes:
            if not (attr.startswith('__') and attr.endswith('__')):
                value = attributes[attr]
                enumval = factory(cls, value, attr)
                if value in cls._enums:
                    other = cls._enums[value]
                    # Without this, sort order is undefined and causes
                    # unpredictable results for the test suite.
                    first = (attr if attr < other else other)
                    second = (other if attr < other else attr)
                    raise ValueError("Conflicting enum value '{}' "
                                     "for names: '{}' and '{}'".format(
                                         value, first, second))
                # Store as an attribute on the class, and save the attr name.
                setattr(cls, attr, enumval)
                cls._enums[value] = attr

    def __dir__(cls):
        # For Python 3.2, we must explicitly convert the dict view to a list.
        # Order is not guaranteed, so don't sort it.
        return list(cls._enums.values())

    def __repr__(cls):
        # We want predictable reprs.  Because base Enum items can have any
        # value, the only reliable way to sort the keys for the repr is based
        # on the attribute name, which must be Python identifiers.
        return '<{0} {{{1}}}>'.format(cls.__name__, COMMASPACE.join(
            '{0}: {1}'.format(value, key)
            for key, value in sorted(cls._enums.items(), key=itemgetter(1))))

    def __iter__(cls):
        for value in sorted(cls._enums.values()):
            yield getattr(cls, value)

    def __getitem__(cls, item):
        attr = cls._enums.get(item)
        if attr is None:
            # If this is an EnumValue, try it's .value attribute.
            if hasattr(item, 'value'):
                attr = cls._enums.get(item.value)
            if attr is None:
                # It wasn't value-ish -- try the attribute name.  This was
                # deprecated in LP: #1167091.
                try:
                    warnings.warn('Enum[item_name] is deprecated; '
                                  'use getattr(Enum, item_name)',
                                  DeprecationWarning, 2)
                    return getattr(cls, item)
                except (AttributeError, TypeError):
                    raise ValueError(item)
        return getattr(cls, attr)

    def __call__(cls, *args):
        # One-argument calling is a deprecated synonym for getitem.
        if len(args) == 1:
            warnings.warn('MyEnum(arg) is deprecated; use MyEnum[arg]',
                          DeprecationWarning, 2)
            return cls.__getitem__(args[0])
        name, source = args
        return _make(cls, name, source)


class EnumValue:
    """Class to represent an enumeration value.

    EnumValue('Color', 'red', 12) prints as 'Color.red' and can be converted
    to the integer 12.
    """
    def __init__(self, enum, value, name):
        self._enum = enum
        self._value = value
        self._name = name

    def __repr__(self):
        return '<EnumValue: {0}.{1} [value={2}]>'.format(
            self._enum.__name__, self._name, self._value)

    def __str__(self):
        return '{0}.{1}'.format(self._enum.__name__, self._name)

    def __int__(self):
        warnings.warn('int() is deprecated; use IntEnums',
                      DeprecationWarning, 2)
        return self._value

    def __reduce__(self):
        return getattr, (self._enum, self._name)

    @property
    def enum(self):
        """Return the class associated with the enum value."""
        return self._enum

    @property
    def name(self):
        """Return the name of the enum value."""
        return self._name

    @property
    def value(self):
        """Return the underlying value."""
        return self._value

    # Support only comparison by identity and equality.  Ordered comparisions
    # are not supported.
    def __eq__(self, other):
        return self is other

    def __ne__(self, other):
        return self is not other

    def __lt__(self, other):
        # In Python 3, returning NotImplemented from an ordered comparison
        # operator will cause a TypeError to be raised.  This doesn't work in
        # Python 2 though, and you'd end up with working, but incorrect,
        # ordered comparisons.  In Python 2 we raise the TypeError explicitly.
        if sys.version_info[0] < 3:
            raise TypeError(
                'unorderable types: {}() < {}()'.format(
                    self.__class__.__name__, other.__class__.__name__))
        return NotImplemented

    def __gt__(self, other):
        if sys.version_info[0] < 3:
            raise TypeError(
                'unorderable types: {}() > {}()'.format(
                    self.__class__.__name__, other.__class__.__name__))
        return NotImplemented

    def __le__(self, other):
        if sys.version_info[0] < 3:
            raise TypeError(
                'unorderable types: {}() <= {}()'.format(
                    self.__class__.__name__, other.__class__.__name__))
        return NotImplemented

    def __ge__(self, other):
        if sys.version_info[0] < 3:
            raise TypeError(
                'unorderable types: {}() >= {}()'.format(
                    self.__class__.__name__, other.__class__.__name__))
        return NotImplemented

    __hash__ = object.__hash__


# Define the Enum class using metaclass syntax compatible with both Python 2
# and Python 3.
Enum = EnumMetaclass(str('Enum'), (), {
    '__doc__': 'The public API Enum class.',
    })


class IntEnumValue(int, EnumValue):
    """An EnumValue that is also an integer."""

    def __new__(cls, enum, value, attr):
        return super(IntEnumValue, cls).__new__(cls, value)

    __repr__ = EnumValue.__repr__
    __str__ = EnumValue.__str__

    # For Python 2 (Python 3 doesn't need this to work).
    __eq__ = int.__eq__
    __ne__ = int.__ne__
    __le__ = int.__le__
    __lt__ = int.__lt__
    __gt__ = int.__gt__
    __ge__ = int.__ge__

    # The non-deprecated version of this method.
    def __int__(self):
        return self._value

    # For slices and index().
    __index__ = __int__


class IntEnumMetaclass(EnumMetaclass):
    # Define an iteration over the integer values instead of the attribute
    # names.
    def __iter__(cls):
        for key in sorted(cls._enums):
            yield getattr(cls, cls._enums[key])


IntEnum = IntEnumMetaclass(str('IntEnum'), (Enum,), {
    '__doc__': 'A specialized enumeration with values that are also integers.',
    '__value_factory__': IntEnumValue,
    })


if str is bytes:
    # Python 2
    STRING_TYPE = basestring
else:
    # Python 3
    STRING_TYPE = str


def _swap(sequence):
    for key, value in sequence:
        yield value, key


def _make(enum_class, name, source):
    """The common implementation for `Enum()` and `IntEnum()`."""
    namespace = {}
    illegals = []
    have_strings = None
    # Auto-splitting of strings.
    if isinstance(source, STRING_TYPE):
        source = source.split()
    # Look for dict-like arguments.  Specifically, it must have a callable
    # .items() attribute.  Because of the way enumerate() works, here we have
    # to swap the key/values.
    try:
        source = _swap(source.items())
    except (TypeError, AttributeError):
        source = enumerate(source, start=1)
    for i, item in source:
        if isinstance(item, STRING_TYPE):
            if have_strings is None:
                have_strings = True
            elif not have_strings:
                raise ValueError('heterogeneous source')
            namespace[item] = i
            if re.match(IDENTIFIER_RE, item) is None:
                illegals.append(item)
        else:
            if have_strings is None:
                have_strings = False
            elif have_strings:
                raise ValueError('heterogeneous source')
            item_name, item_value = item
            namespace[item_name] = item_value
            if re.match(IDENTIFIER_RE, item_name) is None:
                illegals.append(item_name)
    if len(illegals) > 0:
        raise ValueError('non-identifiers: {0}'.format(SPACE.join(illegals)))
    return EnumMetaclass(str(name), (enum_class,), namespace)
