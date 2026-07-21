"""
Constrained Generator Phase Boundary Experiment

Tests:

        ΔGm → ΔΩ → ΔP_reach → ΔC

under realistic constraints.

Differences from previous model:

- Generator growth saturates (logistic)
- Improving the generator has a resource cost
- Frontier expansion has diminishing returns

Question:

Does adaptive acceleration survive when
self-improvement is constrained?

"""

import math


TIMESTEPS = 100


# ==========================================
# Parameters
# ==========================================

initial_C = 1.0
initial_P = 10.0
initial_G = 1.0
initial_R = 10.0


# Capability convergence
alpha = 0.15


# Generator logistic growth
gamma = 0.25
G_capacity = 100.0


# Frontier expansion
beta = 0.03


# Resource dynamics
resource_growth = 1.05
generator_cost = 0.02



# ==========================================
# Fixed Resource Baseline
# ==========================================

def run_baseline():

    C = initial_C
    P = initial_P

    history = []


    for t in range(TIMESTEPS):

        history.append(
            {
                "t": t,
                "C": C,
                "P": P,
                "G": 1.0,
                "R": initial_R,
                "Omega": 0
            }
        )


        # Capability improves inside fixed frontier

        C += alpha * (P - C)


    return history



# ==========================================
# Resource Scaling System
# ==========================================

def run_resource_scaling():

    C = initial_C
    P = initial_P
    R = initial_R


    history = []


    for t in range(TIMESTEPS):

        history.append(
            {
                "t": t,
                "C": C,
                "P": P,
                "G": 1.0,
                "R": R,
                "Omega": 0
            }
        )


        C += alpha * (P - C)


        # resources grow

        R *= resource_growth

        # resources expand frontier slightly

        P += 0.02 * R



    return history



# ==========================================
# Constrained Evolutionary System
# ==========================================

def run_evolutionary():

    C = initial_C
    P = initial_P
    G = initial_G
    R = initial_R


    previous_G = G


    history = []


    for t in range(TIMESTEPS):

        omega = G - previous_G


        history.append(
            {
                "t": t,
                "C": C,
                "P": P,
                "G": G,
                "R": R,
                "Omega": omega
            }
        )


        # Capability approaches reachable frontier

        C += alpha * (P - C)


        # Generator improves but saturates

        G += gamma * G * (1 - G / G_capacity)


        # Generator expands frontier

        frontier_gain = beta * G

        P *= (1 + frontier_gain)


        # Cost of maintaining improvement machinery

        R -= generator_cost * G


        # natural resource recovery

        R *= 1.01


        if R < 0:
            R = 0


        previous_G = G


    return history



# ==========================================
# Run
# ==========================================

baseline = run_baseline()
resource = run_resource_scaling()
evolutionary = run_evolutionary()



# ==========================================
# Output
# ==========================================

print("=" * 70)
print("CONSTRAINED GENERATOR PHASE BOUNDARY TEST")
print("=" * 70)


print(
"""
t | Baseline C | Resource C | Evolution C | Frontier | Generator
------------------------------------------------------------------
"""
)


for t in [0,5,10,20,30,50,75,99]:

    b = baseline[t]
    r = resource[t]
    e = evolutionary[t]


    print(
        f"{t:2d} | "
        f"{b['C']:10.3f} | "
        f"{r['C']:10.3f} | "
        f"{e['C']:12.3f} | "
        f"{e['P']:12.3f} | "
        f"{e['G']:10.3f}"
    )



# ==========================================
# Crossover
# ==========================================

cross = None


for r,e in zip(resource,evolutionary):

    if e["C"] > r["C"]:

        cross = e["t"]
        break



print("\n")
print("=" * 70)
print("FINAL RESULTS")
print("=" * 70)


print()

print(
    "Baseline Capability:",
    round(baseline[-1]["C"],3)
)

print(
    "Resource Scaling Capability:",
    round(resource[-1]["C"],3)
)

print(
    "Evolutionary Capability:",
    round(evolutionary[-1]["C"],3)
)


print()

print(
    "Final Frontier:",
    round(evolutionary[-1]["P"],3)
)

print(
    "Final Generator:",
    round(evolutionary[-1]["G"],3)
)


print(
    "Final Ω:",
    round(evolutionary[-1]["Omega"],5)
)



print("\n")


if cross:

    print(
        "Capability crossover detected:",
        f"t={cross}"
    )

else:

    print(
        "No crossover detected"
    )



print("\n")
print("=" * 70)
print("INTERPRETATION")
print("=" * 70)


print(
"""
If the framework is correct:

Baseline:
    fixed frontier
    fixed generator

Resource scaling:
    frontier expansion from external resources

Evolutionary:
    generator improves
    generator expands reachable space
    capability follows frontier

The important signal:

    ΔGm
      ↓
    ΔΩ
      ↓
    ΔP_reach
      ↓
    ΔC

under resource constraints.
"""
)
