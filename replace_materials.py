# filename: replace_materials.py prompt Python(REPL):
# E:/UNREAL ENGINE/TEMPLATE PROJECTS/GameAnimationSample/replace_materials.py

import unreal

# Define the material you want to replace
OLD_MAT_NAME = "M_Revit_Concrete_Default"
NEW_MAT_PATH = "/Game/Materials/Exterior/MI_Concrete_White.MI_Concrete_White"

# Load the new material
new_material = unreal.EditorAssetLibrary.load_asset(NEW_MAT_PATH)

# Iterate over all static mesh actors
actors = unreal.EditorLevelLibrary.get_all_level_actors()
replaced_count = 0

for actor in actors:
    if isinstance(actor, unreal.StaticMeshActor):
        static_mesh_comp = actor.static_mesh_component
        materials = static_mesh_comp.get_materials()

        for i, mat in enumerate(materials):
            if mat.get_name() == OLD_MAT_NAME:
                static_mesh_comp.set_material(i, new_material)
                replaced_count += 1

unreal.log(f"✅ Replaced {replaced_count} material slots using '{OLD_MAT_NAME}' with '{NEW_MAT_PATH}'")
