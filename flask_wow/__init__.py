"""
    flask-wow
    ~~~~~~~~~

    A simple CLI Generator to create flask app.

    :copyright: 2020 Cove
    :license: BSD 3-Clause License
"""

__version__ = '0.2.0'


# def demo():
#
#     if args.cmd == 'addapp':
#         print(f'Will create Flask app with name "{args.name}"')
#         dir_name = os.path.dirname(__file__)
#         source_dir = os.path.join(dir_name, 'templates', 'app_tmp')
#         dist_dir = os.path.join(os.getcwd(), args.name)
#         if dist_dir_check(dist_dir):
#             shutil.copytree(source_dir, dist_dir,
#                             ignore=lambda src, names: [name for name in names if name == '__pycache__'])
#             format_dir(dist_dir, args.name, args.name)
#             print(f'Create app at {dist_dir} Success!')
#         else:
#             print(f'The directory {dist_dir} was not empty, Can\'t create app.')
