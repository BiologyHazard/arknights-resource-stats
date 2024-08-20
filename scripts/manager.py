import sys
from collections.abc import Callable, Iterable
from typing import Literal

sys.path.append(r".")
from models import ItemInfoList  # NOQA: E402
from time_utils import DateTimeLike  # NOQA: E402

type Line = tuple[ItemInfoList, str, DateTimeLike | str, list[str], int, Literal[1, 2, 6]]
type RegisterType = Callable[[], Iterable[Line]]


class Manager(list):
    def register[T: RegisterType](self, function: T) -> T:
        self.append(function)
        return function


manager = Manager()
