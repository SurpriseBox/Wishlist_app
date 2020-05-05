from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap, QColor
from PyQt5.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QLabel, QSizePolicy, QVBoxLayout, QGridLayout, \
	QHBoxLayout, QPushButton, QMessageBox
from mysql.connector import errors

from UI_classes.add_wish_class import AddWish
from UI_classes.custom_base import CustomBase
from UI_classes.edit_wish_class import EditWish
from UI_classes.main_window_abstract_class import Ui_MainWindow


class MainWindow(QMainWindow, CustomBase):
	def __init__(self, doc_root, db_connector):
		super().__init__()
		CustomBase().__init__()

		self.doc_root = doc_root
		self.db_conn = db_connector

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.active_wishes_list = self.ui.wish_list.layout()
		self.executed_wishes_list = self.ui.executed_wish_list.layout()

		self.active_wishes_mapping = {}
		self.executed_wishes_mapping = {}

		self.ACTIVE = 'active_wishes'
		self.EXECUTED = 'executed_wishes'

		self.ui.scrollArea.setStyleSheet("QScrollArea { border: 0px; }")
		self.ui.scrollArea_2.setStyleSheet("QScrollArea { border: 0px; }")
		self.ui.add_wish_btn.setIcon(QIcon(QPixmap('{}assets/icons/add-icon.svg'.format(self.doc_root))))
		self.ui.add_wish_btn.setIconSize(QSize(40, 40))
		self.ui.add_wish_btn.setFont(self.buttons_font)

		shadow = QGraphicsDropShadowEffect()
		shadow.setColor(QColor(0,0,0, 255*0.5))
		shadow.setBlurRadius(15)
		shadow.setOffset(0)
		self.ui.add_wish_btn.setGraphicsEffect(shadow)

		self.init_wishes_list(self.ACTIVE)
		self.init_wishes_list(self.EXECUTED)

	def init_wishes_list(self, list_type):
		if list_type == 'active_wishes':
			query = "select _id, name, price, link, description, is_executed from wish where is_executed=0"
			map = self.active_wishes_mapping
			layout = self.active_wishes_list
		else:
			query = "select _id, name, price, link, description, is_executed from wish where is_executed=1"
			map = self.executed_wishes_mapping
			layout = self.executed_wishes_list

		cursor = self.db_conn.cursor()
		cursor.execute(query)
		row = cursor.fetchone()
		i = 0
		while row is not None:
			map[i] = int(row[0])
			self.append_list_item(layout, row[1:5], list_type)
			row = cursor.fetchone()
			i += 1
		cursor.close()

	def append_list_item(self, _list, row, list_type):
		if list_type != 'active_wishes' and list_type != 'executed_wishes':
			return

		item = QVBoxLayout()

		header = QHBoxLayout()
		header.setContentsMargins(0, 0, 0, 0)
		header.setSpacing(0)

		wish_name = QLabel(str(row[0]))
		wish_name.setMinimumSize(QSize(1, 40))
		wish_name.setMaximumSize(QSize(10000, 40))
		wish_name.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
		wish_name.setContentsMargins(20, 0, 0, 0)
		wish_name.setStyleSheet("QLabel {background-color: #e9e9e9;"
								"			border-radius: 1px;}")
		wish_name.setFont(self.wish_name_font)
		header.addWidget(wish_name)

		if list_type == 'active_wishes':
			icons_set = ('executed-icon.ico', 'edit-icon.svg', 'delete-icon.svg')
			tool_tips_set = ('Пометить как исполненное', 'Изменить', 'Удалить желание')
			buttons_set = (QPushButton(), QPushButton(), QPushButton())
		else:
			icons_set = ('edit-icon.svg', 'delete-icon.svg')
			tool_tips_set = ('Изменить', 'Удалить желание')
			buttons_set = (QPushButton(), QPushButton())

		for i in range(len(buttons_set)):
			icon = QPixmap('{}assets/icons/{}'.format(self.doc_root, icons_set[i]))
			buttons_set[i].setIcon(QIcon(icon))
			buttons_set[i].setIconSize(QSize(20, 20))
			buttons_set[i].setMinimumSize(QSize(40, 40))
			buttons_set[i].setMaximumSize(QSize(40, 40))
			buttons_set[i].setStyleSheet("QPushButton {background-color: #e9e9e9 ;"
									  "				border: 0px;}"
									  "QPushButton:hover {background-color: #fff ;}")
			buttons_set[i].setToolTip(tool_tips_set[i])
			header.addWidget(buttons_set[i])

		item.addLayout(header)

		fields_grid = QGridLayout()
		fields_grid.setContentsMargins(20, 0, 0, 0)
		fields_grid.setHorizontalSpacing(10)

		icons_set = ('price-icon.ico', 'link-icon.svg', 'comment-icon.svg')
		for i in range(1, len(row)):
			icon = QPixmap('{}assets/icons/{}'.format(self.doc_root, icons_set[i - 1]))
			icon = icon.scaled(16, 16, Qt.KeepAspectRatio)
			field_icon = QLabel()
			field_icon.setPixmap(icon)
			field_icon.setMinimumSize(QSize(50, 50))
			field_icon.setMaximumSize(QSize(50, 50))
			fields_grid.addWidget(field_icon, i, 0, 1, 1)

			field_content = QLabel(str(row[i]))
			field_content.setMinimumSize(QSize(1, 50))
			field_content.setMaximumSize(QSize(10000, 50))
			field_content.setFont(self.wish_fields_font)
			field_content.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
			field_content.setContentsMargins(0, 0, 0, 0)
			fields_grid.addWidget(field_content, i, 1, 1, 1)

		item.addLayout(fields_grid)

		_list.addLayout(item)
		cur_item_index = _list.count() - 1

		if list_type == 'active_wishes':
			buttons_set[0].pressed.connect(lambda: self.move_wish_to_executed(cur_item_index))
			buttons_set[1].pressed.connect(lambda: self.open_EditWish_window(cur_item_index, list_type))
			buttons_set[2].pressed.connect(lambda: self.delete_wish_from_db(cur_item_index, list_type))
		else:
			buttons_set[0].pressed.connect(lambda: self.open_EditWish_window(cur_item_index, list_type))
			buttons_set[1].pressed.connect(lambda: self.delete_wish_from_db(cur_item_index, list_type))

	def alter_list_item(self, _list, _item_index, _new_row):
		item_layout = _list.itemAt(_item_index).layout()

		item_layout.itemAt(0).layout().itemAt(0).widget().setText(str(_new_row[0]))
		item_layout.itemAt(1).layout().itemAt(1).widget().setText(str(_new_row[1]))
		item_layout.itemAt(1).layout().itemAt(3).widget().setText(str(_new_row[2]))
		item_layout.itemAt(1).layout().itemAt(5).widget().setText(str(_new_row[3]))

	def delete_list_item(self, _list, _item_index):
		item_layout = _list.itemAt(_item_index).layout()
		for j in range(item_layout.count()):
			for i in range(item_layout.itemAt(j).layout().count()):
				item_layout.itemAt(j).layout().itemAt(i).widget().hide()

	def move_wish_to_executed(self, _item_index):
		mb = QMessageBox.question(self, 'Подтверждение действия', 'Пометить желание как исполненное?', QMessageBox.Yes | QMessageBox.No)
		if mb == QMessageBox.No:
			return

		cursor = self.db_conn.cursor()
		try:
			cursor.execute("select name, price, link, description from wish where _id={}".format(self.active_wishes_mapping[_item_index]))
			row = cursor.fetchone()
			cursor.execute("update wish set is_executed = 1 where _id={}".format(self.active_wishes_mapping[_item_index]))

			self.delete_list_item(self.active_wishes_list, _item_index)
			self.append_list_item(self.executed_wishes_list, row, self.EXECUTED)
			self.executed_wishes_mapping[self.executed_wishes_list.count() - 1] = self.active_wishes_mapping[_item_index]
		except errors.Error:
			pass

		self.db_conn.commit()
		cursor.close()

	def delete_wish_from_db(self, _item_index, list_type):
		mb = QMessageBox.question(self, 'Подтверждение действия', 'Удалить желание?',
								  QMessageBox.Yes | QMessageBox.No)
		if mb == QMessageBox.No:
			return

		cursor = self.db_conn.cursor()
		if list_type == 'active_wishes':
			row_id = self.active_wishes_mapping[_item_index]
			self.delete_list_item(self.active_wishes_list, _item_index)
			try:
				cursor.execute("delete from wish where _id={}".format(row_id))
			except errors.Error:
				QMessageBox.information(self, 'Ошибка удаления', 'При удалении возникла ошибка', QMessageBox.Ok)

		else:
			row_id = self.executed_wishes_mapping[_item_index]
			self.delete_list_item(self.executed_wishes_list, _item_index)
			try:
				cursor.execute("delete from wish where _id={}".format(row_id))
			except errors.Error:
				QMessageBox.information(self, 'Ошибка удаления', 'При удалении возникла ошибка', QMessageBox.Ok)

		self.db_conn.commit()
		cursor.close()

	def open_AddWish_window(self):
		self.do_blur(100, 4)
		w = AddWish(self, self.doc_root, self.db_conn)
		w.show()
		w.do_slide_in_animation(100, 150)

	def open_EditWish_window(self, _item_index, list_type):
		self.do_blur(100, 4)
		w = EditWish(self, self.doc_root, self.db_conn, _item_index, list_type)
		w.show()
		w.do_slide_in_animation(100, 150)
