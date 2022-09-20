# %%
import pandas as pd
import stanza
from pathlib import Path
# %% Analysis

data_path = Path("/Users/brandonmora/Library/CloudStorage/OneDrive-Inter-AmericanDevelopmentBankGroup/KIC/data")

search_terms = pd.read_csv(data_path / "socrata/clean/search_terms_clean.csv")
# %%
nlp = stanza.Pipeline('es')
# %%
