import os
import re
from PyQt6 import QtWidgets, QtCore, QtGui, QtPrintSupport
from about import AboutMessage
from find import Find
from replace import Replace
from go_to import GoTo 

MIME_TYPES = ["text/plain", "application/json", "text/x-python", "text/x-qml"] 

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.settings = QtCore.QSettings("Darlington Nkwaze", "Notepad Clone")
        self.readSettings()
        self.about_message = AboutMessage()
        self.find_dialog = Find()
        self.replace_dialog = Replace()
        self.go_to_dialog = GoTo()
        self.resize(self.settings.value("mainwindow/size"))
        self.move(self.settings.value("mainwindow/pos"))
        #self.resize(800,600)
        self.setWindowTitle(QtCore.QCoreApplication.applicationName())
        self.setWindowIcon(QtGui.QIcon("./dn_logo.png"))
        self.menu_bar = QtWidgets.QMenuBar(self)
        self.setMenuBar(self.menu_bar)
        self.file_menu = QtWidgets.QMenu("File", self)
        self.new_action = QtGui.QAction("New", self)
        self.new_action.setShortcut("Ctrl+N")
        self.new_window_action = QtGui.QAction("New Window", self)
        self.new_window_action.setShortcut("Ctrl+Shift+N")
        self.open_action = QtGui.QAction("Open...", self)
        self.open_action.setShortcut("Ctrl+O")
        self.save_action = QtGui.QAction("Save", self)
        self.save_action.setShortcut('Ctrl+S')
        self.save_as_action = QtGui.QAction("Save As...", self)
        self.save_as_action.setShortcut("Ctrl+Shift+S")
        self.page_setup_action = QtGui.QAction("Page Setup...", self)
        self.print_action = QtGui.QAction("Print...", self)
        self.print_action.setShortcut("Ctrl+P")
        self.exit_action = QtGui.QAction("Exit", self)
        self.exit_action.setShortcut(QtGui.QKeySequence.StandardKey.Close)
        self.file_menu.addAction(self.new_action)
        self.file_menu.addAction(self.new_window_action)
        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.save_as_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.page_setup_action)
        self.file_menu.addAction(self.print_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.exit_action)
        self.edit_menu = QtWidgets.QMenu("Edit", self)
        self.undo_action = QtGui.QAction("Undo", self)
        self.undo_action.setShortcut("Ctrl+Z")
        self.cut_action = QtGui.QAction("Cut", self)
        self.cut_action.setShortcut("Ctrl+X")
        self.copy_action = QtGui.QAction("Copy", self)
        self.copy_action.setShortcut("Ctrl+C")
        self.paste_action = QtGui.QAction("Paste", self)
        self.paste_action.setShortcut("Ctrl+V")
        self.delete_action = QtGui.QAction("Delete", self)
        self.delete_action.setShortcut("Del")
        self.search_bing_action = QtGui.QAction("Search with Bing...", self)
        self.search_bing_action.setShortcut("Ctrl+E")
        self.find_action = QtGui.QAction("Find...", self) 
        self.find_action.setShortcut("Ctrl+F")
        self.find_next_action = QtGui.QAction("Find Next", self)
        self.find_next_action.setShortcut("F3")
        self.find_previous_action = QtGui.QAction("Find Previous", self)
        self.find_previous_action.setShortcut("Shift+F3")
        self.replace_action = QtGui.QAction("Replace...", self)
        self.replace_action.setShortcut("Ctrl+H")
        self.go_to_action = QtGui.QAction("Go To...", self)
        self.go_to_action.setShortcut("Ctrl+G")
        self.select_all_action = QtGui.QAction("Select All", self)
        self.select_all_action.setShortcut("Ctrl+A")
        self.time_date_action = QtGui.QAction("Time/Date", self)
        self.time_date_action.setShortcut("Ctrl+F5")
        self.edit_menu.addAction(self.undo_action)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.cut_action)
        self.edit_menu.addAction(self.copy_action)
        self.edit_menu.addAction(self.paste_action)
        self.edit_menu.addAction(self.delete_action)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.search_bing_action)
        self.edit_menu.addAction(self.find_action)
        self.edit_menu.addAction(self.find_next_action)
        self.edit_menu.addAction(self.find_previous_action)
        self.edit_menu.addAction(self.replace_action)
        self.edit_menu.addAction(self.go_to_action)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.select_all_action)
        self.edit_menu.addAction(self.time_date_action)
        self.format_menu = QtWidgets.QMenu("Format", self)
        self.word_wrap_action = QtGui.QAction("Word Wrap", self)
        self.word_wrap_action.setCheckable(True)
        self.word_wrap_action.setChecked(self.settings.value("wordwrap/checked", type=bool))
        self.font_action = QtGui.QAction("Font...", self)
        self.format_menu.addAction(self.word_wrap_action)
        self.format_menu.addAction(self.font_action)        
        self.view_menu = QtWidgets.QMenu("View", self)
        self.zoom_menu = QtWidgets.QMenu("Zoom", self)
        self.zoom_in = QtGui.QAction("Zoom In", self)
        self.zoom_in.setShortcut("Ctrl++")
        self.zoom_out = QtGui.QAction("Zoom Out", self)
        self.zoom_out.setShortcut("Ctrl+-")
        self.restore_zoom = QtGui.QAction("Restore Default Zoom", self)
        self.restore_zoom.setShortcut("Ctrl+0")
        self.zoom_menu.addAction(self.zoom_in)
        self.zoom_menu.addAction(self.zoom_out)
        self.zoom_menu.addAction(self.restore_zoom)
        self.status_bar_action = QtGui.QAction("Status Bar", self)
        self.status_bar_action.setCheckable(True)
        #self.status_bar_action.setChecked(True)
        self.status_bar_action.setChecked(self.settings.value("statusbar/checked", type=bool))
        self.view_menu.addAction(self.zoom_menu.menuAction()) 
        self.view_menu.addAction(self.status_bar_action)
        self.help_menu = QtWidgets.QMenu("Help", self)
        self.view_help_action = QtGui.QAction("View Help", self)
        self.send_feedback_action = QtGui.QAction("Send Feedback", self)
        self.about_action = QtGui.QAction("About Notepad Clone", self)
        self.help_menu.addAction(self.view_help_action)
        self.help_menu.addAction(self.send_feedback_action)  
        self.help_menu.addSeparator()   
        self.help_menu.addAction(self.about_action)   
        self.menu_bar.addMenu(self.file_menu)
        self.menu_bar.addMenu(self.edit_menu)
        self.menu_bar.addMenu(self.format_menu) 
        self.menu_bar.addMenu(self.view_menu)       
        self.menu_bar.addMenu(self.help_menu)        
        self.plain_text_edit = QtWidgets.QPlainTextEdit(self)
        self.plain_text_edit.verticalScrollBar().setVisible(True)
        self.plain_text_edit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.plain_text_edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.plain_text_edit.setStyleSheet('border: none')
        self.initial_font = self.plain_text_edit.font().pointSize()
        
        self.setCentralWidget(self.plain_text_edit)

        self.status_bar = QtWidgets.QStatusBar(self)
        self.status_bar.setStyleSheet("QStatusBar::item { border: 0px }")

        row = self.plain_text_edit.textCursor().blockNumber() + 1
        col = self.plain_text_edit.textCursor().positionInBlock() + 1
        self.label = QtWidgets.QLabel("", self)
        self.label_2 = QtWidgets.QLabel(f"Ln {row}, Col {col}", self)
        self.label_2.setContentsMargins(9,3,65,3)
        self.label_3 = QtWidgets.QLabel('100.0%')
        self.label_3.setObjectName('label_3')
        self.label_3.setContentsMargins(3,3,6,3)
        self.label_4 = QtWidgets.QLabel('Windows (CRLF)')
        self.label_4.setContentsMargins(3,3,22,3)
        self.label_5 = QtWidgets.QLabel('UTF8')
        self.label_5.setObjectName('label_4')
        self.label_5.setContentsMargins(4,3,82,3)
        self.label_5.setStyleSheet('QLabel {border: 0px}')
        self.v_line = QtWidgets.QFrame(self)
        self.v_line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.v_line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.v_line.setStyleSheet('color: lightgrey')
        self.v_line_2 = QtWidgets.QFrame(self)
        self.v_line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.v_line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.v_line_2.setStyleSheet('color: lightgrey')
        self.v_line_3 = QtWidgets.QFrame(self)
        self.v_line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.v_line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.v_line_3.setStyleSheet('color: lightgrey')
        self.v_line_4 = QtWidgets.QFrame(self)
        self.v_line_4.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.v_line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.v_line_4.setStyleSheet('color: lightgrey')
        self.status_bar.addPermanentWidget(self.label)
        self.status_bar.addPermanentWidget(self.v_line)
        self.status_bar.addPermanentWidget(self.label_2)
        self.status_bar.addPermanentWidget(self.v_line_2)
        self.status_bar.addPermanentWidget(self.label_3)
        self.status_bar.addPermanentWidget(self.v_line_3)
        self.status_bar.addPermanentWidget(self.label_4)
        self.status_bar.addPermanentWidget(self.v_line_4)
        self.status_bar.addPermanentWidget(self.label_5)
        self.setStatusBar(self.status_bar)

        if self.word_wrap_action.isChecked():
            self.go_to_action.setEnabled(False)
            self.plain_text_edit.setLineWrapMode(QtWidgets.QPlainTextEdit.LineWrapMode.WidgetWidth)
        else:
            self.go_to_action.setEnabled(True)
            self.plain_text_edit.setLineWrapMode(QtWidgets.QPlainTextEdit.LineWrapMode.NoWrap)

        if self.status_bar_action.isChecked():
            self.status_bar.show()
        else:
            self.status_bar.hide()

        if not self.plain_text_edit.toPlainText():
            self.find_action.setEnabled(False)
            self.find_next_action.setEnabled(False)
            self.find_previous_action.setEnabled(False)
        if self.plain_text_edit.toPlainText():
            self.find_action.setEnabled(True)    
            self.find_next_action.setEnabled(True)
            self.find_previous_action.setEnabled(True)

        document = self.plain_text_edit.document()
        document.modificationChanged.connect(self.save_action.setEnabled)
        document.modificationChanged.connect(self.setWindowModified)
        document.undoAvailable.connect(self.undo_action.setEnabled)
        self.setWindowModified(document.isModified())
        self.save_action.setEnabled(document.isModified())
        self.undo_action.setEnabled(document.isUndoAvailable())

        self.plain_text_edit.cursorPositionChanged.connect(self.status_bar_modifier)
  
        #File Menu
        self.new_action.triggered.connect(self.file_new)
        self.new_window_action.triggered.connect(self.file_new_window)
        self.open_action.triggered.connect(self.file_open)
        self.save_action.triggered.connect(self.file_save)
        self.save_as_action.triggered.connect(self.file_save_as)
        self.page_setup_action.triggered.connect(self.file_page_setup)
        self.print_action.triggered.connect(self.file_print)
        self.exit_action.triggered.connect(self.close)

        #Edit Menu
        self.undo_action.triggered.connect(self.undo_changes)
        self.cut_action.setEnabled(False)
        self.plain_text_edit.copyAvailable.connect(self.cut_action.setEnabled)
        self.cut_action.triggered.connect(self.plain_text_edit.cut)
        self.copy_action.setEnabled(False)
        self.plain_text_edit.copyAvailable.connect(self.copy_action.setEnabled)
        self.copy_action.triggered.connect(self.plain_text_edit.copy)
        self.paste_action.setEnabled(False)
        self.paste_action.triggered.connect(self.plain_text_edit.paste)
        self.delete_action.setEnabled(False)
        self.plain_text_edit.selectionChanged.connect(self.delete_enabled)
        self.delete_action.triggered.connect(self.delete_selection)
        self.plain_text_edit.textChanged.connect(self.find_actions_behavior)
        self.search_bing_action.setEnabled(False)
        self.plain_text_edit.selectionChanged.connect(self.search_bing_enabled)
        self.search_bing_action.triggered.connect(self.search_bing)
        self.find_action.triggered.connect(self.show_find_dialog)
        self.find_dialog.push_button.clicked.connect(self.find_text)
        self.find_next_action.triggered.connect(self.find_next_word)
        self.find_previous_action.triggered.connect(self.find_previous_word)
        self.replace_action.triggered.connect(self.show_replace_dialog)
        self.go_to_action.triggered.connect(self.go_to_word)
        self.select_all_action.triggered.connect(self.plain_text_edit.selectAll)
        self.time_date_action.triggered.connect(self.set_time_date) 
       
        #Format Menu
        self.word_wrap_action.triggered.connect(self.word_wrap_action_clicked)
        self.font_action.triggered.connect(self.font_dialog)
        #end of Format Menu
        #View Menu
        self.zoom_in.triggered.connect(self.zoom_in_clicked)
        self.zoom_out.triggered.connect(self.zoom_out_clicked)
        self.restore_zoom.triggered.connect(self.restore_zoom_action_clicked)
        #end of View Menu
        #About Menu
        self.view_help_action.triggered.connect(self.help)
        self.send_feedback_action.triggered.connect(self.feedback)
        self.about_action.triggered.connect(self.about_PyQt5TfY)
        self.status_bar_action.triggered.connect(self.toggle_status_bar)

        md = QtGui.QGuiApplication.clipboard().mimeData()
        if md.hasFormat('text/plain'):
            self.paste_action.setEnabled(True)
        else:
            self.paste_action.setEnabled(False)

        self.printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.PrinterMode.HighResolution)

        QtGui.QGuiApplication.clipboard().dataChanged.connect(self.clipboard_data_changed)

        self.plain_text_edit.setFocus()
        self.set_current_file_name('')

    def readSettings(self):
        try: 
            self.settings.beginGroup("mainwindow")
            self.settings.value("size")
            self.settings.value("pos")
            self.settings.endGroup()
            self.settings.beginGroup("wordwrap")
            self.settings.value("checked")
            self.settings.endGroup()
            self.settings.beginGroup("statusbar")
            self.settings.value("checked")
            self.settings.endGroup()
        except:
            pass

    def writeSettings(self):
        self.settings.beginGroup("mainwindow")
        self.settings.setValue("size", self.size())
        self.settings.setValue("pos", self.pos())
        self.settings.endGroup()
        self.settings.beginGroup("wordwrap")
        self.settings.setValue("checked", self.word_wrap_action.isChecked())
        self.settings.endGroup()
        self.settings.beginGroup("statusbar")
        self.settings.setValue("checked", self.status_bar_action.isChecked())
        self.settings.endGroup()

    @QtCore.pyqtSlot()
    def file_new(self):
        if self.maybe_save():
            self.plain_text_edit.clear()
            self.set_current_file_name("")

    @QtCore.pyqtSlot()
    def file_new_window(self):
        self.writeSettings()
        self.new_window = MainWindow()
        self.new_window.show()

    def load(self, f):
        if not QtCore.QFile.exists(f):
            return False
        file = QtCore.QFile(f)
        if not file.open(QtCore.QFile.ReadOnly):
            return False
        data = file.readAll()
        db = QtCore.QMimeDatabase()
        mime_type_name = db.mimeTypeForFileNameAndData(f, data).name()
        if mime_type_name in MIME_TYPES:
            text = data.data().decode('utf8')
            self.plain_text_edit.setPlainText(text)
        else:
            pass
        self.set_current_file_name(f)
        return True

    @QtCore.pyqtSlot()
    def file_open(self):
        file_dialog = QtWidgets.QFileDialog(self, 
        caption="Open", 
        filter="Text Files (*.txt);; Python Files (*.py);; Json Files (*.json);; QML Files (*.qml)")
        file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptOpen)
        file_dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile)
        if file_dialog.exec() != QtWidgets.QDialog.DialogCode.Accepted:
            return
        fn = file_dialog.selectedFiles()[0]
        self.load(fn)

    def set_current_file_name(self, name):
        self.file_name = name
        self.plain_text_edit.document().setModified(False)
        if name:
            shown_name = QtCore.QFileInfo(name).fileName()         
        else:
            shown_name = "Untitled.txt"
        app_name = QtCore.QCoreApplication.applicationName()
        self.setWindowTitle(f"{shown_name}[*] - {app_name}")
        self.setWindowModified(False)

    def maybe_save(self):
        if not self.plain_text_edit.document().isModified():
            return True
        ret = QtWidgets.QMessageBox.warning(self, QtCore.QCoreApplication.applicationName(),
                                  "Do you want to save your changes to this document?",
                                  QtWidgets.QMessageBox.StandardButton.Save | QtWidgets.QMessageBox.StandardButton.Discard
                                  | QtWidgets.QMessageBox.StandardButton.Cancel)
        if ret == QtWidgets.QMessageBox.StandardButton.Save:
            return self.file_save()
        if ret == QtWidgets.QMessageBox.StandardButton.Cancel:
            return False
        return True

    @QtCore.pyqtSlot()
    def file_save(self):
        if not self.file_name or self.file_name.startswith(":/"):
            return self.file_save_as()
        writer = QtGui.QTextDocumentWriter(self.file_name)
        document = self.plain_text_edit.document()
        success = writer.write(document)
        native_file_name = QtCore.QDir.toNativeSeparators(self.file_name)
        if success:
            document.setModified(False)
            self.statusBar().showMessage(f'Wrote "{native_file_name}"')
        else:
            self.statusBar().showMessage(f'Could not write to file "{native_file_name}"')
        return success

    @QtCore.pyqtSlot()
    def file_save_as(self):
        file_dialog = QtWidgets.QFileDialog(self, "Save as...")
        file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptSave)
        mime_types = MIME_TYPES
        mime_types.insert(1, "application/vnd.oasis.opendocument.text")
        file_dialog.setMimeTypeFilters(mime_types)
        file_dialog.setDefaultSuffix("odt")
        if file_dialog.exec() != QtWidgets.QDialog.DialogCode.Accepted:
            return False

        fn = file_dialog.selectedFiles()[0]
        self.set_current_file_name(fn)
        return self.file_save()

    @QtCore.pyqtSlot()
    def file_print(self):
        dlg = QtPrintSupport.QPrintDialog(self.printer, self)
        if self.plain_text_edit.textCursor().hasSelection():
            dlg.setOption(QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.PrintSelection)
        dlg.setWindowTitle("Print Document")
        if dlg.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            self.plain_text_edit.print(self.printer)

    @QtCore.pyqtSlot()
    def file_page_setup(self):
        top = self.printer.pageLayout().margins().top()
        left = self.printer.pageLayout().margins().left()
        bottom = self.printer.pageLayout().margins().bottom()
        right = self.printer.pageLayout().margins().right()
        margins = QtCore.QMarginsF(left, top, right, bottom)
        page_setup = QtPrintSupport.QPageSetupDialog(self.printer, self)
        self.printer.setPageMargins(margins, QtGui.QPageLayout.Unit.Inch)
        page_setup.setContentsMargins(QtCore.QMargins(int(left), int(top), int(right), int(bottom))) 
        page_setup.exec()

    def closeEvent(self, event):
        if self.maybe_save():
            self.writeSettings()
            event.accept()
        else:
            event.ignore()

    def status_bar_modifier(self):
        new_row = self.plain_text_edit.textCursor().blockNumber() + 1
        new_col = self.plain_text_edit.textCursor().positionInBlock() + 1
        self.status_bar.showMessage(self.label_2.setText(f"Ln {new_row}, Col {new_col}"))

    def undo_changes(self):
        self.plain_text_edit.undo()

    @QtCore.pyqtSlot()
    def clipboard_data_changed(self):
        md = QtGui.QGuiApplication.clipboard().mimeData()
        if md.hasFormat('text/plain'):
            self.paste_action.setEnabled(md and md.hasText())
        else:
            self.paste_action.setEnabled(False)

    def delete_enabled(self):
        if self.plain_text_edit.textCursor().hasSelection():
            self.delete_action.setEnabled(True)
        else:
            self.delete_action.setEnabled(False)
    def delete_selection(self):
            self.plain_text_edit.textCursor().removeSelectedText()

    def search_bing_enabled(self):
        if self.plain_text_edit.textCursor().hasSelection():
            self.search_bing_action.setEnabled(True)
        else:
            self.search_bing_action.setEnabled(False)

    def search_bing(self):
        search_term = self.plain_text_edit.textCursor().selectedText()
        search_term = re.sub(r"\s+", '+', search_term)
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(f"https://www.bing.com/search?q={search_term}"))

    def show_find_dialog(self):
        self.find_dialog.show()
        self.text = self.find_dialog.line_edit.text()
        if self.plain_text_edit.textCursor().hasSelection():
            self.text = self.plain_text_edit.textCursor().selectedText()
            self.find_dialog.line_edit.setText(self.text)
            self.text = self.find_dialog.line_edit.text()
        else:
            pass
        if not self.find_dialog.line_edit.text():
            self.find_dialog.push_button.setEnabled(False)
        if self.find_dialog.line_edit.text():
            self.find_dialog.push_button.setEnabled(True)
        self.find_dialog.push_button.clicked.connect(self.check_to_find)
        self.find_dialog.line_edit.textChanged.connect(self.enable_find_on_find_dialog)
        self.find_dialog.push_button_2.clicked.connect(self.find_dialog.close)

    def enable_find_on_find_dialog(self):
        if not self.find_dialog.line_edit.text():
            self.find_dialog.push_button.setEnabled(False)
        if self.find_dialog.line_edit.text():
            self.text = self.find_dialog.line_edit.text()
            self.find_dialog.push_button.setEnabled(True)

    def find_actions_behavior(self):
        if not self.plain_text_edit.toPlainText():
            self.find_action.setEnabled(False)
            self.find_next_action.setEnabled(False)
            self.find_previous_action.setEnabled(False)
        if self.plain_text_edit.toPlainText():
            self.find_action.setEnabled(True)
            self.find_next_action.setEnabled(True)
            self.find_previous_action.setEnabled(True)

    def check_to_find(self):
        if self.text not in self.plain_text_edit.toPlainText():
            self.cannot_find()
        if self.text in self.plain_text_edit.toPlainText():
            self.find_text()
            self.activateWindow()

    def find_text(self):
        if self.find_dialog.radio_button.isChecked():
            result = self.plain_text_edit.find(self.text, 
            QtGui.QTextDocument.FindFlag.FindBackward)
            result
            if self.find_dialog.check_box_2.isChecked() and not result:
                self.plain_text_edit.moveCursor(QtGui.QTextCursor.MoveOperation.End)
                result
        if self.find_dialog.radio_button_2.isChecked():
            result = self.plain_text_edit.find(self.text)
            result
            if self.find_dialog.check_box_2.isChecked() and not result:
                self.plain_text_edit.moveCursor(QtGui.QTextCursor.MoveOperation.Start)
                result
        if self.find_dialog.radio_button.isChecked() and self.find_dialog.check_box.isChecked():
            result = self.plain_text_edit.find(self.text, 
            QtGui.QTextDocument.FindFlag.FindBackward | 
            QtGui.QTextDocument.FindFlag.FindCaseSensitively)
            result
            if self.find_dialog.check_box_2.isChecked() and not result:
                self.plain_text_edit.moveCursor(QtGui.QTextCursor.MoveOperation.End)
                result
        if self.find_dialog.radio_button_2.isChecked() and self.find_dialog.check_box.isChecked():
            result = self.plain_text_edit.find(self.text, QtGui.QTextDocument.FindFlag.FindCaseSensitively)
            result 
            if self.find_dialog.check_box_2.isChecked() and not result:
                self.plain_text_edit.moveCursor(QtGui.QTextCursor.MoveOperation.Start)
                result

    def cannot_find(self):
        msg = QtWidgets.QMessageBox(self.find_dialog)
        msg.setWindowTitle(QtCore.QCoreApplication.applicationName())
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText(f"Cannot find '{self.text}'")
        msg.exec()

    def find_next_word(self):
        text = self.find_dialog.line_edit.text()
        result = self.plain_text_edit.find(text)
        if text:
            if text in self.plain_text_edit.toPlainText():
                if result == False:
                    self.plain_text_edit.moveCursor(QtGui.QTextCursor.MoveOperation.Start)  
                if result == True:                
                    result                 
            if text not in self.plain_text_edit.toPlainText():
                self.cannot_find()
        if not text:
            self.show_find_dialog()

    def find_previous_word(self):
        text = self.find_dialog.line_edit.text()
        result = self.plain_text_edit.find(self.text, QtGui.QTextDocument.FindFlag.FindBackward)
        if text:
            if text in self.plain_text_edit.toPlainText():
                if result == False:
                    self.plain_text_edit.moveCursor(QtGui.QTextCursor.MoveOperation.End)  
                if result == True:                
                    result                
            if text not in self.plain_text_edit.toPlainText():
                self.cannot_find()
        if not text:
            self.show_find_dialog()

    def show_replace_dialog(self):
        self.replace_dialog.show()       
        if self.plain_text_edit.textCursor().hasSelection():
            text = self.plain_text_edit.textCursor().selectedText()
            self.replace_dialog.line_edit.setText(text)
        else:
            pass
        self.replace_dialog.line_edit.textChanged.connect(self.enable_replace_line_edit)
        self.replace_dialog.push_button.clicked.connect(self.find_to_replace)
        self.replace_dialog.push_button_2.clicked.connect(self.replace_text)
        self.replace_dialog.push_button_3.clicked.connect(self.replace_all_text)
        self.replace_dialog.push_button_4.clicked.connect(self.replace_dialog.close)    

    def enable_replace_line_edit(self):
        if not self.replace_dialog.line_edit.text():
            self.replace_dialog.push_button.setEnabled(False)
            self.replace_dialog.push_button_2.setEnabled(False)
            self.replace_dialog.push_button_3.setEnabled(False)
        if self.replace_dialog.line_edit.text():
            self.text = self.replace_dialog.line_edit.text()
            self.replace_dialog.push_button.setEnabled(True)
            self.replace_dialog.push_button_2.setEnabled(True)
            self.replace_dialog.push_button_3.setEnabled(True)

    def find_to_replace(self):
        text = self.replace_dialog.line_edit.text()
        result = self.plain_text_edit.find(text)    
        if text in self.plain_text_edit.toPlainText():
            if result == False:
                self.plain_text_edit.moveCursor(QtGui.QTextCursor.MoveOperation.Start)  
            if result == True:                
                result
                self.activateWindow()             
        if text not in self.plain_text_edit.toPlainText():
            self.cannot_replace()

    def replace_text(self):
        text = self.replace_dialog.line_edit.text()
        result = self.plain_text_edit.find(text)    
        if text in self.plain_text_edit.toPlainText():
            if result == False:
                self.plain_text_edit.moveCursor(QtGui.QTextCursor.MoveOperation.Start)  
            if result == True:                
                result
                self.activateWindow()
                if self.plain_text_edit.textCursor().hasSelection():
                    text = self.plain_text_edit.textCursor().selectedText()
                    replacing_text = self.replace_dialog.line_edit_2.text()
                    self.plain_text_edit.textCursor().selectedText().replace(text, replacing_text, -1)
                    self.plain_text_edit.textCursor().insertText(replacing_text)            
                else:
                    pass                
        if text not in self.plain_text_edit.toPlainText():
            self.cannot_replace()

    def cannot_replace(self):
        msg = QtWidgets.QMessageBox(self.replace_dialog)
        msg.setWindowTitle(QtCore.QCoreApplication.applicationName())
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        message = f"Cannot find '{self.text}'."
        msg.setText(message)
        msg.exec()

    def replace_all_text(self):     
        selected_text = self.replace_dialog.line_edit.text()
        replacing_text = self.replace_dialog.line_edit_2.text()
        all_texts = self.plain_text_edit.toPlainText().replace(selected_text, replacing_text, -1)
        self.plain_text_edit.setPlainText(all_texts)

    def go_to_word(self):
        if self.word_wrap_action.isChecked():
            self.go_to_action.setEnabled(False)
        else:
            self.go_to_action.setEnabled(True)
            self.block_count = self.plain_text_edit.document().blockCount()
            self.go_to_dialog.show()
            self.validator = QtGui.QIntValidator(1, self.block_count, self.go_to_dialog)
            self.go_to_dialog.line_edit.setValidator(self.validator)
            self.go_to_dialog.line_edit.setText(f"{self.validator.bottom()}")
            self.go_to_dialog.push_button.clicked.connect(self.go_to_clicked)
            self.go_to_dialog.push_button_2.clicked.connect(self.go_to_dialog.close)

    def go_to_clicked(self):
        line = int(self.go_to_dialog.line_edit.text())
        if line < 1 or line > self.block_count:
            self.go_to_warning()
        else:
            line = line-1
            text_cursor = QtGui.QTextCursor(self.plain_text_edit.document().findBlockByLineNumber(line))
            self.plain_text_edit.setTextCursor(text_cursor)
            self.go_to_dialog.close()

    def go_to_warning(self):
        msg = QtWidgets.QMessageBox(self.go_to_dialog)
        msg.resize(150,100)
        msg.setWindowTitle(QtCore.QCoreApplication.applicationName())
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        message = f"The line number is beyond the total number of lines."
        msg.setText(message)
        msg.exec()
        if QtWidgets.QMessageBox.Ok:
            return self.go_to_dialog.line_edit.setText(f"{self.validator.bottom()}")

    def set_time_date(self):
        time_date = QtCore.QDateTime.currentDateTime().toString()
        self.plain_text_edit.insertPlainText(f"{time_date}") 

    #Format Menu
    def word_wrap_action_clicked(self):
        if self.word_wrap_action.isChecked():
            self.plain_text_edit.setLineWrapMode(QtWidgets.QPlainTextEdit.LineWrapMode.WidgetWidth)  
            self.go_to_action.setEnabled(False)
        else:
            self.plain_text_edit.setLineWrapMode(QtWidgets.QPlainTextEdit.LineWrapMode.NoWrap)    
            self.go_to_action.setEnabled(True)

    def font_dialog(self):
        font, _ = QtWidgets.QFontDialog.getFont()
        if _:
            self.plain_text_edit.setFont(font)
    #end of Format Menu

    #View Menu
    def current_point_size(self):
        self.new_font =  self.plain_text_edit.font().pointSize()
        self.delta = (self.new_font/self.initial_font)*100

    def zoom_in_clicked(self):
        self.plain_text_edit.zoomIn(1)
        self.current_point_size()
        self.set_zoom_percentage()

    def zoom_out_clicked(self):
        self.plain_text_edit.zoomOut(1)
        self.current_point_size()
        self.set_zoom_percentage()

    def set_zoom_percentage(self):
        self.status_bar.children()[5].setText(f"{self.delta}%")

    def restore_zoom_action_clicked(self):
        font = QtGui.QFont()
        font.setPointSize(self.initial_font)
        self.plain_text_edit.setFont(font)
        self.status_bar.children()[5].setText("100.0%")

    def toggle_status_bar(self):
        try: 
            if self.status_bar.isVisible():
                self.status_bar.hide()
                self.status_bar_action.setChecked(False)
            else:
                self.status_bar.show()
                self.status_bar_action.setChecked(True)
        except Exception as e:
            print(repr(e))
    #enf of View Menu

    #About Menu
    def help(self):
        search_term = "get help with notepad in windows"
        search_term = re.sub(r"\s+", '+', search_term)
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(f"https://www.bing.com/search?q={search_term}"))

    def feedback(self):
        os.system("start feedback-hub:")
    
    def about_PyQt5TfY(self):
        self.about_message.exec()
 
if __name__ == '__main__':
    app = QtWidgets.QApplication([]) 
    app.setApplicationDisplayName('Notepad Clone')
    ui = MainWindow()
    ui.show() 
    app.exec()