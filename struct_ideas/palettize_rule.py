from config import *
from config.ConfigGroup import ModelGroup, TextureGroup, PaletteGroup
from config.PaletteConfig import TextureConfig, PaletteConfig, ModelConfig, TextureCardConfig

from eggtools.attributes import EggTag

# A different approach
# Instead of using dict keys, let's try out a list-tree route.

rule = [
    PaletteGroup("palette_group_1", [
        ModelGroup([
            ModelConfig("funny.egg", {
                "stupid": "config"
            }),
            ModelConfig("foo.egg", {
                "NodeAttributeConfig": {
                    EggTag("key", "value"): [
                        "nodes",
                        "that",
                        "need this"
                    ]
                }

            }),
            ModelConfig("bar.egg", {
                "custom_texture_configs": [
                    # drop shadows
                    TextureConfig("abc.png", {

                    })
                ]

            })
        ]),
        TextureGroup([
            TextureConfig("stupid.png", {

            })
        ]),
        PaletteConfig([

        ]),
        TextureCardConfig({
            "model_name": "ModelName",
            "texture_includes": TextureGroup([
                TextureConfig("Gahhhdfhshhdsf", {

                })
            ]),
            "palette_config": PaletteConfig([

            ])
        })
    ])
]

"""

        "textures": [
            TextureConfig("hello.png", {
                "dimension_x": 512,
                "dimension_y": 512
            })
        ],
"""
