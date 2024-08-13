# waddiff

Show which lumps differ between two Doom WAD files.

Requires [omgifol](https://github.com/devinacker/omgifol/).

Run `pip install omgifol` before using.

Usage:

`waddiff.py a.wad b.wad`

Prints what differs between the two.

If nothing differs, nothing is printed.

Return code 0 means no differences found.
Return code 1 means differences found.

