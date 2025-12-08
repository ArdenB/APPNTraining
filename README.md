# APPNTraining

Basic training document


## Setup a conda environment

```bash
conda config --add channels conda-forge
conda update -n base -c defaults conda
conda create --name APPNtraining
conda activate APPNtraining
conda install dask xarray pandas matplotlib palettable cartopy seaborn ipdb numba bottleneck netCDF4 webcolors gitpython scikit-learn xgboost joblib optuna ipdb rioxarray geopandas pyarrow
```

