grapher
=======

:code:`grapher` is a a fork of @holman's spark that allows you to plot things in the terminal.

Installation (with epm)
-----------------------

.. code::

   epm install-pkg grapher.py

Installation (without epm)
--------------------------

Download :code:`grapher.py` and place it in :code:`~/.ergo/packages/.`.

Usage
-----

The :code:`grapher` package provides the :code:`graph` command, which accepts a series of numbers and graphs them with special unicode block characters, like so:

.. code::
   
   $ graph 1 5 92 84 33
   ▁▁█▃▅

