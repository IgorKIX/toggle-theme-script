# Open _ & _ and toggle the theme to light/dark
import os
import sys
import datetime

# The default paths to proper files in which style will be changed
PATH_VIM = "PATH/TO/VIM/THEME/CONFIG/FILE"
PATH_PROMPT = "PATH/TO/PROMPT/THEME/CONFIG/FILE"
PATH_PREFIX = os.path.expanduser("~/.config/")

# Theme names
LIGHT_VIM = "VIM_LIGHT_THEME_NAME"
DARK_VIM = "VIM_DARK_THEME_NAME"
LIGHT_PROMPT = "PROMPT_LIGHT_THEME_NAME"
DARK_PROMPT = "PROMPT_DARK_THEME_NAME"
COMMMENT_VIM = '"'
COMMENT_PROMPT = '#'


def determine_intended_theme():
    """Determine the intended theme by parameters of by the day time

    Returns:
        set_theme (string): Theme that will be set in the config files
    """
    if len(sys.argv) > 1:
        set_theme = sys.argv[1]
    else:
        set_theme = check_day_time_to_set_theme()
    return set_theme


def check_day_time_to_set_theme():
    """Check the hour to decide what theme should be set

    Returns:
        set_theme (string): Theme that will be set in the config files
    """
    # Set day & night time
    now_time = datetime.datetime.now()
    start_day = now_time.replace(hour=6, minute=0, second=0, microsecond=0)
    start_night = now_time.replace(hour=16, minute=30, second=0, microsecond=0)

    if now_time < start_day or now_time > start_night:
        set_theme = "dark"
    else:
        set_theme = "light"

    return set_theme


def change_vim_theme(set_theme):
    """Change the theme in vim config file"""
    comment_with = COMMMENT_VIM
    themes = get_on_off_themes(set_theme, LIGHT_VIM, DARK_VIM)
    change_theme_in_file(PATH_PREFIX + PATH_VIM, themes[0], themes[1],
                         comment_with)


def change_prompt_theme(set_theme):
    """Change the theme in vim config file"""
    comment_with = COMMENT_PROMPT
    themes = get_on_off_themes(set_theme, LIGHT_PROMPT, DARK_PROMPT)
    change_theme_in_file(PATH_PREFIX + PATH_PROMPT, themes[0], themes[1],
                         comment_with)


def get_on_off_themes(set_theme, light, dark):
    """Determine the which value should be set on and off

    Parameters:
        set_theme (string): Name of the theme that will be set
        light (string): A name of the light theme
        dark (string): A name of the dark theme

    Returns:
        arr (arr): A array with the theme names (set_on_theme, set_off_theme)
    """
    if set_theme == light:
        theme_on = light
        theme_off = dark
    else:
        theme_on = dark
        theme_off = light
    return [theme_on, theme_off]


def change_theme_in_file(path_to_file, theme_on, theme_off, comment_with):
    """Modify the config file to set the given theme

    Parameters:
        path_to_file (string): A path to the file which will be changed
        theme_on (string): A theme that will be uncomented (set on)
        theme_off (string): A theme that will be commented (set off)
        comment_with (string): A symbol used as a comment signe in this file
    """
    file = open(path_to_file, "r")
    lines = file.readlines()
    for i, line in enumerate(lines):
        # check if the line has wanted theme
        if line.rfind(theme_on) != -1:
            if line[0] == comment_with:
                line = line[1:len(line) - 1] + "\n"
        else:
            if line.rfind(theme_off) != -1:
                if line[0] != comment_with:
                    line = comment_with + line

        lines[i] = line

    file = open(path_to_file, "w")
    file.writelines(lines)
    file.close()


def main():
    set_theme = determine_intended_theme()
    change_vim_theme(set_theme)
    change_prompt_theme(set_theme)


if __name__ == "__main__":
    main()
