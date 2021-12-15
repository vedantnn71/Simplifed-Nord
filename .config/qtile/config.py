from typing import List  # noqa: F401

from libqtile import qtile
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import psutil
import os
import subprocess

mod = "mod4"
alt = "mod1"

# Default Apps
terminal = "alacritty"
browser = "brave-browser-dev"
file_manager = "thunar"
text_editor = "alacritty -e '/bin/nvim'"
music_client = "spotify"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "control"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "control"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "control"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "control"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "shift"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "shift"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "shift"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "shift"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "control"], "Return", lazy.spawn(terminal + " -e /bin/tmux"), desc="Launch tmux terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.spawn(".config/qtile/scripts/rofi/powermenu.sh"), desc="Shutdown Qtile"),
    Key([mod], "p", lazy.spawn("dmenu_run"),
        desc="Runner"),

    # Launch Apps
    Key(["mod1", "shift"], "b", lazy.spawn(browser), desc="Launch Web Browser"),
    Key(["mod1", "shift"], "e", lazy.spawn(text_editor), desc="Launch Text Editor"),
    Key(["mod1", "shift"], "d", lazy.spawn(file_manager), desc="Launch File Manager"),
    Key(["mod1", "shift"], "m", lazy.spawn(music_client), desc="Launch Music Player"),

]


group_names = [
    ("", {
        'layout': 'columns',
        'matches': [Match(wm_class=["qutebrowser", "Firefox", "Brave-browser"])]
    }),
    ("", {
        'layout': 'columns',
        'matches': [Match(wm_class=["emacs", "code", "code-oss", "vscodium", "vim", "neovim"])]
    }),
    ("", {
        'layout': 'columns',
        'matches': [Match(wm_class=["st-256color", "kitty", "alacritty", "termite"])]
    }),
    ("", {
        'layout': 'columns',
        'matches': [Match(wm_class=["evince", "zathura", "thunar", "Pcmanfm", "nautilus", "Bitwarden", "ranger"])]
    }),
    ("", {
        'layout': 'columns',
        'matches': [Match(wm_class=["zoom", "cheese", "droidcam"])]
    }),
    ("", {
        'layout': 'floating',
        'matches': [Match(wm_class=["discord"])]
    }),
    ("", {
        'layout': 'floating',
        'matches': [Match(wm_class=["spotify", "lollypop", "audacity", "audacious"])]
    }),
    ("", {
        'layout': 'floating',
        'matches': [Match(wm_class=["lxappearance", "qt5ct", "gnome-tweaks", "nitrogen", "feh"])]
    }),
    ("", {
        'layout': 'floating',
        'matches': [Match(wm_class=["gimp-2.10", "nitrogen", "feh"])]
    }),
]
groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layout_theme = {
	"border_width": 0,
    "margin": 8,
    "border_focus": "4c566a",
    "border_normal": "2e3440",
    "border_radius": 8,
}

layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Floating(**layout_theme)
]

colors = [
        ["#2e3440", "#2e3440"],  # 0 background
        ["#d8dee9", "#d8dee9"],  # 1 foreground
        ["#3b4252", "#3b4252"],  # 2 background lighter
        ["#8fbcbb", "#8fbcbb"],  # 3 red
        ["#a3be8c", "#a3be8c"],  # 4 green
        ["#ebcb8b", "#ebcb8b"],  # 5 yellow
        ["#81a1c1", "#81a1c1"],  # 6 blue
        ["#b48ead", "#b48ead"],  # 7 magenta
        ["#88c0d0", "#88c0d0"],  # 8 cyan
        ["#e5e9f0", "#e5e9f0"],  # 9 white
        ["#4c566a", "#4c566a"],  # 10 grey
        ["#d08770", "#d08770"],  # 11 orange
        ["#8fbcbb", "#8fbcbb"],  # 12 super cyan
        ["#5e81ac", "#5e81ac"],  # 13 super blue
        ["#242831", "#242831"],  # 14 super dark background
]
widget_defaults = {
    'font': 'JetBrainsMono Nerd Font',
    'fontsize': 12,
    'padding': 3,
    'background': colors[14]
}
extension_defaults = widget_defaults.copy()

group_box_settings = {
        "padding": 5,
        "borderwidth": 4,
        "active": colors[9],
        "inactive": colors[10],
        "disable_drag": True,
        "rounded": True,
        "highlight_color": colors[2],
        "block_highlight_text_color": colors[6],
        "highlight_method": "block",
        "this_current_screen_border": colors[14],
        "this_screen_border": colors[7],
        "other_current_screen_border": colors[14],
        "other_screen_border": colors[14],
        "foreground": colors[1],
        "background": colors[14],
        "urgent_border": colors[3],
}

screens = [
    Screen(
       	top=bar.Bar(
               [
                    widget.TextBox(
                        "",
                        padding=12,
                        foreground=colors[4],
                        mouse_callbacks = {"Button1": lambda: lazy.cmd_spawn(".config/qtile/scripts/rofi/launcher.sh")},
                    ),
                    widget.Sep(
                        size_percent=40,
                        opacity = 0,
                    ),
                    widget.GroupBox(**group_box_settings),
                    widget.Spacer(
                        background=colors[14]
                    ),
                    widget.WindowName(
                        empty_group_string = "Desktop",
                        format = "  {name}",
                        background = colors[14],
                        max_chars = 15
                    ),
                   widget.Spacer(
                        length=50,
                        background=colors[14]
                    ),

                   widget.TextBox(
                       "",
                       foreground = colors[3]
                   ),
                   widget.Volume(
                       foreground = colors[3]
                   ),
                   widget.Sep(
                        size_percent = 40,
                        padding = 20
                    ),
                    widget.CurrentLayoutIcon(
                        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                        foreground=colors[3],
                        scale=0.50
                    ),
                   widget.Sep(
                       size_percent = 40,
                       padding = 20
                   ),
                   widget.Clock(
                       format = " %a, %H:%M",
                       foreground=colors[3]
                   ), 
                   widget.Sep(
                       size_percent = 40,
                       padding = 20
                   ),
                   widget.Systray(),
                   widget.Sep(
                           size_percent = 40,
                           icon_size = 14,
                           padding = 20
                    ),
                   widget.TextBox(
                        "",
                        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(".config/qtile/scripts/rofi/powermenu.sh")},
                        foreground=colors[3]
                    ),
                   widget.Sep(
                       size_percent = 0,
                       padding = 10
                   )

                ],
            32,
            margin=[6, 6, 6, 6],
            background=colors[14]
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    **layout_theme,
    float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pcmanfm'),
    Match(title='Thunar'),
    Match(title='gimp'),
    Match(title='Nitrogen'),
    Match(title="lxappearance"),
    Match(title='audacity'),
    Match(title='kdenlive'),
    Match(title='totem'),
    Match(title='mpd2'),
])
auto_fullscreen = True

# Startup scripts
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "qtile"
