gtk3_dir = join_paths(theme_dir, 'gtk-3.0')

# Install asset files to themes/ThemeName/gtk-3.0/assets
install_subdir('assets', install_dir : gtk3_dir, strip_directory : false)

gtk3_scss_dependencies = [
  '_functions.scss',
  '_colors-public.scss',
  '_colors.scss',
  '_common.scss',
  '_drawing.scss',
 ]

generate_gtk3_light = custom_target('generate_gtk3_light',
        input: 'gtk.scss',
        output: 'gtk.css',
        command: [sass, '--no-source-map', '@INPUT@', '@OUTPUT@'],
        build_by_default: true,
        install: not meson.is_subproject(),
        install_dir: gtk3_dir,
        depend_files: gtk3_scss_dependencies,
    )

if get_option('dark')
  generate_gtk3_dark = custom_target('generate_gtk3_dark',
          input: 'gtk-dark.scss',
          output: 'gtk-dark.css',
          command: [sass, '--no-source-map', '@INPUT@', '@OUTPUT@'],
          build_by_default: true,
          install: not meson.is_subproject(),
          install_dir: gtk3_dir,
          depend_files: gtk3_scss_dependencies,
      )
endif
