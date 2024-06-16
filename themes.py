# themes.py
from PyQt5.QtGui import QColor


def apply_light_theme(app):
    palette = app.palette()
    palette.setColor(palette.Window, QColor(255, 255, 255))
    palette.setColor(palette.WindowText, QColor(0, 0, 0))
    palette.setColor(palette.Base, QColor(255, 255, 255))
    palette.setColor(palette.AlternateBase, QColor(242, 242, 242))
    palette.setColor(palette.ToolTipBase, QColor(255, 255, 220))
    palette.setColor(palette.ToolTipText, QColor(0, 0, 0))
    palette.setColor(palette.Text, QColor(0, 0, 0))
    palette.setColor(palette.Button, QColor(255, 255, 255))
    palette.setColor(palette.ButtonText, QColor(0, 0, 0))
    palette.setColor(palette.BrightText, QColor(255, 0, 0))
    app.setPalette(palette)


def apply_dark_theme(app):
    palette = app.palette()
    palette.setColor(palette.Window, QColor(53, 53, 53))
    palette.setColor(palette.WindowText, QColor(255, 255, 255))
    palette.setColor(palette.Base, QColor(42, 42, 42))
    palette.setColor(palette.AlternateBase, QColor(66, 66, 66))
    palette.setColor(palette.ToolTipBase, QColor(255, 255, 220))
    palette.setColor(palette.ToolTipText, QColor(0, 0, 0))
    palette.setColor(palette.Text, QColor(255, 255, 255))
    palette.setColor(palette.Button, QColor(53, 53, 53))
    palette.setColor(palette.ButtonText, QColor(255, 255, 255))
    palette.setColor(palette.BrightText, QColor(255, 0, 0))
    app.setPalette(palette)
