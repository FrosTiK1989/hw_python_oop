from dataclasses import asdict, dataclass
from typing import Dict, Type


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    MESSAGE = (
        "Тип тренировки: {training_type}; "
        "Длительность: {duration:.3f} ч.; "
        "Дистанция: {distance:.3f} км; "
        "Ср. скорость: {speed:.3f} км/ч; "
        "Потрачено ккал: {calories:.3f}."
    )

    def get_message(self) -> str:
        return self.MESSAGE.format(**asdict(self))


@dataclass
class Training:
    """Базовый класс тренировки."""

    action: int
    duration: float
    weight: float

    M_IN_KM = 1000
    LEN_STEP = 0.65
    MIN_IN_HR = 60

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError(
            f"Необходимо реализовать метод get_spent_calories в классе {type(self).__name__}"
        )

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(
            training_type=type(self).__name__,
            duration=self.duration,
            distance=self.get_distance(),
            speed=self.get_mean_speed(),
            calories=self.get_spent_calories(),
        )


@dataclass
class Running(Training):
    """Тренировка: бег."""

    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 20

    def get_spent_calories(self):
        return (
            (
                self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed()
                - self.CALORIES_MEAN_SPEED_SHIFT
            )
            * self.weight
            / self.M_IN_KM
            * (self.duration)
            * self.MIN_IN_HR
        )


@dataclass
class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    height: float

    CALORIES_WEIGHT_MULTIPLIER = 0.035
    CALORIES_HEIGHT_MULTIPLIER = 0.029

    def get_spent_calories(self) -> float:
        return (
            self.CALORIES_WEIGHT_MULTIPLIER * self.weight
            + (self.get_mean_speed() ** 2 // self.height)
            * self.CALORIES_HEIGHT_MULTIPLIER
            * self.weight
        ) * (self.duration * self.MIN_IN_HR)


@dataclass
class Swimming(Training):
    """Тренировка: плавание."""

    length_pool: float
    count_pool: float

    LEN_STEP = 1.38
    CALORIES_MEAN_SPEED_PLUS = 1.1

    def get_mean_speed(self) -> float:
        return (
            self.length_pool * self.count_pool / self.M_IN_KM / self.duration
        )

    def get_spent_calories(self) -> float:
        return (
            (self.get_mean_speed() + self.CALORIES_MEAN_SPEED_PLUS)
            * 2
            * self.weight
        )


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    workout: Dict[str, Type[Training]] = {
        "SWM": Swimming,
        "RUN": Running,
        "WLK": SportsWalking,
    }
    if workout_type not in workout:
        raise ValueError("Нет такой тренировки.")
    return workout[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(InfoMessage.get_message(info))


if __name__ == "__main__":
    packages = [
        ("SWM", [720, 1, 80, 25, 40]),
        ("RUN", [15000, 1, 75]),
        ("WLK", [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
