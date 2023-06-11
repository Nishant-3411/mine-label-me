import argparse
import codecs
import logging
import os
import os.path as osp
import sys
import yaml

from qtpy import QtCore
from qtpy import QtWidgets

from labelme import __appname__
from labelme import __version__
from labelme.app import MainWindow          
from labelme.config import get_config
from labelme.logger import logger
from labelme.utils import newIcon



def main():
    reset_config = False
    filename = None
    output = None
    output_file = None
    output_dir = None
    # config = get_config()

    # print("CONFIG:", config)

    config = {'auto_save': False, 
     'display_label_popup': True, 'store_data': True, 'keep_prev': False, 'keep_prev_scale': False, 'keep_prev_brightness': False, 'keep_prev_contrast': False, 
     'logger_level': 'info', 'flags': None, 'label_flags': None, 'labels': None, 'file_search': None, 'sort_labels': True, 
     'validate_label': None, 'default_shape_color': [0, 255, 0], 'shape_color': 'auto', 'shift_auto_shape_color': 0, 'label_colors': None, 
     'shape': {'line_color': [0, 255, 0, 128], 'fill_color': [0, 255, 0, 0], 'vertex_fill_color': [0, 255, 0, 255], 'select_line_color': [255, 255, 255, 255], 
    'select_fill_color': [0, 255, 0, 155], 'hvertex_fill_color': [255, 255, 255, 255], 'point_size': 8}, 
     'flag_dock': {'show': True, 'closable': True, 'movable': True, 'floatable': True}, 'label_dock': {'show': True, 'closable': True, 'movable': True, 'floatable': True},
     'shape_dock': {'show': True, 'closable': True, 'movable': True, 'floatable': True}, 'file_dock': {'show': True, 'closable': True, 'movable': True, 'floatable': True}, 
     'show_label_text_field': True, 'label_completion': 'startswith', 'fit_to_content': {'column': True, 'row': False}, 'epsilon': 10.0, 
     'canvas': {'double_click': 'close', 'num_backups': 10, 'crosshair': {'polygon': False, 'rectangle': True, 'circle': False, 'line': False, 'point': False, 'linestrip': False}, 'IRF': [255, 0, 0, 128], 'SRF': [0, 255, 0, 128], 'PED': [0, 0, 255, 128]}, 
     'shortcuts': {'close': 'Ctrl+W', 'open': 'Ctrl+O', 'open_dir': 'Ctrl+U', 'quit': 'Ctrl+Q', 'save': 'Ctrl+S', 'save_as': 'Ctrl+Shift+S', 'save_to': None, 'delete_file': 'Ctrl+Delete', 
                'analyze': 'Ctrl+A+I', 'open_next': ['D', 'Ctrl+Shift+D'], 'open_prev': ['A', 'Ctrl+Shift+A'], 'zoom_in': ['Ctrl++', 'Ctrl+='], 'zoom_out': 'Ctrl+-', 'zoom_to_original': 'Ctrl+0', 'fit_window': 'Ctrl+F', 'fit_width': 'Ctrl+Shift+F', 'create_polygon': 'Ctrl+N', 'create_rectangle': 'Ctrl+R', 'create_circle': None, 'create_line': None, 'create_point': None, 'create_linestrip': None, 'edit_polygon': 'Ctrl+J', 'delete_polygon': 'Delete', 'duplicate_polygon': 'Ctrl+D', 'copy_polygon': 'Ctrl+C', 'paste_polygon': 'Ctrl+V', 'undo': 'Ctrl+Z', 'undo_last_point': 'Ctrl+Z', 'add_point_to_edge': 'Ctrl+Shift+P', 'edit_label': 'Ctrl+E', 'toggle_keep_prev_mode': 'Ctrl+P', 
                'remove_selected_point': ['Meta+H', 'Backspace']}} 

    if output is not None:
        if output.endswith(".json"):
            output_file = output
        else:
            output_dir = output

    translator = QtCore.QTranslator()
    translator.load(
        QtCore.QLocale.system().name(),
        osp.dirname(osp.abspath(__file__)) + "/translate",
    )
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName(__appname__)                 #name of app
    app.setWindowIcon(newIcon("icon"))
    app.installTranslator(translator)
    win = MainWindow(                                     #win object calls mainwindow class
        config=config,
        filename=filename,
        output_file=output_file,
        output_dir=output_dir,
    )

    if reset_config:
        logger.info("Resetting Qt config: %s" % win.settings.fileName())
        win.settings.clear()
        sys.exit(0)

    win.show()
    win.raise_()
    sys.exit(app.exec_())


# this main block is required to generate executable by pyinstaller
if __name__ == "__main__":
    main()
