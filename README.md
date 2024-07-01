# Internet.bs API Python Wrapper | Unofficial

This project provides a Python wrapper for the Internet.bs API, allowing easy interaction with various domain management functionalities.

## Features

- Account management
- Domain operations
- DNS record management
- URL and Email forwarding
- Host management

## Installation

To install the package, use pip:

```
pip install internetbs-api
```

## Usage

First, import the necessary classes:

```python
from internetbs-api import Account, Domain, DNS, Forwarding, Host
```

Then, initialize the API with your credentials:

```python
api_key = 'your_api_key'
password = 'your_password'
test_mode = False  # Set to True for testing

account = Account(api_key, password, test_mode)
domain = Domain(api_key, password, test_mode)
dns = DNS(api_key, password, test_mode)
forwarding = Forwarding(api_key, password, test_mode)
host = Host(api_key, password, test_mode)
```

### Examples

#### Check Domain Availability

```python
result = domain.check_availability('example.com')
print(result)
```

#### Add DNS Record

```python
result = dns.add_record('example.com', 'A', '192.168.1.1')
print(result)
```

#### Add URL Forward

```python
result = forwarding.add_url_forward('example.com', 'https://destination.com')
print(result)
```

#### Create Host

```python
result = host.create_host('ns1.example.com', '192.168.1.1')
print(result)
```

## Documentation

For detailed documentation on all available methods and their parameters, please refer to the inline comments in the source code.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

If specific functions do not work, do not hesitate to open an issue as I have not fully implemented all functions.
