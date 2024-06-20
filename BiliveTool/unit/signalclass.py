from PySide6.QtCore import QObject, Slot, Signal, QSettings
from PySide6.QtWidgets import (QFontDialog, QColorDialog, QListWidget)


class Signal_To_Lyric(QObject):
    def __init__(self, sub_window):
        self.Lyric_name_width_slider_value = ''
        self.Lyric_window_width_slider_value = ''
        self.Lyric_transparency_slider_value = ''
        self.Lyric_font_set = ''
        self.Lyric_font_color_set = ''
        self.Lyric_bg_color_set = ''

        super().__init__()
        self.lyric_window = sub_window



    @Slot(int)
    def on_name_width_slider_value_changed(self, value):
        self.lyric_window.ui.name.setMinimumWidth(value)
        self.Lyric_name_width_slider_value = value

    @Slot(int)
    def on_window_width_slider_value_changed(self, value):
        self.lyric_window.setFixedWidth(value)
        self.Lyric_window_width_slider_value = value

    @Slot(int)
    def on_transparency_slider_value_changed(self, value):
        value = int(value) / 255
        rgba = self.lyric_window.ui.name.styleSheet().split("rgba(")[1].split(")")[0]
        rgba_values_list = rgba.split(",")
        updated_rgba_style = f"{rgba_values_list[0]},{rgba_values_list[1]},{rgba_values_list[2]}, {value}"
        transparency_newstyle = self.lyric_window.ui.name.styleSheet().replace(rgba, updated_rgba_style)

        self.lyric_window.ui.name.setStyleSheet(transparency_newstyle)
        self.lyric_window.ui.lyric.setStyleSheet(transparency_newstyle)

        self.Lyric_transparency_slider_value = transparency_newstyle


    @Slot()
    def on_set_font_button_clicked(self):
        # 设置字体按钮点击事件
        ok, font = QFontDialog.getFont()
        if ok:
            self.lyric_window.ui.name.setFont(font)
            self.lyric_window.ui.lyric.setFont(font)

            self.Lyric_font_set = font


    @Slot()
    def on_set_color_button_clicked(self):

        color = QColorDialog.getColor()
        if color.isValid():
            red = color.red()
            green = color.green()
            blue = color.blue()
            alpha = color.alpha()
            rgb = f"{red}, {green}, {blue}"
            # 设置字体颜色
            # 设置字体颜色和背景颜色
            color_style = self.lyric_window.ui.name.styleSheet().split("rgb(")[1].split(")")[0]
            style = self.lyric_window.ui.name.styleSheet().replace(color_style, rgb)
            # print(style)
            self.lyric_window.ui.name.setStyleSheet(style)
            self.lyric_window.ui.lyric.setStyleSheet(style)


            self.Lyric_font_color_set = style

    @Slot()
    def on_bg_set_color_button_clicked(self):

        color = QColorDialog.getColor()
        if color.isValid():
            red = color.red()
            green = color.green()
            blue = color.blue()
            alpha = color.alpha()
            rgba = f"rgba({red}, {green}, {blue}, {alpha})"
            # 设置字体颜色
            # 设置字体颜色和背景颜色
            color_style = self.lyric_window.ui.name.styleSheet().split("background-color:")[1].split(";")[0]
            style = self.lyric_window.ui.name.styleSheet().replace(color_style, rgba)
            # print(style)
            self.lyric_window.ui.name.setStyleSheet(style)
            self.lyric_window.ui.lyric.setStyleSheet(style)

            self.Lyric_bg_color_set = style

    def load_settings(self):
        # 读取设置
        settings = QSettings("BiliveTool", "Lyric")
        self.Lyric_name_width_slider_value = settings.value("name_width", type=int)
        self.Lyric_window_width_slider_value = settings.value("window_width", type=int)
        self.Lyric_transparency_slider_value = settings.value("transparency", type=str)
        self.Lyric_font_set = settings.value("font", type=str)
        self.Lyric_font_color_set = settings.value("font_color", type=str)
        self.Lyric_bg_color_set = settings.value("bg_color", type=str)

        # 加载设置
        self.lyric_window.ui.name.setMinimumWidth(self.Lyric_name_width_slider_value)
        self.lyric_window.setFixedWidth(self.Lyric_window_width_slider_value)
        self.lyric_window.ui.name.setStyleSheet(self.Lyric_transparency_slider_value)
        self.lyric_window.ui.lyric.setStyleSheet(self.Lyric_transparency_slider_value)
        self.lyric_window.ui.name.setFont(self.Lyric_font_set)
        self.lyric_window.ui.lyric.setFont(self.Lyric_font_set)
        self.lyric_window.ui.name.setStyleSheet(self.Lyric_font_color_set)
        self.lyric_window.ui.lyric.setStyleSheet(self.Lyric_font_color_set)
        self.lyric_window.ui.name.setStyleSheet(self.Lyric_bg_color_set)
        self.lyric_window.ui.lyric.setStyleSheet(self.Lyric_bg_color_set)



