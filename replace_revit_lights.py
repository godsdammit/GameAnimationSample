import unreal

# Load the Blueprint class
bp_class = unreal.EditorAssetLibrary.load_blueprint_class("/Game/Blueprints/Lights/BP_CeilingLight_01")

# Get all actors in the level
actors = unreal.EditorLevelLibrary.get_all_level_actors()
replaced_count = 0

for actor in actors:
    tags = actor.get_tags()
    if any("Max_superclassId: light" in tag for tag in tags):
        location = actor.get_actor_location()
        rotation = actor.get_actor_rotation()
        new_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(bp_class, location, rotation)
        unreal.EditorLevelLibrary.destroy_actor(actor)
        replaced_count += 1

unreal.log(f"✅ Replaced {replaced_count} actors with BP_CeilingLight_01.")
