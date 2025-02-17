# a wrapper around esptool.py to simplify flashing MicroPython or CircuitPython onto an ESP32-C6 dev kit board
import os
import click
import subprocess
import shlex

mp = "ESP32_GENERIC_C6-20241129-v1.24.1.bin"
cp = "adafruit-circuitpython-espressif_esp32c6_devkitc_1_n8-en_US-9.2.4.bin"

@click.command()
@click.option('-f', '--firmware',
              default='MicroPython',
              type=click.Choice(['MicroPython', 'CircuitPython']),
              help='Which version of Python to flash, e.g. MicroPython or CircuitPython')
def cli(firmware):
    app_path, _ = os.path.split(os.path.abspath(__file__))
    if firmware == 'CircuitPython':
        bin = cp
    else:
        bin = mp
    bin_path = os.path.join(app_path, "bin", bin)
    if click.confirm("Erase flash?"):
        click.echo("Erasing flash on ESP32…")
        erase = shlex.split('esptool.py erase_flash')
        #subprocess.run(erase)
        click.echo(f"Flash erased!")
    else:
        click.echo("Skipping erasing flash")
    if click.confirm("Flash devive with {firmware}?"):
        click.echo(f"Flashing bin {bin} to device…")
        flash = shlex.split(f'esptool.py --baud 460800 write_flash 0 {bin_path}')
        #subprocess.run(flash)
        click.echo("Device flashed!")

if __name__ == '__main__':
    cli()
