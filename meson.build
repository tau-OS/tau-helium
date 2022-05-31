project('Helium',
        meson_version: '>= 0.56',
        license : ['LGPL2.1'],
        default_options: ['prefix=/usr'])

sass = find_program('sass')

subdir('Helium')

if get_option('dark')
    subdir('Helium-dark')
endif
