# Crumbly
It just (27/02/2025) occurred to me that this is literally just a glorified dictionary :sob:
It's neat but like come on this literally has nearly the exact features of a dictionary

## Introduction

**Crumbly Library** is a Python library designed to provide a versatile and user-friendly way of storing and managing multiple variables within a single object. This library offers the `Crumb` class, which acts as a container for various key-value pairs, akin to a dictionary. The library aims to simplify the management of data and provide easy-to-use methods for manipulation, conversion, and serialization.

Oh yeah also this was the first name that came to mind, and it *kinda*.... sucks. Can't think of a better one tho

## Features

- **Flexible Storage**: `Crumb` objects allow you to store multiple variables using key-value pairs, similar to a dictionary, providing a convenient way to organize related data.

- **Easy Access**: With intuitive methods such as `__getattr__`, accessing values stored in a `Crumb` is seamless, reducing the need for verbose code.

- **Dynamic Attributes**: Accessing attributes of a `Crumb` object is done by simply using attribute notation, making the code more readable and concise.

- **Dynamic Modification**: The library provides methods for adding, modifying, and deleting key-value pairs within the `Crumb` object, allowing for dynamic data manipulation.

- **Serialization**: `Crumb` objects can be converted into JSON format using the `makeJSON` method, and vice versa using the `crumbFromJSON` class method, facilitating data serialization and deserialization.

- **Convenience Methods**: The library includes various convenient methods for retrieving keys, values, items, copying, checking for key existence, and more.

## Installation

To use the **Crumbly Library**, you can download it off of PyPI using `pip install crumbly` 

Or,

### Stable release

Download the provided ZIP file in the Releases page (`crumbly_vXXXX_XX_XX.zip`) and include the `crumbly.py` file from inside the ZIP in your project directory. Then, simply import the `Crumb` class into your Python code.

### Unstable release

Download `crumbly.py` from the Code section of this page, and include it in your project directory. Then, simply import the `Crumb` class into your Python code.

### Importing

```python
from crumbly import Crumb
```

## Usage

### Creating a `Crumb` Object

To create a `Crumb` object, you can initialize it with key-value pairs as arguments:

```python
my_crumb = Crumb(name="Alice", age=30, city="Wonderland")
```

### Accessing Values

Values stored in a `Crumb` object can be accessed using attribute notation:

```python
print(my_crumb.name)  # Output: Alice
print(my_crumb.age)   # Output: 30
```

### Modifying and Deleting Values

You can modify existing values or add new key-value pairs using the `addData` method:

```python
my_crumb.addData("job", "Adventurer")
my_crumb.age = 31
```

To delete a key-value pair:

```python
del my_crumb.city
```

### Serialization

You can convert a `Crumb` object into a JSON string using the `makeJSON` method:

```python
json_data = my_crumb.makeJSON()
```

And deserialize a JSON string back into a `Crumb` object using the `crumbFromJSON` class method:

```python
restored_crumb = Crumb.crumbFromJSON(json_data)
```

### Other Useful Methods

- `len(my_crumb)`: Get the number of key-value pairs in the `Crumb` object.
- `my_crumb.keys()`: Get a list of keys in the `Crumb` object.
- `my_crumb.values()`: Get a list of values in the `Crumb` object.
- `my_crumb.items()`: Get a list of key-value tuples in the `Crumb` object.
- `my_crumb.copy()`: Create a copy of the `Crumb` object.
- `my_crumb.has_key("name")`: Check if a key exists in the `Crumb` object.
- `my_crumb.clear()`: Remove all key-value pairs from the `Crumb` object.

## Contributions

Contributions to the **Crumbly Library** are welcome! If you find any issues or have suggestions for improvements, feel free to submit a pull request or open an issue on the [GitHub repository](https://github.com/noodledx/crumbly).

## License

This library is provided under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

**Disclaimer:** The "Crumbly Library" is intended for educational and experimental purposes and might not be suitable for production use. Use it at your own discretion.

## ...

No, **YOU** used ChatGPT to make this readme

I did change the installation part from the generated version quite a bit though