class Signal_To_Song(QObject):
    send2song_window = Signal(object)
    sendcolor2window = Signal(object)

    def __init__(self, sub_window):
        super().__init__(sub_window)
        self.Song_window = sub_window
        self.send2song_window.connect(self.Song_window.get_font)
        self.sendcolor2window.connect(self.Song_window.get_color)

    @Slot(int)
    def on_transparency_slider_value_changed(self, value):
        value = int(value) / 255
        hd_rgba = self.Song_window.lb_headframe.styleSheet().split("rgba(")[1].split(")")[0]
        hd_rgba_values_list = hd_rgba.split(",")
        updated_hd_rgba_style = f"{hd_rgba_values_list[0]},{hd_rgba_values_list[1]},{hd_rgba_values_list[2]}, {value}"
        hd_transparency_newstyle = self.Song_window.lb_headframe.styleSheet().replace(hd_rgba, updated_hd_rgba_style)

        self.Song_window.lb_headframe.setStyleSheet(hd_transparency_newstyle)

        list_rgba = self.Song_window.list_widget.styleSheet().split("rgba(")[1].split(")")[0]
        list_rgba_values_list = list_rgba.split(",")
        updated_list_rgba_style = f"{list_rgba_values_list[0]},{list_rgba_values_list[1]},{list_rgba_values_list[2]}, {value}"
        list_transparency_newstyle = self.Song_window.list_widget.styleSheet().replace(list_rgba, updated_list_rgba_style)

        self.Song_window.list_widget.setStyleSheet(list_transparency_newstyle)

        self.Song_window.container_stylesheet = list_transparency_newstyle

        self.Song_window.reload()

    @Slot()
    def on_set_font_button_clicked(self):
        ok, font = QFontDialog.getFont()
        if ok:
            self.send2song_window.emit(font)
        self.Song_window.reload()

    @Slot()
    def on_set_color_button_clicked(self):
        color = QColorDialog.getColor()
        if color.isValid():
            list_widget = self.Song_window.findChild(QListWidget, 'list_widget')
            list_widget_bg_style = list_widget.styleSheet().split("background-color:")[
                1].split(";")[0] if 'background-color' in list_widget.styleSheet() else 'white'
            style = f"color: {color.name()}; background-color: {list_widget_bg_style}; border: none;"
            list_widget.setStyleSheet(style)
            self.Song_window.container_stylesheet = style
        self.Song_window.reload()

    @Slot()
    def on_bg_set_color_button_clicked(self):
        color = QColorDialog.getColor()
        if color.isValid():
            red = color.red()
            green = color.green()
            blue = color.blue()
            alpha = color.alpha()
            rgba = f"rgba({red}, {green}, {blue}, {alpha})"

            # 设置表头背景颜色
            bt_bg_color_style = self.Song_window.lb_headframe.styleSheet().split("background-color:")[1].split(";")[0]
            style = self.Song_window.lb_headframe.styleSheet().replace(bt_bg_color_style, rgba)
            self.Song_window.lb_headframe.setStyleSheet(style)

            # 设置list背景颜色
            list_bg_color_style = self.Song_window.list_widget.styleSheet().split("background-color:")[1].split(";")[0]
            new_bg_color_style = self.Song_window.list_widget.styleSheet().replace(list_bg_color_style, rgba)
            self.Song_window.list_widget.setStyleSheet(new_bg_color_style)

            self.sendcolor2window.emit(new_bg_color_style)

        self.Song_window.reload()

    def on_bt_set_font_button_clicked(self):
        ok, font = QFontDialog.getFont()
        if ok:
            self.Song_window.lb_headframe.setFont(font)
        self.Song_window.reload()

    def on_bt_set_color_button_clicked(self):
        color = QColorDialog.getColor()
        if color.isValid():
            red = color.red()
            green = color.green()
            blue = color.blue()
            alpha = color.alpha()
            rgb = f"{red}, {green}, {blue}"

            lb_head_style = self.Song_window.lb_headframe.styleSheet().split("rgb(")[1].split(")")[0]
            style = self.Song_window.lb_headframe.styleSheet().replace(lb_head_style, rgb)
            self.Song_window.lb_headframe.setStyleSheet(style)
        self.Song_window.reload()




