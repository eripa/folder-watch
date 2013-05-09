# folder watch

## Description

simple script to watch for changes in a given folder, with OS X error reporting and emailing functionality

## How to use

Simply run with a folder as the first and only argument.
    
    watch.py <folder>

Preferably setup in crontab, something like this to check your iPhoto Masters each night at 20:00:

    ## Run script to watch for removed files in iPhoto library
    00 20   *   *   *   ~/Library/folder-watch/watch.py ~/Photos/iPhoto\ Library/Masters &> /dev/null || osascript ~/Library/folder-watch/osx_error.scpt "watch.py" &> /dev/null

## To be done

  * Add intelligence to track if the file is moved and not actually removed.
  * Add some more options to define to, from and maybe password on the command line instead of in the script (i.e. add argparse)

## License

This script is delivered "as is" and is [unlicensed](http://unlicense.org).

    This is free and unencumbered software released into the public domain.

    Anyone is free to copy, modify, publish, use, compile, sell, or
    distribute this software, either in source code form or as a compiled
    binary, for any purpose, commercial or non-commercial, and by any
    means.

    In jurisdictions that recognize copyright laws, the author or authors
    of this software dedicate any and all copyright interest in the
    software to the public domain. We make this dedication for the benefit
    of the public at large and to the detriment of our heirs and
    successors. We intend this dedication to be an overt act of
    relinquishment in perpetuity of all present and future rights to this
    software under copyright law.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
    OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
    ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE.

    For more information, please refer to <http://unlicense.org/>
