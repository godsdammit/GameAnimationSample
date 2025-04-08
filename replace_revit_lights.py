# #Generated for: Mr. Gary
# By: Juniper (ChatGPT) April 7, 2025 v4
# run in UE python (REPL) bash: exec(open("E:/UNREAL ENGINE/TEMPLATE PROJECTS/GameAnimationSample/replace_revit_lights.py").read())

import unreal
import re

# Load the Blueprint class
bp_class = unreal.EditorAssetLibrary.load_blueprint_class("/Game/Blueprints/Lights/BP_CeilingLight_01")

# Get all actors in level
actors = unreal.EditorLevelLibrary.get_all_level_actors()

# Pattern to match light mesh names with numeric ID suffix
pattern = r"M_Ceiling_Light_-_Flat_Round_100W_-_120V__\d+_?$"

replaced = 0

for actor in actors:
    if isinstance(actor, unreal.StaticMeshActor):
        mesh = actor.static_mesh_component.static_mesh
        if mesh:
            name = mesh.get_name()
            if re.fullmatch(pattern, name):
                loc = actor.get_actor_location()
                rot = actor.get_actor_rotation()
                unreal.EditorLevelLibrary.spawn_actor_from_class(bp_class, loc, rot)
                unreal.EditorLevelLibrary.destroy_actor(actor)
                replaced += 1

unreal.log(f"✅ Replaced {replaced} StaticMeshActor(s) with BP_CeilingLight_01.")
