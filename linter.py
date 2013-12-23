#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by William Meldon
# Copyright (c) 2013 William Meldon
#
# License: MIT

"""This module exports the Apiblueprint plugin class."""

from SublimeLinter.lint import Linter, util


class Apiblueprint(Linter):

    """Provides an interface to apiblueprint."""

    syntax = 'apiblueprint'
    cmd = 'snowcrash -v'
    executable = 'snowcrash'
    executable = None
    regex = (
        r'(?:(?P<warning>warning)|(?P<error>error)):\s*\((?P<code>\d+)\)'
        r'(?P<message>.+?)(?::|$)'
        r'(?P<pos>\d+):(?P<upto>\d+)(?:.*)'
    )
    multiline = False
    line_col_base = (0, 0)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None

    def find_errors(self, output):
        """
        A generator which matches the linter's regex against the linter output.

        If multiline is True, split_match is called for each non-overlapping
        match of self.regex. If False, split_match is called for each line
        in output.

        """

        if self.multiline:
            errors = self.regex.finditer(output)

            if errors:
                for error in errors:
                    yield self.split_match(error)
            else:
                yield self.split_match(None)
        else:
            for line in output.splitlines():
                yield self.split_match(self.regex.match(line.rstrip()))

    def split_match(self, match):
        """
        Split a match into the standard elements of an error and return them.

        If subclasses need to modify the values returned by the regex, they
        should override this method, call super(), then modify the values
        and return them.

        """
        
        if match:
            items = {'pos': None, 'upto': None, 'error': None, 'warning': None, 'message': '', 'near': None}
            items.update(match.groupdict())
            pos, upto, error, warning, message, near = [
                items[k] for k in ('pos', 'upto', 'error', 'warning', 'message', 'near')
            ]
            line, col = self.view.rowcol((int(pos)))

            if line is not None:
                line = int(line) - self.line_col_base[0]

            if col is not None:
                col = int(col) - self.line_col_base[1]

            return match, line, col, error, warning, message, near
        else:
            return match, None, None, None, None, '', None
