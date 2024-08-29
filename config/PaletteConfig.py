class TheConfig:
    def __init__(self, config:dict):
        palette_configs = []
        for palette_group in config.keys():
            palette_configs.append()

class PaletteConfig:
    def __init__(self, palette_name, config_attrs:dict=None):

        pass


class ModelConfig:
    def __init__(self, model_name, config_attrs:dict=None):
        self.name = model_name
        self.data = config_attrs
        pass


class TextureConfig:
    def __init__(self, texture_name, config_attrs:dict):
        self.dimension_x = config_attrs.get("dimension_x")
        self.dimension_y = config_attrs.get("dimension_x")
        self.color_mode = config_attrs.get("color_mode")
        self.generic = config_attrs.get("generic")


class TextureCardConfig:
    def __init__(self, palette_name, config_attrs: dict = None):
        pass