from setuptools import setup

setup(name="youtubevlc",
      version="1.0",
      description="Script to import latest videos into VLC media player.",
      url="https://github.com/Jake0oo0/YoutubeToVLC",
      author="Jake0oo0",
      author_email="jake0oo0andminecraft@gmail.com",
      license="BSD",
      packages=['youtube'],
      entry_points={
          "console_scripts": ["youtube=youtube.YoutubeVLC:main"]
      },
      classifiers=["Operating System :: POSIX",
                   "Operating System :: Microsoft :: Windows",
                   "Environment :: Console",
                   "Development Status :: 5 - Production/Stable",
                   "Topic :: Internet :: WWW/HTTP",
                   "Topic :: Multimedia :: Sound/Audio",
                   "Topic :: Multimedia :: Video",
                   "Topic :: Utilities"]
)