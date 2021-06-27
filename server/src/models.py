from pydantic import BaseModel

from typing import Optional


class Problem(BaseModel):
    title: str
    description: str
    problem_statement: str
    input_format: str
    constraints: Optional[str] = 'This program has no constraints.'
    output_format: str

class ProblemUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    problem_statement: Optional[str]
    input_format: Optional[str]
    constraints: Optional[str]
    output_format: Optional[str]


class TestCase(BaseModel):
    std_input: str
    std_output: str
    sample: bool
