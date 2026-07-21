"""
reachability.py

Adaptive Evolutionary Architecture

Reachable Space Geometry.

Defines the mathematical object:

    P^reach(t)

the set of future transformations accessible to a system
given its current state, representations, resources,
search mechanisms, and generator mechanisms.

Core distinction:

    Possible futures != Reachable futures

This module does not attempt to enumerate all possible
futures. It defines the boundary of futures accessible
under constraints.

"""

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Set, Tuple


# ============================================================
# Transformation Object
# ============================================================

@dataclass(frozen=True)
class Transformation:
    """
    A reachable transformation.

    Represents:

        tau : E_t -> E_{t+k}

    A transformation is not a state.
    It is a transition between states.

    """

    name: str

    source: Any

    target: Any

    cost: float = 0.0

    metadata: Dict[str, Any] = field(default_factory=dict)


# ============================================================
# Reachability Constraints
# ============================================================

@dataclass
class ReachabilityConstraints:
    """
    Constraints defining the reachable region.

    P^reach is bounded by:

        (M, pi, V, C, G_s, G_m, R)

    """

    representation: Any = None

    policy: Any = None

    value_function: Any = None

    capability: float = 0.0

    search_mechanism: Any = None

    generator_mechanism: Any = None

    resources: Dict[str, float] = field(
        default_factory=dict
    )


# ============================================================
# Reachable Evolutionary Space
# ============================================================

@dataclass
class ReachableSpace:
    """
    Approximation of:

        P^reach_evo(t)

    Defined as:

        {
            tau:
            E_t -> E_(t+k)

            reachable under X_t,R_t
        }

    """

    transformations: Set[Transformation] = field(
        default_factory=set
    )

    constraints: Optional[
        ReachabilityConstraints
    ] = None


    def size(self) -> int:
        """
        Approximation of:

            |P^reach|

        """

        return len(self.transformations)


    def add(self, transformation: Transformation):
        """
        Add an accessible transformation.
        """

        self.transformations.add(
            transformation
        )


    def contains(self, transformation: Transformation):
        """
        Test whether a transformation is reachable.
        """

        return transformation in self.transformations


# ============================================================
# Reachability Expansion
# ============================================================

def reachable_expansion(
    old_space: ReachableSpace,
    new_space: ReachableSpace
) -> Set[Transformation]:
    """
    Calculate frontier expansion.

   :

        ΔP^reach =
        P^reach(t+1) - P^reach(t)

    """

    return (
        new_space.transformations
        -
        old_space.transformations
    )


# ============================================================
# Capability Proxy
# ============================================================

def capability(space: ReachableSpace) -> int:
    """
    Current capability approximation:

        C_t = |P^reach_current(t)|

    """

    return space.size()


# ============================================================
# Reachable Frontier Distance
# ============================================================

def frontier_distance(
    space_a: ReachableSpace,
    space_b: ReachableSpace
) -> float:
    """
    Measures difference between reachable spaces.

    A simple symmetric distance proxy.

    Future versions may replace this with:
    
        - KL divergence
        - graph distance
        - Wasserstein distance
        - manifold distance

    """

    union = (
        space_a.transformations
        |
        space_b.transformations
    )

    intersection = (
        space_a.transformations
        &
        space_b.transformations
    )

    if len(union) == 0:
        return 0.0

    return (
        1 -
        len(intersection) / len(union)
    )


# ============================================================
# Search Expansion
# ============================================================

def explore_reachable_space(
    current_space: ReachableSpace,
    search_operator: Callable[
        [ReachableSpace],
        List[Transformation]
    ]
) -> ReachableSpace:
    """
    Apply G_s:

        G_s:
        P^reach_current
        ->
        P^explored

    Search expands known reachable transformations.

    """

    discoveries = search_operator(
        current_space
    )

    expanded = ReachableSpace(
        transformations=set(
            current_space.transformations
        ),
        constraints=current_space.constraints
    )

    for item in discoveries:
        expanded.add(item)

    return expanded


# ============================================================
# Generator Expansion
# ============================================================

def modify_reachability_generator(
    space: ReachableSpace,
    generator_operator: Callable
) -> ReachableSpace:
    """
    Apply G_m:

        G_m:
        G_s(t)
        ->
        G_s(t+1)

    Changes the mechanism responsible
    for exploring future transformations.

    """

    return generator_operator(space)


# ============================================================
# Reachability Growth Rate
# ============================================================

def log_reachability_velocity(
    previous: ReachableSpace,
    current: ReachableSpace,
    dt: float
) -> float:
    """
    Approximation of:

        Λ(t)
        =
        d/dt log|P^reach(t)|

    """

    if previous.size() == 0:
        return 0.0

    import math

    return (
        math.log(current.size())
        -
        math.log(previous.size())
    ) / dt


# ============================================================
# Evolutionary Reachability Object
# ============================================================

@dataclass
class EvolutionaryReachability:
    """
    Combined object for historical experiments.

    Stores:

        reachable space
        generator changes
        capability changes

    """

    time: float

    space: ReachableSpace

    generator_change: float = 0.0

    capability_change: float = 0.0


    def snapshot(self):
        return {
            "time": self.time,
            "reachable_size": self.space.size(),
            "generator_change": self.generator_change,
            "capability_change": self.capability_change,
        }


# ============================================================
# Example
# ============================================================

if __name__ == "__main__":

    space = ReachableSpace()

    space.add(
        Transformation(
            name="manual_solution",
            source="problem",
            target="answer"
        )
    )

    space.add(
        Transformation(
            name="automated_solution",
            source="problem",
            target="answer"
        )
    )

    print(
        "Reachable capability:",
        capability(space)
    )
