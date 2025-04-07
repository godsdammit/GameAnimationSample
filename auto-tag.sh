#!/bin/bash
#INSTRUCTIONS: 
#Run the Script: Execute the script to automatically create and push a new tag:
#Execute the script by running IN GIT BASH TERMINAL:  ./auto-tag.sh
#
# Get the latest tag
latest_tag=$(git describe --tags --abbrev=0 2>/dev/null)

# Get the commit hash of the latest tag
latest_tag_commit=$(git rev-list -n 1 "$latest_tag" 2>/dev/null)

# Get the current commit hash
current_commit=$(git rev-parse HEAD)

# If the latest tag points to the current commit, exit the script
if [ "$latest_tag_commit" == "$current_commit" ]; then
  echo "The latest tag ($latest_tag) already points to the current commit. No new tag created."
  exit 0
fi

# If no tags exist, start with the initial version v1.0.0
if [ -z "$latest_tag" ]; then
  new_tag="v1.0.0"
else
  # Split the latest tag into major, minor, and patch components
  IFS='.' read -r major minor patch <<<"${latest_tag#v}"

  # Increment the patch version
  patch=$((patch + 1))

  # Create the new tag
  new_tag="v${major}.${minor}.${patch}"
fi

# Append the current date and time to the tag (format: YYYYMMDD-HHMMSS)
timestamp=$(date +"%Y%m%d-%H%M%S")
new_tag="${new_tag}-${timestamp}"

# Create and push the new tag
git tag -a "$new_tag" -m "Auto-generated tag: $new_tag"
git push origin "$new_tag"

echo "Created and pushed tag: $new_tag"