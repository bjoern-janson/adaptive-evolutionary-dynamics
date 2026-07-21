"""
Saturated Frontier Phase Boundary Experiment

Tests:

        ΔGm → ΔΩ → ΔP_reach → ΔC

with realistic constraints:

- generator growth saturates
- reachable frontier saturates
- resource scaling has diminishing returns
- evolutionary advantage comes from improving dynamics,
  not infinite exponential growth


Key measurements:

C(t)       = capability
P(t)       = reachable possibility frontier
Gm(t)      = generator capacity
Lambda(t)  = capability velocity
Omega(t)   = change in capability velocity

"""

import math


TIMESTEPS = 100


# ==========================================
# Parameters
# ==========================================

initial_C = 1.0
initial_P = 10.0
initial_G = 1.0


# Capability movement toward frontier
alpha = 0.20


# Generator logistic growth
gamma = 0.20
G_capacity = 10.0


# Frontier expansion
beta = 0.05
P_capacity = 1000.0


# Resource system
resource_growth = 1.08
resource_frontier_gain = 0.05


# ==========================================
# Baseline
# ==========================================

def baseline_system():

    C = initial_C
    P = initial_P

    history = []

    for t in range(TIMESTEPS):

        previous_C = C

        history.append({
            "t": t,
            "C": C,
            "P": P,
            "G": 1.0,
            "Lambda": C - previous_C,
            "Omega": 0
        })

        C += alpha * (P - C)


    return history



# ==========================================
# Resource scaling
# ==========================================

def resource_system():

    C = initial_C
    P = initial_P
    R = 1.0

    history = []

    previous_lambda = 0


    for t in range(TIMESTEPS):

        previous_C = C


        C += alpha * (P - C)


        # resources increase

        R *= resource_growth


        # resource expands frontier
        # but saturates

        P += resource_frontier_gain * R * (1 - P/P_capacity)


        Lambda = C - previous_C
        Omega = Lambda - previous_lambda


        history.append({
            "t": t,
            "C": C,
            "P": P,
            "G": 1.0,
            "Lambda": Lambda,
            "Omega": Omega
        })


        previous_lambda = Lambda


    return history



# ==========================================
# Evolutionary generator
# ==========================================

def evolutionary_system():

    C = initial_C
    P = initial_P
    G = initial_G

    history = []

    previous_lambda = 0


    for t in range(TIMESTEPS):

        previous_C = C


        # capability follows frontier

        C += alpha * (P - C)



        # generator improves but saturates

        G += gamma * G * (1 - G/G_capacity)



        # frontier expands based on generator

        P += (
            beta
            * G
            * P
            * (1 - P/P_capacity)
        )


        Lambda = C - previous_C

        Omega = Lambda - previous_lambda


        history.append({
            "t": t,
            "C": C,
            "P": P,
            "G": G,
            "Lambda": Lambda,
            "Omega": Omega
        })


        previous_lambda = Lambda


    return history



# ==========================================
# Run
# ==========================================

baseline = baseline_system()
resource = resource_system()
evolutionary = evolutionary_system()



# ==========================================
# Output
# ==========================================

print("="*75)
print("SATURATED FRONTIER PHASE BOUNDARY TEST")
print("="*75)


print("""
t | Baseline C | Resource C | Evolution C | Frontier | Generator | Omega
------------------------------------------------------------------------
""")


for t in [0,5,10,20,30,50,75,99]:

    b = baseline[t]
    r = resource[t]
    e = evolutionary[t]


    print(
        f"{t:2d} | "
        f"{b['C']:10.3f} | "
        f"{r['C']:10.3f} | "
        f"{e['C']:12.3f} | "
        f"{e['P']:10.3f} | "
        f"{e['G']:9.3f} | "
        f"{e['Omega']:8.5f}"
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
print("="*75)
print("FINAL RESULTS")
print("="*75)


print()

print(
    "Baseline Capability:",
    round(baseline[-1]["C"],3)
)

print(
    "Resource Capability:",
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
    "Final Lambda:",
    round(evolutionary[-1]["Lambda"],5)
)

print(
    "Final Omega:",
    round(evolutionary[-1]["Omega"],5)
)



print("\n")


if cross:

    print(
        "Capability crossover detected at:",
        f"t={cross}"
    )

else:

    print(
        "No crossover detected"
    )



print("\n")
print("="*75)
print("INTERPRETATION")
print("="*75)


print(
"""
The hypothesis predicts:

Resource scaling:
    ΔR > 0
    fixed generator
    frontier expands externally


Evolutionary system:
    ΔGm > 0
    Ω > 0 during transition
    frontier expansion becomes internally generated


Expected signature:

    generator improvement
            ↓
    acceleration increase
            ↓
    reachable frontier expansion
            ↓
    capability increase


A phase boundary exists if the evolutionary
system changes the trajectory class rather
than only increasing the current capability.
"""
)
