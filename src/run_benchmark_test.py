# Copyright OpenSearch Contributors
# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.

import sys
from typing import Union

from manifests.build_manifest import BuildManifest
from manifests.bundle_manifest import BundleManifest
from system import console
from test_workflow.benchmark_test.benchmark_args import BenchmarkArgs
from test_workflow.benchmark_test.benchmark_test_runners import BenchmarkTestRunners
from test_workflow.benchmark_test.benchmark_test_suite import BenchmarkTestSuite


def main() -> int:
    """
    Entry point for Benchmark Test with bundle manifest or for a comparison between two test executions.
    If running a benchmark, the config file will contain the required arguments for running
    benchmarking test. Will call out in test.sh with 'benchmark execute-test' or 'benchmark compare' as argument
    """
    benchmark_args = BenchmarkArgs()

    if benchmark_args.command == "execute-test":
        console.configure(level=benchmark_args.logging_level)
        if benchmark_args.bundle_manifest:
            manifest: Union[BundleManifest, BuildManifest] = (
                BundleManifest.from_file(benchmark_args.bundle_manifest)
                if not benchmark_args.min_distribution
                else BuildManifest.from_file(benchmark_args.bundle_manifest)
            )
            BenchmarkTestRunners.from_args(benchmark_args, manifest).run()
        else:
            BenchmarkTestRunners.from_args(benchmark_args).run()
    else:
        benchmark_test_suite = BenchmarkTestSuite("", False, benchmark_args, "")
        benchmark_test_suite.execute()

    return 0


if __name__ == "__main__":
    sys.exit(main())
