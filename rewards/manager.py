from collections.abc import Callable

from models import ResourceStats

type RegisterType = Callable[[ResourceStats], None]


class Manager(list[RegisterType]):
    def register[T: RegisterType](self, function: T) -> T:
        self.append(function)
        return function


manager = Manager()
