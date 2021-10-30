import pickle
import os
import pandas


class ModelFileNotFound(Exception):
    pass


# copied code from training.
# I'm sure I could have isolated this as a module, but I'm copying and
# pasting for simplicity
def feature_extractor(dataframe):
    concatenated_text_information = \
            dataframe["title"] + \
            " " + dataframe["query"] + \
            " " + dataframe["concatenated_tags"].fillna("")
    return concatenated_text_information


def get_wrapped_model(model):
    
    def wrapped_model(product):
        formatted_product = {
            "query": [product.get("query", "")],
            "title": [product.get("title", "")],
            "concatenated_tags": [product.get("concatenated_tags", "")]
        }
        product_df = pandas.DataFrame(formatted_product)
        product_tf = feature_extractor(product_df)
        predicted = model.predict(product_tf)
        return predicted[-1]
    
    return wrapped_model


def get_model():
    model_path = os.environ.get("MODEL_PATH")
    if model_path is None:
        raise ModelFileNotFound("Could not find model file")
    
    model = None
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)
    
    return get_wrapped_model(model)

