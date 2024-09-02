# ruff: noqa: E721, E501, PLR2004, PLR0912, PLR0915
from dataclasses import MISSING, Field, asdict, dataclass, fields, is_dataclass
from typing import Any, Callable, ClassVar, Union, get_args, get_origin


@dataclass
class Serializable:
    """A base class for serializable dataclasses.

    It compiles (optional) the serialization and deserialization code into class functions to make it faster.
    """

    _schema: ClassVar[dict[str, Field]]
    _map: ClassVar[dict[str, type]]

    _serialize_fn: ClassVar[Callable[[Any], dict[str, Any]]]
    _deserialize_fn: ClassVar[Callable[[type, dict[str, Any]], Any]]

    def __init_subclass__(cls, /, **kwargs) -> None:
        """Meta class for making dataclasses serializable."""
        cls = dataclass(cls)  # noqa: PLW0642

        # Create a schema with field names and types, including inherited fields.
        cls._schema = {}
        for base in cls.__mro__:  # type: ignore
            # Iterate over all base classes from children to parents.
            if is_dataclass(base):
                for field in fields(base):
                    # Let child classes override fields of parent classes.
                    if field.name in cls._schema:
                        continue

                    cls._schema.update({field.name: field})

        # Automatically generate __slots__ based on dataclass fields.
        if "__slots__" not in cls.__dict__:
            cls.__slots__ = tuple(cls._schema.keys())  # type: ignore

        # Generate custom serialization and deserialization code and compile it into a class function.
        serializer: list[str] = ["def _serialize_fn(instance):", "    result = {}"]
        deserializer: list[str] = ["def _deserialize_fn(cls, data):", "    result = {}"]

        # Iterate over schema, build types map and generate serialization & deserialization code.
        cls._map = {}
        for name, field in cls._schema.items():
            ftype: type = field.type  # type: ignore

            origin: type | None = get_origin(ftype)
            args: tuple[type, ...] = get_args(ftype)

            is_optional: bool = origin == Union and len(args) == 2 and args[1] == type(None)
            if is_optional:
                ftype = args[0]

            _default_value = "None" if field.default == MISSING else repr(field.default)

            if_nested_dataclass: bool = False
            if origin and origin in {list, set, tuple}:
                cls._map[name] = origin
                if is_dataclass(args[0]):
                    if_nested_dataclass = True
                    cls._map[name] = args[0]
                if _default_value == MISSING:
                    _default_value = "[]"
            elif origin and origin == dict:
                cls._map[name] = origin
                if is_dataclass(args[1]):
                    if_nested_dataclass = True
                    cls._map[name] = args[1]
                if _default_value == MISSING:
                    _default_value = "{}"
            else:
                cls._map[name] = ftype

            _sopt: str = f" if instance.{name} is not None else None" if is_optional else ""
            _def: str = f" if ('{name}' in data and data['{name}'] is not None) else {_default_value}"
            _debug: str = f"    print('Field: {name}, {origin.__name__ if origin else 'None'} - {ftype.__name__}', is_dataclass({ftype.__name__}))\n"

            _serialize: str = f"    result['{name}'] = "
            _deserialize: str = f"    result['{name}'] = "

            if is_dataclass(ftype):
                _serialize += f"instance.{name}.serialize()" + _sopt
                _deserialize += f"cls._map['{name}'].deserialize(data['{name}'])" + _def
            elif if_nested_dataclass and origin and origin in {list, set, tuple}:
                _serialize += f"{origin.__name__}(item.serialize() for item in instance.{name})" + _sopt
                _deserialize += f"{origin.__name__}(cls._map['{name}'].deserialize(item) for item in data['{name}'])" + _def
            elif if_nested_dataclass and origin and origin == dict:
                _serialize += f"{{k: v.serialize() for k, v in instance.{name}.items()}}" + _sopt
                _deserialize += f"{{k: cls._map['{name}'].deserialize(v) for k, v in data['{name}'].items()}}" + _def
            else:
                _serialize += f"instance.{name}" + _sopt
                _deserialize += f"cls._map['{name}'](data['{name}'])" + _def

            serializer.append(_serialize)
            deserializer.append(_deserialize)

        serializer.append("    return result")
        deserializer.append("    return cls(**result)")

        exec("\n".join(serializer), globals(), locals())  # noqa: S102
        cls._serialize_fn = locals()["_serialize_fn"]

        exec("\n".join(deserializer), globals(), locals())  # noqa: S102
        cls._deserialize_fn = locals()["_deserialize_fn"]

    def serialize(self) -> dict[str, Any]:
        """Serialize the dataclass into a dictionary with Python types.

        Returns:
            A dictionary representation of the current instance.
        """
        return self.__class__._serialize_fn(self)

    @classmethod
    def deserialize(cls, data: dict[str, Any]):  # noqa: ANN206
        """Deserialize the dictionary into a dataclass with Python types.

        Args:
            data: The dictionary to deserialize.

        Returns:
            An instance of the dataclass.
        """
        return cls._deserialize_fn(cls, data)


def performance_test() -> None:
    """Test the performance of the serialization and deserialization."""
    from datetime import UTC, datetime
    from time import perf_counter

    @dataclass
    class ComplexSerializable(Serializable):
        """A complex serializable dataclass."""

        name: str
        age: int
        is_active: bool
        created_at: datetime
        updated_at: datetime

    @dataclass
    class NestedSerializable(Serializable):
        """A nested serializable dataclass."""

        name: str
        age: int
        is_active: bool
        created_at: datetime
        updated_at: datetime

    @dataclass
    class RootSerializable(Serializable):
        """A root serializable dataclass."""

        nested: NestedSerializable
        complex: dict[str, ComplexSerializable]
        list: list[ComplexSerializable]

    root = RootSerializable(
        nested=NestedSerializable(
            name="John Doe",
            age=30,
            is_active=True,
            created_at=datetime.now(UTC),
            updated_at=datetime.now(UTC),
        ),
        complex={
            "key": ComplexSerializable(
                name="John Doe", age=30, is_active=True, created_at=datetime.now(UTC), updated_at=datetime.now(UTC)
            )
        },
        list=[
            ComplexSerializable(
                name="John Doe", age=30, is_active=True, created_at=datetime.now(UTC), updated_at=datetime.now(UTC)
            )
        ],
    )

    start = perf_counter()
    for _ in range(100):
        root.serialize()
    custom_serialization_time = (perf_counter() - start) / 100 * 1000

    start = perf_counter()
    for _ in range(100):
        asdict(root)
    asdict_serialization_time = (perf_counter() - start) / 100 * 1000

    print(f"Custom serialization time: {custom_serialization_time:.6f} avg. ms")  # noqa: T201
    print(f"asdict serialization time: {asdict_serialization_time:.6f} avg. ms")  # noqa: T201

    print(f"Equal: {root.serialize() == asdict(root)}")  # noqa: T201
    print(f"Ratio: {asdict_serialization_time / custom_serialization_time:.2f}x")  # noqa: T201
