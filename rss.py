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

import re
import curses
import feedparser
import os
import json
import sys

# Global variables
CONFIG_FILE  = "/home/pablo/etc/rss/config.conf" # List of RSS feeds and working directories.
feed_file    = "feed_file"                       # File where to store content of feed (JSON format).
watched_file = "marked_as_watched"

#
# Config class. Manages the config file.
#
class Config:

    def __init__( self, filename ):
        # Check if file exists.
        if not os.path.isfile( filename ):
            print( "(EE) Config file doesn't exist, or there's not access to it:", filename, file=sys.stderr  )
            raise ValueError

        self.filename = filename
        try:
            config_fp = open( self.filename, "r" )
        except:
            print( "(EE) Can't open config file:", self.filename, file=sys.stderr  )
            raise ValueError

        config = []

        # Load contents of config file.
        # Format:
        # feedname url directory
        line_number = 0
        for line in config_fp:
            line_number += 1

            # Parse line, get fields between spaces.
            split_line = re.split( '\s+', line )

            # Skiping blank lines and comments.
            if not split_line[0] or split_line[0][0] == "#":
                continue

            # Length=4 means 3 fields so it is a well formated line.
            if len( split_line ) == 4:
                feed_name = split_line[0]
                feed_url  = split_line[1]
                feed_dir  = split_line[2]
                entry     = {'name' : feed_name, 'url' : feed_url, 'dir' : feed_dir}
                config.append( entry )
            else:
                print("(WW) Config file, ignoring line#", line_number, ": ", line, sep="", end="", file=sys.stderr )

        config_fp.close()
        self.list = config
        return

    # For print method.
    def __str__( self ):
        output = "Filename:\n" + "    " + self.filename + "\n"

        output += "Feeds:\n"
        for feed in self.list:
            output += "    " + feed['name'] + "\n"
            output += "        url: " + feed['url'] + "\n"
            output += "        directory: " + feed['dir'] + "\n"
    
        return output

def main( argv ):
    # Create config object and load the file.
    try:
        feed_config = Config( CONFIG_FILE )
    except:
        return

    print( feed_config, end="" )
    return

if __name__ == "__main__":
    main( sys.argv )
