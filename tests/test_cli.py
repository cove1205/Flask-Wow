import pytest
from click.testing import CliRunner

from flask_wow.cli import startproject



def test_startproject():

    runner = CliRunner()
    result = runner.invoke(startproject, ["newproject"])
    assert not result.exception
