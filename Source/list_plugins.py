# filename:list_plugins.py
# #Generated for: Mr. Gary
# By: Juniper (ChatGPT) April 8, 2025 v4
# run in UE python (REPL) bash: exec(open("E:/UNREAL ENGINE/TEMPLATE PROJECTS/GameAnimationSample/Source/list_plugins.py").read())

import unreal

registry = unreal.AssetRegistryHelpers.get_asset_registry()
plugin_assets = registry.get_assets_by_path('/Engine/Plugins', recursive=True)

plugin_names = set()
for asset in plugin_assets:
    plugin_name = asset.package_name.split('/')[2]
    plugin_names.add(plugin_name)

for name in sorted(plugin_names):
    print(f"{name}")
