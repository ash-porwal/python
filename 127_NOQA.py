"""
If we want want to avoid PEP guidelines then we can add NOQA tag to that line.
NOQA stands for No Quality Assurance.

So, we can either specify NOQA as a comment like this - # NOQA or we can specify some particular rule 
that we are breaking, like earlier we hadsome error like E401, so that is the rule that we broke, so we
can ignore it like # NOQA:E401
"""
from my_module import some_function  # noqa

from my_module import some_function  # noqa: F401
