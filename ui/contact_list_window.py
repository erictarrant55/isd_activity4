"""The module defines the ContactListWindow class."""
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem

from ui.base.main_window import MainWindow
__author__ = "Eric Tarrant"
__version__ = "1.0.0"

class ContactListWindow(MainWindow):

    def __init__(self) -> None:
        """Initializes the ContactListWindow class."""
        super().__init__()
        self.setWindowTitle("Contact List")
        self.__initialize_widgets()
    
    def __initialize_widgets(self) -> None:
        """Init the widgets in the window"""

        self._name_line_edit.setPlaceholderText("Contact name")

        self._phone_line_edit.setInputMask("(000) 000-0000;_")

        self._add_button.setDefault(True)
        self._add_button.setEnabled(False)

        self._remove_button.setEnabled(False)

        self._name_line_edit.textChanged.connect(self._on_input_changed)
        self._phone_line_edit.textChanged.connect(self._on_input_changed)

        self._add_button.clicked.connect(self.__on_add_button_clicked)
        self._contact_table.itemSelectionChanged.connect(
            self.__on_table_selection_changed)
    
    self._remove_button.clicked.connect(self.__on_remove_button_clicked)

    @Slot()
    def __get_select_row(self) -> int:
        """Returns the index of the selected row in the contact table.

        Returns:
            int: The index of the selected row, or -1 if no row is selected.
        """
        selected_items = self._contact_table.selectedItems()
        if not selected_items:
            return -1
        return selected_items[0].row()

    def __on_input_changed(self) -> None:
        """Enables or disables the add button based on the input."""
        name = self._name_line_edit.text().strip()
        phone = self._phone_line_edit.text().strip()
        self._add_button.setEnabled(name_is_valid and phone_is_valid)

    @Slot()
    def __on_add_button_clicked(self) -> None:

    @Slot()
    def _on_table_selection_changed(self) -> None:
        self._remove_button.setEnabled(self.__get_selected_row() is not None)

    @Slot()
    def __on_remove_button_clicked(self) -> None: