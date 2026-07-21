"""
Delayed Generator Phase Boundary Experiment

Tests the temporal ordering:

        t_Gm < t_Ω < t_C

Hypothesis:

A system does not instantly gain capability when
a better generator appears.

The sequence should be:

1. Generator improvement
        ↓
2. Adoption / activation delay
        ↓
3. Reachable frontier expansion
        ↓
4. Capability acceleration


Variables:

Gm:
    generator potential

A:
    activated generator capacity

P:
    reachable frontier

C:
    capability

Lambda:
    capability velocity

Omega:
    change in capability velocity

"""


TIMESTEPS = 120


# ==========================================
# Parameters
# ==========================================

initial_C = 1.0
initial_P = 10.0

initial_G = 1.0
initial_A = 1.0


# Capability tracking

alpha = 0.15


# Generator improvement

gamma = 0.12
G_capacity = 20.0


# Adoption lag

rho = 0.05


# Frontier expansion

beta = 0.04
P_capacity = 10000.0



# ==========================================
# Baseline
# ==========================================

def baseline_system():

    C = initial_C
    P = initial_P

    history = []

    previous_lambda = 0


    for t in range(TIMESTEPS):

        old_C = C

        C += alpha * (P - C)

        Lambda = C - old_C

        Omega = Lambda - previous_lambda


        history.append({
            "t": t,
            "C": C,
            "P": P,
            "G": 1,
            "A": 1,
            "Lambda": Lambda,
            "Omega": Omega
        })


        previous_lambda = Lambda


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

        old_C = C


        C += alpha * (P-C)


        R *= 1.06


        P += (
            0.03
            * R
            * (1-P/P_capacity)
        )


        Lambda = C-old_C

        Omega = Lambda-previous_lambda


        history.append({
            "t": t,
            "C": C,
            "P": P,
            "G": 1,
            "A": 1,
            "Lambda": Lambda,
            "Omega": Omega
        })


        previous_lambda = Lambda


    return history



# ==========================================
# Delayed evolutionary system
# ==========================================

def evolutionary_system():

    C = initial_C
    P = initial_P


    G = initial_G
    A = initial_A


    history = []


    previous_lambda = 0


    for t in range(TIMESTEPS):

        old_C = C


        # Capability follows frontier

        C += alpha*(P-C)



        # Generator improves

        G += (
            gamma
            * G
            * (1-G/G_capacity)
        )


        # Adoption slowly catches up

        A += rho*(G-A)



        # Only adopted generator expands frontier

        P += (
            beta
            * A
            * P
            * (1-P/P_capacity)
        )


        Lambda = C-old_C

        Omega = Lambda-previous_lambda


        history.append({
            "t": t,
            "C": C,
            "P": P,
            "G": G,
            "A": A,
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
# Find transition points
# ==========================================

def first_positive_change(data, key):

    for x in data:

        if x[key] > 0:

            return x["t"]

    return None



# Generator improvement start

t_Gm = None

for x in evolutionary:

    if x["G"] > initial_G:

        t_Gm = x["t"]
        break



# Omega peak

omega_peak = max(
    evolutionary,
    key=lambda x:x["Omega"]
)

t_Omega = omega_peak["t"]



# Capability acceleration point

lambda_peak = max(
    evolutionary,
    key=lambda x:x["Lambda"]
)

t_C = lambda_peak["t"]



# ==========================================
# Output
# ==========================================

print("="*75)
print("DELAYED GENERATOR PHASE BOUNDARY TEST")
print("="*75)


print(
"""
t | Resource C | Evolution C | Gm | Adoption | Frontier | Omega
----------------------------------------------------------------
"""
)


for t in [0,10,20,40,60,80,100,119]:

    r = resource[t]
    e = evolutionary[t]


    print(
        f"{t:3d} | "
        f"{r['C']:10.3f} | "
        f"{e['C']:12.3f} | "
        f"{e['G']:6.3f} | "
        f"{e['A']:8.3f} | "
        f"{e['P']:10.3f} | "
        f"{e['Omega']:8.5f}"
    )



print("\n")
print("="*75)
print("TEMPORAL ORDERING")
print("="*75)


print()

print(
"t_Gm (generator change):",
t_Gm
)

print(
"t_Ω (acceleration peak):",
t_Omega
)

print(
"t_C (capability acceleration):",
t_C
)



print("\n")
print("="*75)
print("FINAL RESULTS")
print("="*75)


print()

print(
"Resource Final Capability:",
round(resource[-1]["C"],3)
)

print(
"Evolutionary Final Capability:",
round(evolutionary[-1]["C"],3)
)


print()

print(
"Final Generator:",
round(evolutionary[-1]["G"],3)
)

print(
"Final Adoption:",
round(evolutionary[-1]["A"],3)
)

print(
"Final Frontier:",
round(evolutionary[-1]["P"],3)
)



print("\n")
print("="*75)
print("PHASE BOUNDARY TEST")
print("="*75)


if t_Gm < t_Omega < t_C:

    print(
"""
Temporal ordering detected:

        t_Gm < t_Ω < t_C

Evidence is consistent with:

Generator improvement
        ↓
Evolutionary acceleration
        ↓
Capability acceleration
"""
    )

else:

    print(
"""
Expected ordering not detected.

Possible causes:

- insufficient lag
- parameters need tuning
- model assumptions incorrect
"""
    )
