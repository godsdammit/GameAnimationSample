# filename: set_complex_collision.py
# This script sets the collision complexity of all static meshes in a specified folder to "USE_COMPLEX_AS_SIMPLE"
# Create the Python script content for setting complex collision on all static meshes in a specified folder in Unreal Engine

import unreal

# Set the name of the parent Actor containing your architecture
target_actor_name = "22001DAYCARERENO20v25_test_01_rvt"

# Get reference to the Editor Actor Subsystem
actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

# Get all actors in the current level
all_actors = actor_subsystem.get_all_level_actors()

# Find the actor with the given name
target_actor = None
for actor in all_actors:
    if actor.get_name() == target_actor_name:
        target_actor = actor
        break

if not target_actor:
    print(f"❌ Could not find actor named: {target_actor_name}")
else:
    print(f"🔍 Found target actor: {target_actor_name}")
    # Get attached static mesh components
    static_mesh_components = target_actor.get_components_by_class(
        unreal.StaticMeshComponent)

    count = 0
    for comp in static_mesh_components:
        mesh = comp.get_editor_property("static_mesh")
        if mesh:
            mesh.set_editor_property(
                "collision_complexity", unreal.CollisionComplexity.USE_COMPLEX_AS_SIMPLE)
            unreal.EditorAssetLibrary.save_loaded_asset(mesh)
            print(f"✅ Collision updated for: {mesh.get_name()}")
            count += 1

    print(f"🏁 Done. Updated collision on {count} static meshes.")
