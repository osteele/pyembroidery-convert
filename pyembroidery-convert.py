#! /usr/bin/env uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pyembroidery",
#     "click",
# ]
# ///
import click
import pyembroidery
import os

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument('input_file', type=click.Path(exists=True), required=False)
@click.option('-o', '--output', type=click.Path(), help='Output file name')
@click.option('-t', '--type', type=str, help='Output file type')
@click.option('--list', is_flag=True, help='List supported formats')
def convert_embroidery(input_file, output, type, list):
    """Convert embroidery file to specified format."""
    supported_formats = pyembroidery.supported_formats()

    if list:
        click.echo("Supported formats:")
        for format_info in supported_formats:
            click.echo(f"- {format_info['extension']}: {format_info['description']}")
        return

    if not input_file:
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        ctx.exit()

    if bool(output) == bool(type):
        raise click.UsageError("Exactly one of --output or --type must be provided.")

    typename = type.lower()
    if typename not in [format_info['extension'] for format_info in supported_formats]:
        raise click.UsageError(f"Unsupported format: {type}")

    if not output:
        output = os.path.splitext(input_file)[0] + f'.{typename}'

    if os.path.abspath(input_file) == os.path.abspath(output):
        raise click.UsageError("Output file cannot be the same as input file.")

    pattern = pyembroidery.read(input_file)
    pyembroidery.write(pattern, output)
    click.echo(f"Converted {input_file} to {output}")


if __name__ == '__main__':
    convert_embroidery()
