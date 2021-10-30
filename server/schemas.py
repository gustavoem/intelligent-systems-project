CATEGORIZE_PRODUCT = {
    "type": "object",
    "properties": {
        "products": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "properties": {
    	            "title": {"type": "string"},
    	            "query": {"type": "string"},
                    "concatenated_tags": {"type": "string"}
                },
                "additionalProperties": False,
                "minProperties": 1
            }
        }
    },
    "required": ["products"]
}

