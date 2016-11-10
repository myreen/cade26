# Sources for the CADE-26 webpage

To make simple edits to the webpage at http://www.cade-26.info/ do
the following:

  1. edit the text files, i.e. the `.txt`-files, *do not edit the `.html` files directly*

  2. run `make` at the command-line, this generates the `.html` files

  3. check the look of the new content in your browser, e.g. on Mac OS run `open start.html` on the command-line; if there are errors, go back to step 1

  4. commit and push your version of the to github

  5. update the public version of the webpage by going to the update page -- contact Magnus if you have lost the URL

For more significant changes, edits may be required to `build.py` which
is intentionally very simple and I hope understandable.
