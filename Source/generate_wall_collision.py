# #Generated for: Mr. Gary
# By: Juniper (ChatGPT) April 7, 2025 v4
# run in UE python (REPL) bash: exec(open("E:/UNREAL ENGINE/TEMPLATE PROJECTS/GameAnimationSample/Source/generate_wall_collision.py").read())
# filename: generate_wall_collision.py

import unreal

# Settings for Auto Convex Collision
accuracy = 6
max_hull_verts = 8
max_hulls_per_mesh = 2

# Get all selected assets in Content Browser
selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()

for asset in selected_assets:
    if isinstance(asset, unreal.StaticMesh):
        asset_name = asset.get_name().lower()
        
        # Skip meshes with "door" in the name
        if "door" in asset_name:
            unreal.log(f"⏭️ Skipped: {asset_name} (contains 'door')")
            continue

        # Generate Auto Convex Collision
        unreal.EditorStaticMeshLibrary.generate_convex_collision(asset, accuracy, max_hull_verts)

        # Set Collision Complexity
        asset.set_editor_property("collision_complexity", unreal.CollisionComplexity.USE_SIMPLE_AS_COMPLEX)

        # Save the asset
        unreal.EditorAssetLibrary.save_asset(asset.get_path_name())

        unreal.log(f"✅ Collision generated and saved for: {asset_name}")
    else:
        unreal.log_warning(f"⚠️ Skipped non-static mesh asset: {asset.get_name()}")
