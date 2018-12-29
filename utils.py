import numpy as np
import pandas as pd

def estimate_uplift(data, T_label, Y_label):
    """
    Estiamte the difference in means between two groups.

    Parameters
    ----------
    data: pandas.DataFrame
        a dataframe of samples.

    Returns
    -------
    estimated_uplift: dict[Str: float] containing two items:
        "estimated_effect" - the difference in mean values of $y$ for treated and untreated samples.
        "standard_error" - 90% confidence intervals arround "estimated_effect"


    """
    base = data[data[T_label] == 0]
    variant = data[data[T_label] == 1]

    delta = variant[Y_label].mean() - base[Y_label].mean()
    delta_err = 1.96 * np.sqrt(
        variant[Y_label].var() / variant.shape[0] +
        base[Y_label].var() / base.shape[0])

    return {"estimated_effect": delta, "standard_error": delta_err}