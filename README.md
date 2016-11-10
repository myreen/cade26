# Sources for the CADE-26 webpage

To make simple edits to the webpage at http://www.cade-26.info/ do
the following:

  1. edit the text files, i.e. the `.txt`-files

  2. run `make` at the command-line to generate the `.html` files

  3. check the look of the new content in your browser, e.g. on Mac OS run `open start.html` on the command-line; if there are errors, go back to step 1

  4. `git commit` and `git push` your version to github

  5. update the public version of the webpage by going to the update page

For more significant changes, edits may be required to `build.py` which
is intentionally very simple and, I hope, understandable.
