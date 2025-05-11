# filename: set_collision_all_static_mesh.py
# run: exec(open(r"E:\UNREAL ENGINE\TEMPLATE PROJECTS\GameAnimationSample\set_collision_all_static_mesh.py").read())

import unreal

# Access the editor actor subsystem
editor_subsys = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

if editor_subsys:
    all_actors = editor_subsys.get_all_level_actors()

    for actor in all_actors:
        if isinstance(actor, unreal.StaticMeshActor):
            static_mesh_comp = actor.get_editor_property(
                "static_mesh_component")
            if static_mesh_comp:
                # Enable collision: both query and physics
                static_mesh_comp.set_collision_enabled(
                    unreal.CollisionEnabled.QUERY_AND_PHYSICS)

                # Set response to block for key channels (must use correct enum constants)
                for channel in [
                    unreal.CollisionChannel.CC_WorldStatic,
                    unreal.CollisionChannel.CC_WorldDynamic,
                    unreal.CollisionChannel.CC_Pawn,
                ]:
                    static_mesh_comp.set_collision_response_to_channel(
                        channel, unreal.CollisionResponseType.ECR_Block
                    )

                print("Collision set for:", actor.get_name())
            else:
                print("No StaticMeshComponent on:", actor.get_name())
else:
    print("EditorActorSubsystem not available — are you in the editor?")
