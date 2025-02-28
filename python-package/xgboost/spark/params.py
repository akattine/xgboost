# type: ignore
"""Xgboost pyspark integration submodule for params."""
# pylint: disable=too-few-public-methods
from pyspark.ml.param import TypeConverters
from pyspark.ml.param.shared import Param, Params


class HasArbitraryParamsDict(Params):
    """
    This is a Params based class that is extended by _SparkXGBParams
    and holds the variable to store the **kwargs parts of the XGBoost
    input.
    """

    arbitrary_params_dict = Param(
        Params._dummy(),
        "arbitrary_params_dict",
        "arbitrary_params_dict This parameter holds all of the additional parameters which are "
        "not exposed as the the XGBoost Spark estimator params but can be recognized by "
        "underlying XGBoost library. It is stored as a dictionary.",
    )


class HasBaseMarginCol(Params):
    """
    This is a Params based class that is extended by _SparkXGBParams
    and holds the variable to store the base margin column part of XGboost.
    """

    base_margin_col = Param(
        Params._dummy(),
        "base_margin_col",
        "This stores the name for the column of the base margin",
    )


class HasFeaturesCols(Params):
    """
    Mixin for param featuresCols: a list of feature column names.
    This parameter is taken effect only when use_gpu is enabled.
    """

    features_cols = Param(
        Params._dummy(),
        "features_cols",
        "feature column names.",
        typeConverter=TypeConverters.toListString,
    )

    def __init__(self):
        super().__init__()
        self._setDefault(features_cols=[])
