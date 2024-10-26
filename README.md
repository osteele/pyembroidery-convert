# Embroidery File Converter

This Python script provides a command-line interface for converting embroidery
files between different formats using the
[`pyembroidery`](https://github.com/EmbroidePy/pyembroidery) library.

## Features

- Convert embroidery files to various supported formats
- List all supported embroidery file formats
- Simple command-line interface

## Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) package manager

## Installation

1. Ensure you have `uv` installed.
2. Clone this repository or download the `pyembroidery-convert.py` script.
3. Make the script executable:
   ```sh
   chmod +x pyembroidery-convert.py
   ```

## Usage

```sh
./pyembroidery-convert.py [OPTIONS] [INPUT_FILE]
```


### Options:

- `-o, --output FILE`: Specify the output file name
- `-t, --type FORMAT`: Specify the output file type
- `--list`: List all supported embroidery file formats
- `-h, --help`: Show help message and exit

### Examples:

1. Convert a file to a specific format:
   ```
   ./pyembroidery-convert.py input.pes -t dst
   ```

2. Convert a file with a custom output name:
   ```
   ./pyembroidery-convert.py input.pes -o output.dst
   ```

3. List supported formats:
   ```
   ./pyembroidery-convert.py --list
   ```

## Supported Formats

To see a list of all supported embroidery file formats, run the script with the
`--list` option.

## Notes

- You must provide either the `--output` or `--type` option, but not both.
- The input file and output file cannot be the same.
- If only the `--type` option is provided, the output file will be created in
  the same directory as the input file with the new extension.

## Dependencies

- [pyembroidery](https://github.com/EmbroidePy/pyembroidery)
- [click](https://click.palletsprojects.com/)

These dependencies are automatically managed by `uv` when running the script.

## License

Copyright (c) 2024 Oliver Steele

This project is licensed under the MIT License.
