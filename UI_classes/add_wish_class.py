from PyQt5.QtGui import QColor, QIcon, QPixmap
from PyQt5.QtWidgets import QDialog, QGraphicsDropShadowEffect

from UI_classes.add_wish_abstract_class import Ui_Dialog
from UI_classes.custom_base import CustomBase


class AddWish(QDialog, CustomBase):
	def __init__(self, parent, doc_root, db_connector):
		super().__init__(parent)
		CustomBase().__init__()

		self.parent = parent
		self.doc_root = doc_root
		self.db_conn = db_connector
		self.parent.setEnabled(False)
		self.setEnabled(True)

		self.ui = Ui_Dialog()
		self.ui.setupUi(self)

		self.ui.add_wish_btn.setIcon(QIcon(QPixmap('{}assets/icons/add-icon.svg'.format(self.doc_root))))
		self.ui.add_wish_btn.setFont(self.buttons_font)
		shadow = QGraphicsDropShadowEffect()
		shadow.setColor(QColor(0, 0, 0, 255 * 0.5))
		shadow.setBlurRadius(15)
		shadow.setOffset(0)
		self.ui.add_wish_btn.setGraphicsEffect(shadow)

		self.ui.add_wish_btn.clicked.connect(self.commit_changes)

	def commit_changes(self):
		new_values = []
		new_values.append(self.ui.wish_name.toPlainText())

		if len(self.ui.wish_price.toPlainText()) == 0:
			self.ui.wish_price.setPlainText('0')

		new_values.append(self.ui.wish_price.toPlainText())
		new_values.append(self.ui.wish_url.toPlainText())
		new_values.append(self.ui.wish_description.toPlainText())

		cursor = self.db_conn.cursor()

		try:
			cursor.execute("insert into wish values(default, '{}', '{}', '{}', '{}', default)"
						   .format(new_values[0], new_values[1], new_values[2], new_values[3]))

			self.db_conn.commit()
			row_id = cursor.lastrowid
			cursor.close()

			self.parent.append_list_item(self.parent.active_wishes_list, new_values, self.parent.ACTIVE)
			self.parent.active_wishes_mapping[self.parent.active_wishes_list.count() - 1] = row_id

		except Exception as err:
			print(err)
			return

		self.enable_parent()
		self.destroy(True, True)

	def enable_parent(self):
		self.parent.setEnabled(True)
		self.parent.do_unblur(100, 4)
