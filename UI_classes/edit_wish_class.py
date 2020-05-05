from PyQt5.QtGui import QIcon, QPixmap
from mysql.connector import errors

from UI_classes.add_wish_class import AddWish


class EditWish(AddWish):
	def __init__(self, parent, doc_root, db_connector, _item_index, list_type):
		super().__init__(parent, doc_root, db_connector)
		self.parent = parent
		self.db_conn = db_connector
		self.item_index = _item_index
		self.list_type = list_type
		self.setWindowTitle('Edit Wish')
		self.ui.edit_wish_btn = self.ui.add_wish_btn

		self.ui.edit_wish_btn.setText('Изменить')
		self.ui.edit_wish_btn.setIcon(QIcon(QPixmap('{}assets/icons/edit-icon.svg'.format(self.doc_root))))

		self.ui.edit_wish_btn.clicked.connect(self.commit_changes)

		if self.list_type == 'active_wishes':
			self.ui.wish_name.setPlainText(self.parent.active_wishes_list.
										   itemAt(self.item_index).layout().
										   itemAt(0).layout().itemAt(0).widget().text())
			self.ui.wish_price.setPlainText(self.parent.active_wishes_list.
										   itemAt(self.item_index).layout().
										   itemAt(1).layout().itemAt(1).widget().text())
			self.ui.wish_url.setPlainText(self.parent.active_wishes_list.
										   itemAt(self.item_index).layout().
										   itemAt(1).layout().itemAt(3).widget().text())
			self.ui.wish_description.setPlainText(self.parent.active_wishes_list.
										   itemAt(self.item_index).layout().
										   itemAt(1).layout().itemAt(5).widget().text())
		else:
			self.ui.wish_name.setPlainText(self.parent.executed_wishes_list.
										   itemAt(self.item_index).layout().
										   itemAt(0).layout().itemAt(0).widget().text())
			self.ui.wish_price.setPlainText(self.parent.executed_wishes_list.
										   itemAt(self.item_index).layout().
										   itemAt(1).layout().itemAt(1).widget().text())
			self.ui.wish_url.setPlainText(self.parent.executed_wishes_list.
										   itemAt(self.item_index).layout().
										   itemAt(1).layout().itemAt(3).widget().text())
			self.ui.wish_description.setPlainText(self.parent.executed_wishes_list.
										   itemAt(self.item_index).layout().
										   itemAt(1).layout().itemAt(5).widget().text())

	def commit_changes(self):
		new_values = []
		new_values.append(self.ui.wish_name.toPlainText())

		if len(self.ui.wish_price.toPlainText()) == 0:
			self.ui.wish_price.setPlainText('0')

		new_values.append(self.ui.wish_price.toPlainText())
		new_values.append(self.ui.wish_url.toPlainText())
		new_values.append(self.ui.wish_description.toPlainText())

		row_id = 0
		if self.list_type == 'active_wishes':
			row_id = self.parent.active_wishes_mapping[self.item_index]
		else:
			row_id = self.parent.executed_wishes_mapping[self.item_index]

		cursor = self.db_conn.cursor()
		try:
			cursor.execute("update wish set "
						   "name = '{}',"
						   "price = '{}',"
						   " link = '{}',"
						   " description = '{}'"
						   " where _id={}".format(new_values[0], new_values[1], new_values[2], new_values[3], row_id))

			if self.list_type == 'active_wishes':
				self.parent.alter_list_item(self.parent.active_wishes_list, self.item_index, new_values)
			else:
				self.parent.alter_list_item(self.parent.executed_wishes_list, self.item_index, new_values)

		except errors.Error as er:
			return

		self.db_conn.commit()
		cursor.close()
		self.enable_parent()
		self.destroy(True, True)
