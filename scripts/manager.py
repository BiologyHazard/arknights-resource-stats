import sys
from collections.abc import Callable, Iterable
from typing import Literal, NamedTuple

sys.path.append(r".")
from models import ItemInfoList  # NOQA: E402
from time_utils import DateTimeLike  # NOQA: E402

type Line = tuple[ItemInfoList, str, DateTimeLike | str, list[str], int, Literal[1, 2, 6]]
type RegisterType = Callable[[], Iterable[Line]]


class FunctionInfo(NamedTuple):
    function: RegisterType
    file_name: str
    function_name: str
    import_str: str
    comments: str = ""


class Manager(list[FunctionInfo]):
    def register[T: RegisterType](self,
                                  file_name: str,
                                  function_name: str,
                                  import_str: str,
                                  comments: str = "") -> Callable[[T], T]:
        def wrapper(function: T) -> T:
            self.append(FunctionInfo(function, file_name, function_name, import_str, comments))
            return function

        return wrapper


manager = Manager()

# if __name__ == "__main__":
#     @manager.register(
#         file_name="zone_record",
#         function_name="add_zone_record_resources",
#         import_str="from models import ResourceStats",
#     )
#     def f() -> Iterable[Line]:
#         yield ItemInfoList(), "", "", [], 0, 1
#     print(manager)
