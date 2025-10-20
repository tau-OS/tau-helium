project('Helium', license: ['GPL3'], default_options: ['prefix=/usr'])

sass = find_program('sass')

subdir('Helium')

if get_option('dark')
    subdir('Helium-dark')
endif
