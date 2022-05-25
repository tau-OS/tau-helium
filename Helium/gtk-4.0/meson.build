gtk4_dir = join_paths(theme_dir, 'gtk-4.0')

# Install asset files to themes/ThemeName/gtk-4.0/assets
install_subdir('assets', install_dir : gtk4_dir, strip_directory : false)

# theme sources .scss files

# The files that need to be compiled
if get_option('dark')
  gtk4_scss_sources = [
    'gtk',
    'gtk-dark',
  ]
else
  gtk4_scss_sources = [
    'gtk',
    'gtk-dark',
  ]
endif

# Dependencies of the files that need to be compiled
gtk4_scss_dependencies = [
  '_colors.scss',
  '_common.scss',
  '_compat-colors.scss',
  '_defaults.scss',
  '_drawing.scss',
  '_functions.scss',
  '_widgets.scss',
  '_tauos.scss',

  'widgets/_avatar.scss',
  'widgets/_buttons.scss',
  'widgets/_calendar.scss',
  'widgets/_checks.scss',
  'widgets/_color-chooser.scss',
  'widgets/_dialogs.scss',
  'widgets/_dropdowns.scss',
  'widgets/_emoji-chooser.scss',
  'widgets/_entries.scss',
  'widgets/_expanders.scss',
  'widgets/_file-chooser.scss',
  'widgets/_header-bar.scss',
  'widgets/_labels.scss',
  'widgets/_level-bar.scss',
  'widgets/_linked.scss',
  'widgets/_links.scss',
  'widgets/_lists.scss',
  'widgets/_menus.scss',
  'widgets/_message-dialog.scss',
  'widgets/_misc.scss',
  'widgets/_notebook.scss',
  'widgets/_paned.scss',
  'widgets/_popovers.scss',
  'widgets/_preferences.scss',
  'widgets/_progress-bar.scss',
  'widgets/_scale.scss',
  'widgets/_scrolling.scss',
  'widgets/_shortcuts-window.scss',
  'widgets/_sidebars.scss',
  'widgets/_spinner.scss',
  'widgets/_spin-button.scss',
  'widgets/_switch.scss',
  'widgets/_tab-view.scss',
  'widgets/_text-selection.scss',
  'widgets/_toolbars.scss',
  'widgets/_tooltip.scss',
  'widgets/_transition-shadow.scss',
  'widgets/_trees.scss',
  'widgets/_views.scss',
  'widgets/_view-switcher.scss',
  'widgets/_window.scss',
]

# Generate .css files and install
gtk4_scss_dependencies = files(gtk4_scss_dependencies)
#
foreach f : gtk4_scss_sources
    custom_target('generate_' + f,
        input: f + '.scss',
        output: f + '.css',
        depend_files: gtk4_scss_dependencies,
        command: [sass, '--no-source-map', '-s', 'compressed', '@INPUT@', '@OUTPUT@'],
        build_by_default: true,
        install: true,
        install_dir: gtk4_dir,
    )
endforeach
