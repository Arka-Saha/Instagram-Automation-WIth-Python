from distutils.core import setup
setup(
  name = 'instacomment',         # How you named your package folder (MyLib)
  packages = ['instacomment'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A simple Python Library that helps to post costom comments in instagram posts',   # Give a short description about your library
  author = 'Arka Saha',                   # Type in your name
  author_email = 'i.am.arka.saha@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Arka-Saha/instacomment',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Arka-Saha/instacomment/archive/refs/tags/v_01.tar.gz',    # I explain this later on
  keywords = ['instagram', 'automation', 'instagramPosts', 'auto comments', 'instagram posts comment'],   # Keywords that define your package best
  install_requires=[           
          'selenium',
          'time',
          'keyboard',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)
