import os
import subprocess

from django.core.management.base import BaseCommand, CommandError, CommandParser


class Command(BaseCommand):
    help = "Instalar dependencias em desenvolvimento"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("apps", nargs="+", type=str)

    def handle(self, *args, **kwargs):
        base_dir = os.path.abspath(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../../../")
        )
        apps_dir = os.path.join(base_dir, "apps")
        web_dir = os.path.join(base_dir, "web")

        app_list = kwargs["apps"]

        if len(app_list) == 1 and app_list[0] == "all":
            app_list = os.listdir(apps_dir)

        for app_name in app_list:
            src = os.path.join(apps_dir, app_name)
            if os.path.exists(src):
                try:
                    os.symlink(src, os.path.join(web_dir, app_name))
                    
                    requirements_path = os.path.join(src, 'requirements.txt')
                    if os.path.exists(requirements_path):
                        subprocess.run(['pip', 'install', '-r', requirements_path])

                    self.stdout.write(
                        self.style.SUCCESS(f'Create a symlink to "{app_name}" app')
                    )
                except FileExistsError:
                    pass
