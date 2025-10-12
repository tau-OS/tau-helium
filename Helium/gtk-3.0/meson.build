gtk3_dir = join_paths(theme_dir, 'gtk-3.0')

# Install asset files to themes/ThemeName/gtk-3.0/assets
install_subdir('assets', install_dir: gtk3_dir, strip_directory: false)

# theme sources .scss files

# The files that need to be compiled
if get_option('dark')
  gtk3_scss_sources = [
    'gtk',
    'gtk-dark',
  ]
else
  gtk3_scss_sources = [
    'gtk',
    'gtk-dark',
  ]
endif

# Dependencies of the files that need to be compiled
gtk3_scss_dependencies = [
  '_colors-defaults.scss',
  '_colors-public.scss',
  '_colors.scss',
  '_drawing.scss',
  '_functions.scss',
  '_palette.scss',

  'widgets/_bars.scss',
  'widgets/_base.scss',
  'widgets/_button.scss',
  'widgets/_check-radio.scss',
  'widgets/_combobox.scss',
  'widgets/_dialog.scss',
  'widgets/_entry.scss',
  'widgets/_flowbox.scss',
  'widgets/_frame.scss',
  'widgets/_headerbar.scss',
  'widgets/_index.scss',
  'widgets/_infobar.scss',
  'widgets/_label.scss',
  'widgets/_list.scss',
  'widgets/_menu.scss',
  'widgets/_misc.scss',
  'widgets/_notebook.scss',
  'widgets/_pathbar.scss',
  'widgets/_popover.scss',
  'widgets/_scale.scss',
  'widgets/_scrollbar.scss',
  'widgets/_sidebar.scss',
  'widgets/_spinbutton.scss',
  'widgets/_switch.scss',
  'widgets/_toolbar.scss',
  'widgets/_typography.scss',
  'widgets/_view.scss',

  'platforms/_budgie.scss',
  'platforms/_granite.scss',
  'platforms/_index.scss',
  'platforms/_libhandy.scss',
  'platforms/_phosh.scss',
]

# Generate .css files and install
gtk3_scss_dependencies = files(gtk3_scss_dependencies)
foreach f : gtk3_scss_sources
  custom_target(
    'generate_' + f,
    input: f + '.scss',
    output: f + '.css',
    depend_files: gtk3_scss_dependencies,
    command: [sass, '--quiet-deps', '--no-source-map', '@INPUT@', '@OUTPUT@'],
    build_by_default: true,
    install: true,
    install_dir: gtk3_dir,
  )
endforeach
