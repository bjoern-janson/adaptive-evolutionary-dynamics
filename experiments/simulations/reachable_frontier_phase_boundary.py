"""
Reachable Frontier Phase Boundary Experiment

Tests the stronger hypothesis:

    ΔGm → ΔΩ → ΔP_reach → ΔC

where:

C_t:
    current capability

P_t:
    reachable possibility frontier

G_m:
    generator modification capacity

The key distinction:

Resource scaling:
    grows capability inside a fixed frontier

Evolutionary system:
    expands the frontier itself


Prediction:

Early:
    resource system may perform better

Later:
    evolutionary system crosses because
    reachable space expands.
"""


import math


TIMESTEPS = 50


# ==========================================
# Parameters
# ==========================================

alpha = 0.15      # capability approaches frontier
beta = 0.05       # frontier expansion from generator
gamma = 0.10      # generator improvement

initial_capability = 1.0
initial_frontier = 10.0
initial_generator = 1.0



# ==========================================
# Resource System
# ==========================================

def run_resource_system():

    C = initial_capability
    P = initial_frontier
    Gm = initial_generator

    history = []


    for t in range(TIMESTEPS):

        history.append(
            {
                "t": t,
                "C": C,
                "P": P,
                "Gm": Gm,
                "Omega": 0
            }
        )


        # Capability approaches fixed frontier
        C += alpha * (P - C)


        # Frontier does not expand
        P = P


    return history



# ==========================================
# Evolutionary System
# ==========================================

def run_evolutionary_system():

    C = initial_capability
    P = initial_frontier
    Gm = initial_generator

    history = []


    previous_Gm = Gm


    for t in range(TIMESTEPS):

        omega = Gm - previous_Gm


        history.append(
            {
                "t": t,
                "C": C,
                "P": P,
                "Gm": Gm,
                "Omega": omega
            }
        )


        # Capability moves toward reachable frontier
        C += alpha * (P - C)


        # Generator expands frontier
        P *= (1 + beta * Gm)


        # Generator improves itself
        previous_Gm = Gm
        Gm *= (1 + gamma)


    return history



# ==========================================
# Run simulations
# ==========================================

resource = run_resource_system()
evolutionary = run_evolutionary_system()



# ==========================================
# Display
# ==========================================

print("=" * 65)
print("REACHABLE FRONTIER PHASE BOUNDARY TEST")
print("=" * 65)


print(
    "\nt | Resource C | Resource P | "
    "Evolution C | Evolution P"
)

print("-" * 65)


for t in [0,5,10,15,20,30,40,49]:

    r = resource[t]
    e = evolutionary[t]

    print(
        f"{t:2d} | "
        f"{r['C']:10.3f} | "
        f"{r['P']:10.3f} | "
        f"{e['C']:12.3f} | "
        f"{e['P']:12.3f}"
    )



# ==========================================
# Find crossover
# ==========================================

crossover = None


for r,e in zip(resource,evolutionary):

    if e["C"] > r["C"]:

        crossover = e["t"]
        break



print("\n")
print("=" * 65)
print("FINAL RESULTS")
print("=" * 65)


print()

print(
    "Resource Final Capability:",
    round(resource[-1]["C"],3)
)

print(
    "Resource Final Frontier:",
    round(resource[-1]["P"],3)
)


print()

print(
    "Evolutionary Final Capability:",
    round(evolutionary[-1]["C"],3)
)

print(
    "Evolutionary Final Frontier:",
    round(evolutionary[-1]["P"],3)
)


print()

print(
    "Generator Change ΔGm:",
    round(
        evolutionary[-1]["Gm"]
        -
        initial_generator,
        3
    )
)

print(
    "Final Ω Proxy:",
    round(
        evolutionary[-1]["Omega"],
        5
    )
)



print("\n")


if crossover is not None:

    print(
        "Capability crossover detected at:",
        f"t={crossover}"
    )

else:

    print(
        "No capability crossover detected"
    )



print("\n")
print("=" * 65)
print("PHASE BOUNDARY INTERPRETATION")
print("=" * 65)


print(
"""
The framework prediction:

Resource system:
    ΔR > 0
    ΔGm ≈ 0
    fixed reachable frontier


Evolutionary system:
    ΔGm > 0
    Ω > 0
    expanding reachable frontier


The critical signal:

    ΔGm
      ↓
    ΔΩ
      ↓
    ΔP_reach
      ↓
    ΔC


The evolutionary system is not merely
better at using possibilities.

It creates new reachable possibilities.
"""
)
