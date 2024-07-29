# benchmark_test_base.py
from abc import ABC, abstractmethod
from typing import Any
import os

import subprocess

from test_workflow.benchmark_test.benchmark_args import BenchmarkArgs

class BenchmarkTestBase(ABC):
    endpoint: str
    security: bool
    args: BenchmarkArgs
    command: str
    password: str

    def __init__(
            self,
            endpoint: Any,
            security: bool,
            args: BenchmarkArgs,
            password: str
    ) -> None:
        self.endpoint = endpoint
        self.security = security
        self.args = args
        self.password = password
        self.command = None

    @abstractmethod
    def form_command(self) -> str:
        pass

    @abstractmethod
    def execute(self) -> None:
        pass

    def cleanup(self) -> None:
        subprocess.check_call(f"docker rm -f docker-container-{self.args.stack_suffix}", cwd=os.getcwd(), shell=True)