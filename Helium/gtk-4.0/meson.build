gtk4_dir = join_paths(theme_dir, 'gtk-4.0')

# Install asset files to themes/ThemeName/gtk-4.0/assets
install_subdir('assets', install_dir : gtk4_dir, strip_directory : false)

generate_gtk4_light = custom_target('generate_gtk4_light',
        input: 'gtk.scss',
        output: 'gtk.css',
        command: [sass, '--no-source-map', '-s', 'compressed', '@INPUT@', '@OUTPUT@'],
        build_by_default: true,
        install: true,
        install_dir: gtk4_dir,
    )

if get_option('dark')
  generate_gtk4_dark = custom_target('generate_gtk4_dark',
          input: 'gtk-dark.scss',
          output: 'gtk-dark.css',
          command: [sass, '--no-source-map', '-s', 'compressed', '@INPUT@', '@OUTPUT@'],
          build_by_default: true,
          install: true,
          install_dir: gtk4_dir,
      )
endif