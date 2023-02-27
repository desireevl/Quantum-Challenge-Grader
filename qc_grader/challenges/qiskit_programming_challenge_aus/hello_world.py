import jsonpickle
import pickle

from pathlib import Path

from qc_grader.grader.grade import grade


challenge_id = Path(__file__).parent.name


@typechecked
def grade_ex1a(qc: QuantumCircuit) -> None:
    answer = jsonpickle.encode(qc.export_as_lp_string())
    grade(answer, '1a', challenge_id)
