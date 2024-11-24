import numpy as np

def get_variable_category(df):
    discrete_vars = []
    categorical_vars = []
    continuous_vars = []
    binary_vars = []
    id_vars = []
    
    for col in df.columns:
        unique_values = df[col].nunique()
        dtype = df[col].dtype
        
        # ID variables
        if unique_values == len(df):
            id_vars.append(col)
        
        # Binary variables
        elif unique_values == 2:
            binary_vars.append(col)
        
        # Categorical variables
        elif dtype == 'object':
            categorical_vars.append(col)
        
        # Continuous variables
        elif np.issubdtype(dtype, np.number) and unique_values > 10:
            continuous_vars.append(col)
        
        # Discrete variables
        elif np.issubdtype(dtype, np.number):
            discrete_vars.append(col)
    
    return discrete_vars, categorical_vars, continuous_vars, binary_vars, id_vars
