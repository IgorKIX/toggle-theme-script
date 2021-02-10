# toggle-theme-script

Simple python script to toggle theme in vim & fish prompt theme

### How to use:

`PATH_VIM` & `PARTH_PROMPT` are the paths to your theme config files
`LIGHT_VIM DARK_VIM LIGHT_PROMPT DARK_PROMPT` are the names of themes that you want to toggle.
`COMMENT_VIM COMMMENT_PROMPT` are the variables for adequate comment signe for the file

You can also set the time when dark & light theme will be enabled. To do this look into `check_day_time_to_set_theme` method and in replace function change the houre, minute, etc...

Change this variables to suit your system configuration and run the script by `python toggleTheme.py`.
Ofc you have to be in the same dir ;)
