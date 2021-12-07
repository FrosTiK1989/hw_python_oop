class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                training_type: str,
                duration: float,
                distance: float,
                speed: float,
                calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories
    def get_message() -> str:
        return (f'Тип тренировки: {training_type}; Длительность: {duration:.3f} ч.; '
                f'Дистанция: {distance:.3f} км; Ср. скорость: {speed:.3f} км/ч; '
                f'Потрачено ккал: {calories:.3f}.')


class Training:
    """Базовый класс тренировки."""
    M_IN_KM = 1000
    LEN_STEP = 0.65

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.distance / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        get_spent_calories()

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        show_training_info()


class Running(Training):
    """Тренировка: бег."""
    def __init__(self, action: int, duration: float, weight: float) -> None:
        super().__init__(action, duration, weight)
        cf_cal_1 = 18
        cf_cal_2 = 20
        return ((cf_cal_1 * self.get_mean_speed() - cf_cal_2) * self.weight / 
                (self.M_IN_KM * self.duration) * 60)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    pass


class Swimming(Training):
    """Тренировка: плавание."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

