# Copyright (C) 2018 Nithya Duraisamy <nithyadurai87@gmail.com>
# Tamil sandhi checker - validate and fix list of Sandhi errors in Tamil text

from . import sandhi_checker
check_sandhi = sandhi_checker.check_sandhi
Results = sandhi_checker.Results
sandhi_checker_file_IO=sandhi_checker.sandhi_checker_file_IO
__all__ = ["check_sandhi","sandhi_checker","Results","sandhi_checker_file_IO"]

