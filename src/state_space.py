"""
state_space.py

Adaptive Evolutionary Architecture

Core state-space representation.

This module defines the mathematical objects used to represent
adaptive systems:

    A_t = (S_t, D_t, X_t, Theta_t)

where:

    S_t     = scale
    D_t     = adaptive depth
    X_t     = internal configuration
    Theta_t = trajectory dynamics

The purpose is not to simulate a complete adaptive system,
but to provide a stable representation layer for empirical
and computational experiments.

"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Optional


# ============================================================
# Scale
# ============================================================

class Scale(Enum):
    """
    Where adaptation occurs.

    Scale is orthogonal to adaptive depth.

    A system can be:
        - micro + D3
        - macro + D0

    Scale does not imply sophistication.
    """

    MICRO = "micro"
    MESO = "meso"
    MACRO = "macro"
    CIVILIZATIONAL = "civilizational"


# ============================================================
# Adaptive Depth
# ============================================================

class AdaptiveDepth(Enum):
    """
    Target of adaptation.

    D answers:

        What does feedback modify?
    """

    D0_STATE = 0
    D1_SEARCH = 1
    D2_GENERATOR = 2
    D3_GENERATOR_DYNAMICS = 3


# ============================================================
# Internal Configuration
# ============================================================

@dataclass
class InternalConfiguration:
    """
    X_t

    Internal system configuration.

    X_t =
    (
        Z_t,
        M_t,
        pi_t,
        V_t,
        C_t,
        G_s,t,
        G_m,t,
        R_t
    )

    """

    # Current state
    Z: Any = None

    # Representation/model
    M: Any = None

    # Policy/controller
    policy: Any = None

    # Objective/value function
    value_function: Any = None

    # Current capability
    capability: float = 0.0

    # Search mechanism
    search_mechanism: Any = None

    # Generator modification mechanism
    generator_mechanism: Any = None

    # Available resources
    resources: Dict[str, float] = field(default_factory=dict)


# ============================================================
# Trajectory Dynamics
# ============================================================

@dataclass
class Trajectory:
    """
    Theta_t

    Describes how the system evolves.

    Represents:

        X_{t+1}=F_X(X_t,E_t,u_t)

    """

    time: float = 0.0

    state_history: list = field(default_factory=list)

    capability_history: list = field(default_factory=list)

    generator_history: list = field(default_factory=list)

    omega_history: list = field(default_factory=list)


# ============================================================
# Adaptive System State
# ============================================================

@dataclass
class AdaptiveSystem:
    """
    Complete adaptive architecture.

    A_t = (S_t,D_t,X_t,Theta_t)

    """

    scale: Scale

    depth: AdaptiveDepth

    configuration: InternalConfiguration

    trajectory: Trajectory = field(default_factory=Trajectory)

    metadata: Dict[str, Any] = field(default_factory=dict)


    def state_vector(self):
        """
        Return X_t.

        """

        return self.configuration


    def describe(self):
        """
        Human-readable structural summary.
        """

        return {
            "scale": self.scale.value,
            "depth": self.depth.name,
            "capability": self.configuration.capability,
            "resources": self.configuration.resources,
            "has_search_mechanism":
                self.configuration.search_mechanism is not None,
            "has_generator_mechanism":
                self.configuration.generator_mechanism is not None,
        }


# ============================================================
# State Transition
# ============================================================

def state_transition(
    system: AdaptiveSystem,
    environment: Any,
    action: Any
) -> AdaptiveSystem:
    """
    Implements the abstract transition:

        X_{t+1}=F_X(X_t,E_t,u_t)

    This is intentionally left abstract.

    Specific systems should implement:

        - biological evolution
        - scientific discovery
        - AI systems
        - organizations
        - economic systems

    """

    raise NotImplementedError(
        "Implement domain-specific adaptive dynamics."
    )


# ============================================================
# Depth Classification
# ============================================================

def classify_depth(target: str) -> AdaptiveDepth:
    """
    Classify adaptive depth based on feedback target.

    """

    mapping = {
        "state": AdaptiveDepth.D0_STATE,
        "search": AdaptiveDepth.D1_SEARCH,
        "generator": AdaptiveDepth.D2_GENERATOR,
        "generator_dynamics": AdaptiveDepth.D3_GENERATOR_DYNAMICS,
    }

    if target not in mapping:
        raise ValueError(
            f"Unknown adaptive target: {target}"
        )

    return mapping[target]


# ============================================================
# Example
# ============================================================

if __name__ == "__main__":

    system = AdaptiveSystem(
        scale=Scale.MICRO,
        depth=AdaptiveDepth.D2_GENERATOR,
        configuration=InternalConfiguration(
            capability=10.0,
            resources={
                "compute": 100,
                "data": 1000
            }
        )
    )

    print(system.describe())
