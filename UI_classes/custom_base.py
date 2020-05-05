from PyQt5.QtCore import pyqtProperty, QPropertyAnimation, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGraphicsBlurEffect


class CustomBase:
	def __init__(self):
		self.wish_name_font = QFont()
		self.wish_name_font.setFamily("Yu Gothic UI Semibold")
		self.wish_name_font.setPointSize(14)
		self.wish_name_font.setBold(True)
		self.wish_name_font.setWeight(75)
		self.wish_name_font.setLetterSpacing(QFont.AbsoluteSpacing, 2)

		self.wish_fields_font = QFont()
		self.wish_fields_font.setFamily("Yu Gothic UI Light")
		self.wish_fields_font.setPointSize(13)
		self.wish_fields_font.setBold(False)
		self.wish_fields_font.setWeight(50)
		self.wish_fields_font.setLetterSpacing(QFont.AbsoluteSpacing, 1)

		self.buttons_font = QFont()
		self.buttons_font.setFamily("Yu Gothic UI Semibold")
		self.buttons_font.setPointSize(14)
		self.buttons_font.setBold(True)
		self.buttons_font.setWeight(75)
		self.buttons_font.setLetterSpacing(QFont.AbsoluteSpacing, 1)

	def _set_blur(self, value):
		blur = QGraphicsBlurEffect()
		blur.setBlurRadius(value)
		self.setGraphicsEffect(blur)

	blur = pyqtProperty(float, fset=_set_blur)

	def do_blur(self, dur, value):
		self.anim = QPropertyAnimation(self, b'blur')
		self.anim.setDuration(dur)
		self.anim.setStartValue(1)
		self.anim.setEndValue(value)
		self.anim.start()

	def do_unblur(self, dur, value):
		self.anim = QPropertyAnimation(self, b'blur')
		self.anim.setDuration(dur)
		self.anim.setStartValue(value)
		self.anim.setEndValue(1)
		self.anim.start()

	def do_slide_in_animation(self, duration, h):
		self.anim = QPropertyAnimation(self, b'geometry')
		self.anim.setDuration(duration)
		self.anim.setStartValue(QRect(self.frameGeometry().left(),
									  self.frameGeometry().top() - h,
									  self.frameGeometry().width(),
									  self.frameGeometry().height()))

		self.anim.setEndValue(QRect(self.frameGeometry().left(),
									  self.frameGeometry().top(),
									  self.frameGeometry().width(),
									  self.frameGeometry().height()))
		self.anim.start()

	def do_slide_out_animation(self, duration, h):
		self.anim = QPropertyAnimation(self, b'geometry')
		self.anim.setDuration(duration)
		self.anim.setStartValue(QRect(self.frameGeometry().left(),
									  self.frameGeometry().top(),
									  self.frameGeometry().width(),
									  self.frameGeometry().height()))

		self.anim.setEndValue(QRect(self.frameGeometry().left(),
									self.frameGeometry().top() + h,
									self.frameGeometry().width(),
									self.frameGeometry().height()))
		self.anim.start()
