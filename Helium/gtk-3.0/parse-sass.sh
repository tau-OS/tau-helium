#! /bin/bash

if [ ! "$(which sass 2> /dev/null)" ]; then
   echo sass needs to be installed to generate the css.
   exit 1
fi

SASS_OPT="--no-source-map -s compressed"

echo Generating the css...

sass $SASS_OPT gtk.scss gtk.css
sass $SASS_OPT gtk-dark.scss gtk-dark.css
