# -*- coding: utf-8 -*-
# @Time    : 3/25/2024 8:39 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : HCSeetings.py
# @Software: PyCharm

from dataclasses import dataclass


@dataclass(kw_only=True)
class HCSettings:
    load_mult: float
    push_reg: int
    capacitor: bool
    add_existing_ger: bool
    mult_existing_gen: float