class Signal_To_Queue(QObject):

    send2window = Signal(object)
    sendcolor2window = Signal(object)

    def __init__(self, sub_window):
        super().__init__(sub_window)
        self.Queue_window = sub_window
        self.send2window.connect(self.Queue_window.receive_font)
        self.sendcolor2window.connect(self.Queue_window.receive_color)

    @Slot(int)
    def on_transparency_slider_value_changed(self, value):
        value = int(value)/255
        hd_rgba = self.Queue_window.lb_headframe.styleSheet().split("rgba(")[1].split(")")[0]
        hd_rgba_values_list = hd_rgba.split(",")
        updated_hd_rgba_style = f"{hd_rgba_values_list[0]},{hd_rgba_values_list[1]},{hd_rgba_values_list[2]}, {value}"
        hd_transparency_newstyle = self.Queue_window.lb_headframe.styleSheet().replace(hd_rgba, updated_hd_rgba_style)

        self.Queue_window.lb_headframe.setStyleSheet(hd_transparency_newstyle)

        list_rgba = self.Queue_window.list_widget.styleSheet().split("rgba(")[1].split(")")[0]
        list_rgba_values_list = list_rgba.split(",")
        updated_list_rgba_style = f"{list_rgba_values_list[0]},{list_rgba_values_list[1]},{list_rgba_values_list[2]}, {value}"
        list_transparency_newstyle = self.Queue_window.list_widget.styleSheet().replace(list_rgba, updated_list_rgba_style)

        self.Queue_window.list_widget.setStyleSheet(list_transparency_newstyle)

        self.Queue_window.container_stylesheet = list_transparency_newstyle


        self.Queue_window.reload()



    @Slot()
    def on_set_font_button_clicked(self):
        ok, font = QFontDialog.getFont()
        if ok:
            self.send2window.emit(font)
        self.Queue_window.reload()


    @Slot()
    def on_set_color_button_clicked(self):
        color = QColorDialog.getColor()
        if color.isValid():
            list_widget = self.Queue_window.findChild(QListWidget, 'list_widget')
            list_widget_bg_style = list_widget.styleSheet().split("background-color:")[
                1].split(";")[0] if 'background-color' in list_widget.styleSheet() else 'white'
            style = f"color: {color.name()}; background-color: {list_widget_bg_style}; border: none;"
            list_widget.setStyleSheet(style)
            self.Queue_window.container_stylesheet = style
        self.Queue_window.reload()



    @Slot()
    def on_bg_set_color_button_clicked(self):
        color = QColorDialog.getColor()
        if color.isValid():
            red = color.red()
            green = color.green()
            blue = color.blue()
            alpha = color.alpha()
            rgba = f"rgba({red}, {green}, {blue}, {alpha})"


            # 设置表头背景颜色
            bt_bg_color_style = self.Queue_window.lb_headframe.styleSheet().split("background-color:")[1].split(";")[0]
            style = self.Queue_window.lb_headframe.styleSheet().replace(bt_bg_color_style, rgba)
            self.Queue_window.lb_headframe.setStyleSheet(style)

            # 设置list背景颜色
            list_bg_color_style = self.Queue_window.list_widget.styleSheet().split("background-color:")[1].split(";")[0]
            new_bg_color_style = self.Queue_window.list_widget.styleSheet().replace(list_bg_color_style, rgba)
            self.Queue_window.list_widget.setStyleSheet(new_bg_color_style)


            self.sendcolor2window.emit(new_bg_color_style)

        self.Queue_window.reload()

    def on_bt_set_font_button_clicked(self):
        ok, font = QFontDialog.getFont()
        if ok:
            self.Queue_window.lb_headframe.setFont(font)
        self.Queue_window.reload()

    def on_bt_set_color_button_clicked(self):
        color = QColorDialog.getColor()
        if color.isValid():
            red = color.red()
            green = color.green()
            blue = color.blue()
            alpha = color.alpha()
            rgb = f"{red}, {green}, {blue}"

            lb_head_style = self.Queue_window.lb_headframe.styleSheet().split("rgb(")[1].split(")")[0]
            style = self.Queue_window.lb_headframe.styleSheet().replace(lb_head_style, rgb)
            self.Queue_window.lb_headframe.setStyleSheet(style)
        self.Queue_window.reload()



