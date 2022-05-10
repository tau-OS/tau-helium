sass = find_program('sassc')
install_exec = meson.current_source_dir() / 'meson' / 'install-to-dir.py'
theme = 'Helium'

sass_command = [
    sass,
    '@INPUT@',
    '@OUTPUT@'
]

theme_project_name = meson.project_name()

theme_target = custom_target(
    theme_project_name,
    input : 'themes' / theme + '.scss',
    output : theme + '.css',
    command : sass_command,
    build_by_default: true
)

theme_dark_target = custom_target(
    theme_project_name + '-dark',
    input : 'themes' / theme + '-dark.scss',
    output : theme + '-dark.css',
    command : sass_command,
    build_by_default: true
)

dest_theme_dir = get_option('datadir') / 'themes' / theme_project_name

meson.add_install_script (install_exec,
    theme_target.full_path(),
    dest_theme_dir / 'gtk-4.0' / 'gtk.css'
)

meson.add_install_script (install_exec,
    theme_dark_target.full_path(),
    dest_theme_dir / 'gtk-4.0' / 'gtk-dark.css'
)

install_subdir([
    'assets',
], install_dir: dest_theme_dir / 'gtk-4.0' )
