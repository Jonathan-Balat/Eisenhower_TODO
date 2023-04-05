from PySide2.QtCore import QPropertyAnimation, QEasingCurve


class AnimatorClass:

    def __init__(self, app_session):
        self.app_session = app_session
        self.animator = None  # Variable for setting animator instance

    def animation_handler(self, target, property, start_value, end_value,
                          curve_type=QEasingCurve.BezierSpline, duration=250):
        self.animator = QPropertyAnimation(target, property, target.parent())

        self.animator.setDuration(duration)
        self.animator.setStartValue(start_value)
        self.animator.setEndValue(end_value)
        self.animator.setEasingCurve(curve_type)
        self.animator.start()

