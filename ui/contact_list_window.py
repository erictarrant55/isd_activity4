"""The module defines the ContactListWindow class."""
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
 
from ui.base.main_window import MainWindow
 
__author__ = "Eric Tarrant"
__version__ = "1.0.0"
 
 
class ContactListWindow(MainWindow):
    """Represents a window for a list of phone contacts."""
 
    def __init__(self) -> None:
        """Initializes the ContactListWindow class."""
 
        super().__init__()
 
        self.setWindowTitle("Contact Manager")
 
        self.__initialize_widgets()
 
    def __initialize_widgets(self) -> None:
        """Init the widgets in the window."""
 
        self._name_line_edit.setPlaceholderText("Contact Name")
 
        self._phone_line_edit.setInputMask("(000) 000-0000;_")
 
        self._add_button.setDefault(True)
        self._add_button.setEnabled(False)
 
        self._remove_button.setEnabled(False)
 
        self._name_line_edit.textChanged.connect(self.__on_input_changed)
        self._phone_line_edit.textChanged.connect(self.__on_input_changed)
 
        self._add_button.clicked.connect(self.__on_add_button_clicked)
        self._contact_table.itemSelectionChanged.connect(
            self.__on_table_selection_changed)
 
        self._remove_button.clicked.connect(self.__on_remove_button_clicked)
 
    def __get_selected_row(self) -> None:
        """Returns the selected row in the contact table.
 
        Returns:
            None: The selected row, or None if no row is selected.
        """
 
        selected_items = self._contact_table.selectedItems()
 
        if not selected_items:
            return None
 
        return selected_items[0].row()
 
    @Slot()
    def __on_input_changed(self) -> None:
        """
        Represents a function that enables or disables the add button based 
        on the input.
        """
 
        name_is_valid = self._name_line_edit.text().strip() != ""
        phone_is_valid = self._phone_line_edit.hasAcceptableInput()
 
        self._add_button.setEnabled(name_is_valid and phone_is_valid)
 
    @Slot()
    def __on_add_button_clicked(self) -> None:
        """
        Represents a function that handles the clicked event of the add button.
        """
 
        row = self._contact_table.rowCount()
        self._contact_table.insertRow(row)
 
        self._contact_table.setItem(
            row, 0, QTableWidgetItem(self._name_line_edit.text().strip()))
        self._contact_table.setItem(
            row, 1, QTableWidgetItem(self._phone_line_edit.text()))
 
        self._name_line_edit.clear()
        self._phone_line_edit.clear()
        self._name_line_edit.setFocus()
 
    @Slot()
    def __on_table_selection_changed(self) -> None:
        """
        Represents a function that handles the item 
        selection changed event of the table.
        """
 
        self._remove_button.setEnabled(self.__get_selected_row() is not None)
 
    @Slot()
    def __on_remove_button_clicked(self) -> None:
        """
        Represents a function that handles the clicked 
        event of the remove button.
        """
 
        row = self.__get_selected_row()
 
        if row is None:
            return
 
        name = self._contact_table.item(row, 0).text()
 
        message_box = QMessageBox(self)
        message_box.setWindowTitle("Remove Contact")
        message_box.setIcon(QMessageBox.Icon.Question)
        message_box.setText(f"Do you want to remove the contact {name}?")
        message_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        message_box.setDefaultButton(QMessageBox.StandardButton.No)
 
        if message_box.exec() == QMessageBox.StandardButton.Yes:
            self._contact_table.removeRow(row)