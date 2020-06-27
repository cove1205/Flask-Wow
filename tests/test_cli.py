import pytest
from click.testing import CliRunner

from flask_wow.cli import startproject_command



def test_startproject():

    runner = CliRunner()
    result = runner.invoke(startproject_command, ["newproject"])
    assert not result.exception
