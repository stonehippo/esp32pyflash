# a wrapper around esptool.py to simplify flashing MicroPython or CircuitPython onto an ESP32-C6 dev kit board
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
    if firmware == 'CircuitPython':
        bin = cp
    else:
        bin = mp
    click.echo("Erasing flash on ESP32")
    erase = shlex.split('esptool.py erase_flash…')
    #subprocess.run(erase)
    click.echo(f"Flash erased!\nFlashing the device with {firmware}")
    click.echo(f"Flashing bin {bin}…")
    flash = shlex.split(f'esptool.py --baud 460800 write_flash 0 {bin}')
    #subprocess.run(flash)
    click.echo("Board flashed!")

if __name__ == '__main__':
    cli()
