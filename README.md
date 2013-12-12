Description
===========

Customizations towards phennymods for our crazy little IRC channels.

Testing
=======

Test your changes like so:

```python
$ python
Python 2.7.3 (default, Jul 24 2012, 10:05:38)
[GCC 4.7.0 20120507 (Red Hat 4.7.0-5)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> class Phenny(object):
...     def say(self, msg):
...             print msg
...
>>> import dance
>>>
>>> dance.dance(Phenny(), None)
    <("<)
           <("^)
                  ^("^)
                   (^")^
            (^")>
     (>")>
>>>
```

To test wunderground changes:

```python wunderground.py pws:KORHILLS16
[Hillsboro at 231st, Hillsboro, Oregon, US] Current: Light Freezing Fog 24.2F, -4.3C Humidity: 98%, Wind: Calm
```
