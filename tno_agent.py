import click
import subprocess  # Для Gemini
import logging  # Для логов

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@click.group()  # Группа команд
def cli():
    pass

@cli.command()  # Пример: Тестовая команда
@click.option('--test', default='world', help='Test param')
def hello(test):
    """Простая тестовая команда."""
    logging.info(f"Starting hello command with {test}")
    click.echo(f"Hello {test}!")

@cli.command(name='g_help')  # Команда для Gemini помощи
@click.argument('prompt')
def gemini_help(prompt):
    """Запуск Gemini для помощи (e.g., debug)."""
    try:
        result = subprocess.run(['gemini.cmd', '-p', prompt], capture_output=True, text=True)
        click.echo(result.stdout)
    except Exception as e:
        logging.error(f"Gemini error: {e}")
        click.echo("Error running Gemini.")

if __name__ == '__main__':
    cli()