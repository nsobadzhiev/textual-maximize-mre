# MRE to reproduce a width issue with maximizing widgets

The issue is that sometimes, when a widget is maximized, it's too narrow even if its width is specified to 100% in CSS.

Steps to reproduce:
* start the app from `app.py`
* Press Tab twice to focus on the article screen widget
* Maximize that widget

Expected result:

CSS specifies the widget should take up 100% of the width

Actual result:

The widget is center in the middle, but very narrow - around 20% od the width
