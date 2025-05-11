# filename: list_level_actors.py
# This script lists all actors in the current level using the Editor Actor Subsystem.

import unreal

# Get all level actors using the Editor Actor Subsystem
actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
all_actors = actor_subsystem.get_all_level_actors()

# Print their names to the Output Log
print("📋 Listing all actor names in the current level:")
for actor in all_actors:
    print(f" - {actor.get_name()}")
