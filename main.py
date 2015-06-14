#!/usr/bin/python3

# Copyright (C) 2015 Pablo Piaggio.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

from rsslibrary import config

def main( argv ):
    # Create config object and load the file.
    try:
        feed_config = config.Config( config.CONFIG_FILE )
    except Exception as e:
        print( e, file=sys.stderr)
        return
    else:
        if hasattr( feed_config, "warnings"):
            print( feed_config.warnings, file=sys.stderr)

    #print( feed_config, end="" )

    #msg = feed_config.check_directories()
    #if msg != "":
        #print( msg, end="", file=sys.stderr)

    #try:
        #feed_config.create_directories()
    #except Exception as e:
        #print( e, file=sys.stderr)
        #return

    try:
        feed_config.check_feed_urls()
    except Exception as e:
        print( e, file=sys.stderr)
        return

    return

if __name__ == "__main__":
    main( sys.argv )
