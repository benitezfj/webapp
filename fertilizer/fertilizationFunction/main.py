from fertilizer.fertilizationFunction.soy.soy_p1_quantity import soy_p1_quantity
from fertilizer.fertilizationFunction.soy.soy_p2_quantity import soy_p2_quantity
from fertilizer.fertilizationFunction.soy.soy_k1_quantity import soy_k1_quantity
from fertilizer.fertilizationFunction.soy.soy_k2_quantity import soy_k2_quantity
from fertilizer.fertilizationFunction.maize.maize_n1_quantity import maize_n1_quantity
from fertilizer.fertilizationFunction.maize.maize_p1_quantity import maize_p1_quantity
from fertilizer.fertilizationFunction.maize.maize_p2_quantity import maize_p2_quantity
from fertilizer.fertilizationFunction.maize.maize_k1_quantity import maize_k1_quantity
from fertilizer.fertilizationFunction.maize.maize_k2_quantity import maize_k2_quantity
from fertilizer.fertilizationFunction.wheat.wheat_n1_quantity import wheat_n1_quantity
from fertilizer.fertilizationFunction.wheat.wheat_p1_quantity import wheat_p1_quantity
from fertilizer.fertilizationFunction.wheat.wheat_k1_quantity import wheat_k1_quantity

"""
    Input 1  -> % of organic material
    Input 2 -> Previous crop
        - 'M' -> Maize
        - 'S' - Soy
        - 'W' -> Wheat
        - 'G' - Grass (gramínea)
        - 'C' - Cockle (consorcio o berberecho)
        - 'L' - Legume (leguminosa)
    Input 3 -> Expected productivity kg/ha
    Input 4 -> Clay tennor
        - 410 - 600 -> Class 1
        - 210 - 400 -> Class 2
    Input 5 -> K in soil mg/dm^3
    Input 6 -> Crop type
        - 'M' -> Maize
        - 'S' - Soy
        - 'W' -> Wheat
        - 'G' - Grass (gramínea)
        - 'C' - Cockle (consorcio o berberecho)
        - 'L' - Legume (leguminosa
    Input 7 -> P in soil mg/dm^3
    Input 8 -> Number of crops per year (1, 2, or 3)
    Input 9 -> Soil pH
    Input 10 -> Temperature of the crop
"""


def main(i1, i2, i3, i4, i5, i6, i7, i8, i9, i10):
    # Weighting coefficients. These values will indicate how
    # reliable the moaunts of fertilization we have obtained are.
    # That is, the weighting coefficient of a fertilization value
    # obtained from a trustworthy source is going to be higher
    # than the one obtained from a not-so-reliable source
    W1N = 1  # Weighting value for N1
    W1P = 1  # Weighting value for P1
    W2P = 1  # Weighting value for P2
    W1K = 1  # Weighting value for K1
    W2K = 1  # Weighting value for K2

    if i6 == "M":
        N1 = maize_n1_quantity(i2, i3, i1)
        P1 = maize_p1_quantity(i4, i3)
        P2 = maize_p2_quantity(i4, i7)
        K1 = maize_k1_quantity(i5, i3)
        K2 = maize_k2_quantity(i5, i8)
    elif i6 == "S":
        N1 = 0
        P1 = soy_p1_quantity(i4, i3)
        P2 = soy_p2_quantity(i4, i7)
        K1 = soy_k1_quantity(i5, i3)
        K2 = soy_k2_quantity(i5, i8)
    elif i6 == "W":
        N1 = wheat_n1_quantity(i2, i1, i3)
        P1 = wheat_p1_quantity(i4, i3)
        P2 = 0
        K1 = wheat_k1_quantity(i5, i3)
        K2 = 0

    Poso = [W1N * N1, P1 * W1P + P2 * W2P, K1 * W1K + K2 + W2K]

    print(Poso)
    if i9 > 5.5:
        print("Message = Attention! pH too high")
    else:
        print("Message = pH value is ok")
