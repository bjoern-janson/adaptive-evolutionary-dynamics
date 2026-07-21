"""
generator_metrics.py

Adaptive Evolutionary Architecture

Generator Dynamics Measurement Layer.

This module defines observable proxies for:

    G_m

the generator-modification mechanism.

Core distinction:

    Capability:
        What the system can produce.

    Generator:
        How the system produces improvements.

    Generator modification:
        How the improvement process itself changes.

The purpose of this module is not to measure intelligence.
It estimates whether a system has become better at improving
its own capability-generation process.

"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


# ============================================================
# Generator Metrics
# ============================================================


@dataclass
class GeneratorMetrics:
    """
    Observable proxy vector for G_m.

    Proposed:

        G_m_hat =
        (
            ΔT,
            ΔA,
            ΔL,
            I_r,
            A_m
        )

    where:

        ΔT = iteration cost reduction
        ΔA = accessible approach expansion
        ΔL = representation compression
        I_r = reusable infrastructure
        A_m = automation of improvement
    """

    iteration_cost_reduction: float = 0.0

    approach_expansion: float = 0.0

    representation_compression: float = 0.0

    reusable_infrastructure: float = 0.0

    improvement_automation: float = 0.0


    def vector(self) -> List[float]:
        """
        Return:

            G_m_hat

        """

        return [
            self.iteration_cost_reduction,
            self.approach_expansion,
            self.representation_compression,
            self.reusable_infrastructure,
            self.improvement_automation,
        ]


# ============================================================
# Generator Change
# ============================================================


@dataclass
class GeneratorTransition:
    """
    Represents:

        ΔG_m

    """

    before: GeneratorMetrics

    after: GeneratorMetrics


    def delta(self) -> List[float]:
        """
        Compute generator modification.

        """

        return [
            b - a
            for a, b in zip(
                self.before.vector(),
                self.after.vector()
            )
        ]


    def magnitude(self) -> float:
        """
        Scalar approximation:

            |ΔG_m|

        """

        import math

        return math.sqrt(
            sum(
                x*x
                for x in self.delta()
            )
        )


# ============================================================
# Generator Capacity
# ============================================================


@dataclass
class GeneratorState:
    """
    Represents the current improvement machinery.

    G_m is treated as a process/operator,
    not a scalar capability.

    """

    name: str

    domain: str

    mechanisms: List[str] = field(
        default_factory=list
    )

    metrics: GeneratorMetrics = field(
        default_factory=GeneratorMetrics
    )


    def describe(self) -> Dict[str, Any]:

        return {
            "name": self.name,
            "domain": self.domain,
            "mechanisms": self.mechanisms,
            "metrics": self.metrics.vector()
        }


# ============================================================
# Proxy Estimators
# ============================================================


def estimate_iteration_gain(
    old_cycle_time: float,
    new_cycle_time: float
) -> float:
    """
    Estimate:

        ΔT

    Lower iteration cost increases
    generator efficiency.

    """

    if old_cycle_time == 0:
        return 0.0

    return (
        old_cycle_time - new_cycle_time
    ) / old_cycle_time



def estimate_representation_compression(
    old_description_length: float,
    new_description_length: float
) -> float:
    """
    Estimate:

        ΔL

    Measures reduction in complexity required
    to express or operate a process.

    """

    if old_description_length == 0:
        return 0.0

    return (
        old_description_length
        -
        new_description_length
    ) / old_description_length



def estimate_reusable_infrastructure(
    reusable_components_before: int,
    reusable_components_after: int
) -> float:
    """
    Estimate:

        I_r

    Increase in reusable transformation assets.

    """

    if reusable_components_before == 0:
        return float(
            reusable_components_after
        )

    return (
        reusable_components_after
        -
        reusable_components_before
    ) / reusable_components_before



def estimate_approach_expansion(
    old_strategy_count: int,
    new_strategy_count: int
) -> float:
    """
    Estimate:

        ΔA

    Expansion of accessible solution methods.

    """

    if old_strategy_count == 0:
        return float(new_strategy_count)

    return (
        new_strategy_count
        -
        old_strategy_count
    ) / old_strategy_count



def estimate_improvement_automation(
    manual_steps_removed: int,
    total_steps: int
) -> float:
    """
    Estimate:

        A_m

    Degree to which improvement cycles
    become automated.

    """

    if total_steps == 0:
        return 0.0

    return (
        manual_steps_removed
        /
        total_steps
    )


# ============================================================
# Generator Score
# ============================================================


def generator_score(
    metrics: GeneratorMetrics,
    weights: Optional[List[float]] = None
) -> float:
    """
    Produce a scalar proxy:

        |G_m|

    This is not the definition of G_m.

    It is only an empirical estimator.

    """

    values = metrics.vector()

    if weights is None:
        weights = [
            1,
            1,
            1,
            1,
            1
        ]

    return sum(
        v*w
        for v, w in zip(
            values,
            weights
        )
    )


# ============================================================
# Generator Transition Detection
# ============================================================


def detect_generator_transition(
    before: GeneratorMetrics,
    after: GeneratorMetrics,
    threshold: float = 0.1
) -> bool:
    """
    Detect whether:

        ΔG_m > 0

    """

    transition = GeneratorTransition(
        before,
        after
    )

    return (
        transition.magnitude()
        >
        threshold
    )


# ============================================================
# Historical Example Schema
# ============================================================


@dataclass
class GeneratorEvent:
    """
    Dataset-compatible event.

    Used by:

        phase_boundary_dataset.md

    """

    name: str

    system: str

    before: GeneratorState

    after: GeneratorState

    year: Optional[int] = None


    def delta_generator(self):

        return GeneratorTransition(
            self.before.metrics,
            self.after.metrics
        )


# ============================================================
# Example
# ============================================================


if __name__ == "__main__":

    manual_programming = GeneratorState(
        name="Manual Programming",
        domain="computation",
        mechanisms=[
            "human instruction writing"
        ]
    )

    compiler_system = GeneratorState(
        name="Compiler",
        domain="computation",
        mechanisms=[
            "automatic translation",
            "optimization",
            "reuse"
        ],
        metrics=GeneratorMetrics(
            iteration_cost_reduction=0.8,
            approach_expansion=0.7,
            representation_compression=0.9,
            reusable_infrastructure=0.8,
            improvement_automation=0.6
        )
    )


    event = GeneratorEvent(
        name="Compiler Transition",
        system="software development",
        before=manual_programming,
        after=compiler_system
    )


    print(
        "Generator change:",
        event.delta_generator().magnitude()
    )
