# -*- coding: utf-8 -*-
from distutils.core import setup
import setup_translate

pkg = 'Extensions.ArabicSavior'
setup(name='enigma2-plugin-extensions-arabicsavior',
       version='1.2',
       description='Plugin For Arabic langauge correction.',
       packages=[pkg],
       package_dir={pkg: 'plugin'},
       package_data={pkg: ['plugin.png', 'font_default.otf', '*/*.png', 'images/*.png', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass, # for translation
      )
