class TextureGroup:
    def __init__(self, texture_configs):
        pass

class ModelGroup:
    config_data = {}

    def __init__(self, model_configs):
        # Holds all ModelConfig data
        for config in model_configs:
            self.config_data[config.name] = config.data
        pass

class PaletteGroup:
    def __init__(self, name, config):
        pass