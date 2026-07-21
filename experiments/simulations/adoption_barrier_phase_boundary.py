"""
Adoption Barrier Phase Boundary Experiment

Tests:

    ΔGm ≠ ΔΩ

A better generator does not automatically
create a phase transition.

A usable transition requires:

    Generator improvement
            ↓
       Adoption crossing
            ↓
     Reachable frontier growth
            ↓
        Capability acceleration


Three systems:

1. Successful transition

    Generator improves
    Adoption succeeds
    Frontier expands


2. Adoption barrier

    Generator improves
    Adoption blocked by friction
    Frontier stagnates


3. Resource scaling

    No generator improvement
    Capability grows externally


Variables:

G:
    generator potential

A:
    activated generator

P:
    reachable frontier

C:
    capability

Ω:
    evolutionary velocity proxy

"""


TIMESTEPS = 120



# ==========================================
# Parameters
# ==========================================

initial_C = 1.0
initial_P = 10.0

initial_G = 1.0
initial_A = 1.0



# Capability movement

alpha = 0.15



# Generator improvement

gamma = 0.15
G_capacity = 20.0



# Adoption

rho_success = 0.08

rho_barrier = 0.08
friction = 0.10



# Frontier

beta = 0.04
P_capacity = 10000.0



# ==========================================
# Simulation
# ==========================================

def simulate(mode):

    C = initial_C
    P = initial_P

    G = initial_G
    A = initial_A


    history = []

    previous_lambda = 0



    for t in range(TIMESTEPS):

        old_C = C


        # capability follows reachable space

        C += alpha*(P-C)



        # generator improves regardless

        G += gamma*G*(1-G/G_capacity)



        # adoption dynamics

        if mode == "success":

            A += rho_success*(G-A)



        elif mode == "barrier":

            A += rho_barrier*(G-A)

            # adoption resistance

            A -= friction*A



        elif mode == "resource":

            A = 1



        # prevent negative adoption

        A = max(A,0)



        # frontier expansion only through adoption

        if mode != "resource":

            P += (
                beta
                * A
                * P
                * (1-P/P_capacity)
            )

        else:

            P += (
                0.08
                * (1-P/P_capacity)
            )



        Lambda = C-old_C

        Omega = Lambda-previous_lambda



        history.append({

            "t":t,
            "C":C,
            "P":P,
            "G":G,
            "A":A,
            "Lambda":Lambda,
            "Omega":Omega

        })


        previous_lambda = Lambda



    return history



# ==========================================
# Run
# ==========================================

success = simulate("success")
barrier = simulate("barrier")
resource = simulate("resource")



# ==========================================
# Output
# ==========================================

print("="*85)
print("ADOPTION BARRIER PHASE BOUNDARY TEST")
print("="*85)


print("""
t | Success C | Barrier C | Resource C | Success A | Barrier A | Barrier Ω
---------------------------------------------------------------------------
""")


for t in [0,10,20,40,60,80,100,119]:

    s = success[t]
    b = barrier[t]
    r = resource[t]


    print(
        f"{t:3d} | "
        f"{s['C']:10.3f} | "
        f"{b['C']:10.3f} | "
        f"{r['C']:10.3f} | "
        f"{s['A']:9.3f} | "
        f"{b['A']:9.3f} | "
        f"{b['Omega']:9.5f}"
    )



# ==========================================
# Results
# ==========================================

print("\n")
print("="*85)
print("FINAL RESULTS")
print("="*85)


print()

print(
"Successful Capability:",
round(success[-1]["C"],3)
)

print(
"Barrier Capability:",
round(barrier[-1]["C"],3)
)

print(
"Resource Capability:",
round(resource[-1]["C"],3)
)


print()

print(
"Successful Generator:",
round(success[-1]["G"],3)
)

print(
"Barrier Generator:",
round(barrier[-1]["G"],3)
)


print()

print(
"Successful Adoption:",
round(success[-1]["A"],3)
)

print(
"Barrier Adoption:",
round(barrier[-1]["A"],3)
)


print()

print(
"Successful Frontier:",
round(success[-1]["P"],3)
)

print(
"Barrier Frontier:",
round(barrier[-1]["P"],3)
)



print("\n")
print("="*85)
print("FRAMEWORK INTERPRETATION")
print("="*85)


print(
"""
Prediction:

Both systems should have:

    ΔGm > 0


But only successful adoption should produce:

    ΔΩ > 0

and:

    ΔC > 0


Expected:

SUCCESS:

    Generator
        ↓
    Adoption
        ↓
    Frontier expansion
        ↓
    Capability acceleration


BARRIER:

    Generator
        ↓
    Adoption resistance
        ↓
    Frontier blocked
        ↓
    No phase transition


The experiment tests:

    Generator capacity
        ≠
    Realized evolutionary velocity
"""
)
