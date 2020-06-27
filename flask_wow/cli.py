import os
import sys
import click
import shutil
import subprocess


@click.group(
    help="""\
Flask-Wow
A simple CLI Generator for flask apps.

\b
  {prefix}flask-wow startproject newproj
""".format(
        # cmd="export" if os.name == "posix" else "set",
        prefix="$ " if os.name == "posix" else "> ",
    ))
def cli():
    pass


@cli.command('startproject')
@click.argument('proj_name', nargs=1)
@click.option('-v', '--venv', is_flag=True)
def startproject_command(proj_name, venv):

    click.echo('Creating project with name "{}"...'.format(proj_name))

    proj_source = os.path.join(
        os.path.dirname(__file__),
        'templates',
        'project_tmp',
        'proj_name')

    proj_dist = os.path.join(os.getcwd(), proj_name)

    app_source = os.path.join(
        os.path.dirname(__file__),
        'templates',
        'app_tmp',
        'app_name')

    app_dist = os.path.join(proj_dist, 'apps', 'demo')

    if not dir_check(proj_dist):
        click.echo(
            'The directory {} was not empty, Can\'t create project.'.format(proj_name))
        return None

    click.echo('Copying files to "{}" ...'.format(proj_dist))
    shutil.copytree(proj_source, proj_dist,
                    ignore=lambda src, names: [name for name in names if name == '__pycache__'])

    click.echo(
        'Copying demo files from {} to {}...'.format(
            app_source, app_dist))
    shutil.copytree(app_source, app_dist,
                    ignore=lambda src, names: [name for name in names if name == '__pycache__'])

    ch_name(proj_dist, project_name=proj_name)

    if venv:
        create_venv(proj_name)

    click.echo('Creating project at {} has succeeded!'.format(proj_dist))


@cli.command('startapp')
@click.argument('app_name', nargs=1)
def startapp_command(app_name):

    click.echo('Creating app with name "{}"...'.format(app_name))

    app_source = os.path.join(
        os.path.dirname(__file__),
        'templates',
        'app_tmp',
        'app_name')
    app_dist = os.path.join(os.getcwd(), 'apps', app_name)

    shutil.copytree(app_source, app_dist,
                    ignore=lambda src, names: [name for name in names if name == '__pycache__'])

    click.echo('new app "{}" has been successfully created！'.format(app_name))

    pass


def dir_check(dist_dir):
    if not os.path.exists(dist_dir) or not os.listdir(
            dist_dir):  # dir not exists
        return True
    return False


def ch_name(root, app_name=None, project_name=None):

    for fl in os.walk(root):
        dir, sub_dir, files = fl
        for file in files:
            if not file.endswith('.py'):
                continue
            fp = os.path.join(dir, file)
            with open(fp, 'r', encoding='utf-8') as f:
                content = f.read()
                if project_name:
                    content = content.replace(
                        "{% project_name %}", project_name)
                if app_name:
                    content = content.replace("{% app_name %}", app_name)
                with open(f'{fp}.bak', 'w', encoding='utf-8') as f:
                    f.write(content)

            os.remove(fp)
            os.rename(f'{fp}.bak', fp)


def create_venv(project_name):

    process = subprocess.Popen(
        'cd {} && python -m venv venv'.format(os.getcwd()), shell=True, stdout=subprocess.PIPE)
    click.echo('Creating Python virtual environment...')
    process.wait()
    if process.returncode == 0:
        print('Virtual environment created.')
    else:
        print('Virtual environment creation failed: {}'.format(process.stdout))


def main(as_module=False):
    cli.main(args=sys.argv[1:],
             prog_name="python -m flask-wow" if as_module else None)


if __name__ == "__main__":
    main(as_module=True)
