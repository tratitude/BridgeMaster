from distutils.core import setup, Extension

setup(name='ddsTable',
      py_modules=['ddsTable.py'],
      ext_modules=[
        Extension('_ddsTable',
                  ['ddsTable_wrap.cxx'],
                  include_dirs = [],
                  define_macros = [],

                  undef_macros = [],
                  library_dirs = [],
                  libraries = ['ddsTable']
                  )
        ]
)
'''
create libddsTable.so

#prepare
activate venv

#step 1 compile ddsTable.cpp
g++ -fPIC -O3 -flto -fopenmp -mtune=generic -std=c++11 -fopenmp -lboost_system -lboost_thread -DDDS_THREADS_BOOST -DDDS_THREADS_OPENMP -DDDS_THREADS_STL ddsTable.cpp -c ddsTable.o

#step 2 linking files
g++ ddsTable.o hands.o -shared -Wl,-O2 -Wl,--sort-common -Wl,--as-needed -Wl,-z -Wl,relro -fopenmp -lboost_system -lboost_thread -fPIC -L. -ldds -o libddsTable.so

#step 3 copy shared library
sudo cp libddsTable.so /usr/local/lib/

#step 4 swig
swig -python -py3 -c++ ddsTable.i

#step 5 .py
python setup.py build_ext --inplace
'''