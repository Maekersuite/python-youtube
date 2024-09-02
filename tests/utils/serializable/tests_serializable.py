from dataclasses import dataclass
from typing import Optional

import pytest

from pyyoutube.utils import Serializable


@dataclass
class SerializableExample(Serializable):
    name: str
    age: int


@pytest.mark.structure
def test_serializable_serialization():
    """Test the `serialize` method of the `Serializable` class."""
    test = SerializableExample(name="John", age=30)
    data = test.serialize()
    assert isinstance(data, dict)
    assert data["name"] == "John"
    assert data["age"] == 30


@pytest.mark.structure
def test_serializable_inheritance():
    """Test inheritance and serialization of nested Serializable classes."""

    @dataclass
    class NestedSerializable(Serializable):
        value: float

    @dataclass
    class ComplexSerializable(SerializableExample):
        nested: NestedSerializable

    complex_test = ComplexSerializable(name="Alice", age=25, nested=NestedSerializable(value=3.14))
    data = complex_test.serialize()

    assert isinstance(data, dict)
    assert data["name"] == "Alice"
    assert data["age"] == 25
    assert isinstance(data["nested"], dict)
    assert data["nested"]["value"] == pytest.approx(3.14)


@pytest.mark.structure
def test_serializable_empty():
    """Test serialization of an empty Serializable class."""

    @dataclass
    class EmptySerializable(Serializable):
        pass

    empty_test = EmptySerializable()
    data = empty_test.serialize()

    assert isinstance(data, dict)
    assert len(data) == 0


@pytest.mark.structure
def test_serializable_with_default_values():
    """Test serialization of a Serializable class with default values."""

    @dataclass
    class DefaultValueSerializable(Serializable):
        name: str = "Default"
        count: int = 0

    default_test = DefaultValueSerializable()
    data = default_test.serialize()

    assert isinstance(data, dict)
    assert data["name"] == "Default"
    assert data["count"] == 0

    custom_test = DefaultValueSerializable(name="Custom", count=10)
    custom_data = custom_test.serialize()

    assert isinstance(custom_data, dict)
    assert custom_data["name"] == "Custom"
    assert custom_data["count"] == 10


@pytest.mark.structure
def test_serializable_deserialization():
    """Test the `deserialize` method of the `Serializable` class."""
    data = {"name": "Jane", "age": 28}
    deserialized = SerializableExample.deserialize(data)
    assert isinstance(deserialized, SerializableExample)
    assert deserialized.name == "Jane"
    assert deserialized.age == 28


@pytest.mark.structure
def test_serializable_inheritance_deserialization():
    """Test deserialization of nested Serializable classes."""

    @dataclass
    class NestedSerializable(Serializable):
        value: float

    @dataclass
    class ComplexSerializable(SerializableExample):
        nested: NestedSerializable

    data = {"name": "Bob", "age": 35, "nested": {"value": 2.718}}
    deserialized = ComplexSerializable.deserialize(data)

    assert isinstance(deserialized, ComplexSerializable)
    assert deserialized.name == "Bob"
    assert deserialized.age == 35
    assert isinstance(deserialized.nested, NestedSerializable)
    assert deserialized.nested.value == pytest.approx(2.718)


@pytest.mark.structure
def test_serializable_empty_deserialization():
    """Test deserialization of an empty Serializable class."""

    @dataclass
    class EmptySerializable(Serializable):
        pass

    data = {}
    deserialized = EmptySerializable.deserialize(data)

    assert isinstance(deserialized, EmptySerializable)


@pytest.mark.structure
def test_serializable_with_default_values_deserialization():
    """Test deserialization of a Serializable class with default values."""

    @dataclass
    class DefaultValueSerializable(Serializable):
        name: str = "Default"
        count: int = 0

    data = {}
    deserialized = DefaultValueSerializable.deserialize(data)

    assert isinstance(deserialized, DefaultValueSerializable)
    assert deserialized.name == "Default"
    assert deserialized.count == 0

    custom_data = {"name": "Custom", "count": 10}
    custom_deserialized = DefaultValueSerializable.deserialize(custom_data)

    assert isinstance(custom_deserialized, DefaultValueSerializable)
    assert custom_deserialized.name == "Custom"
    assert custom_deserialized.count == 10


@pytest.mark.structure
def test_serializable_complex_types():
    """Test serialization and deserialization of complex types."""

    @dataclass
    class NestedSerializable(Serializable):
        value: float

    @dataclass
    class ComplexSerializable(Serializable):
        nested: list[NestedSerializable]
        optional: Optional[NestedSerializable]
        complex_tuple: tuple[NestedSerializable]
        complex_dict: dict[str, NestedSerializable]
        simple: list[str]
        simple_set: set[str]
        simple_tuple: tuple[str]
        simple_dict: dict[str, str]

    nested = NestedSerializable(value=1.0)

    complex_test = ComplexSerializable(
        nested=[nested, nested],
        optional=None,
        complex_tuple=(nested,),
        complex_dict={"key": nested},
        simple=["a", "b", "c"],
        simple_set={"a", "b", "c"},
        simple_tuple=("a", "b", "c"),
        simple_dict={"a": "b", "c": "d"},
    )

    data = complex_test.serialize()
    assert isinstance(data, dict)
    assert data["nested"] == [{"value": 1.0}, {"value": 1.0}]
    assert data["optional"] is None
    assert data["complex_tuple"] == ({"value": 1.0},)
    assert data["complex_dict"] == {"key": {"value": 1.0}}
    assert data["simple"] == ["a", "b", "c"]
    assert data["simple_set"] == {"a", "b", "c"}
    assert data["simple_tuple"] == ("a", "b", "c")
    assert data["simple_dict"] == {"a": "b", "c": "d"}

    deserialized = ComplexSerializable.deserialize(data)
    assert isinstance(deserialized, ComplexSerializable)
    assert deserialized.nested == [nested, nested]
    assert deserialized.optional is None
    assert deserialized.complex_tuple == (nested,)
    assert deserialized.complex_dict == {"key": nested}
    assert deserialized.simple == ["a", "b", "c"]
    assert deserialized.simple_set == {"a", "b", "c"}
    assert deserialized.simple_tuple == ("a", "b", "c")
