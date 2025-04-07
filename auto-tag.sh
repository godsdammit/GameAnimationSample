#!/bin/bash
# INSTRUCTIONS:
# Run the Script: Execute the script to automatically create and push a new tag.
# Execute the script by running IN GIT BASH TERMINAL: ./auto-tag.sh
# comment fake 100. 

# Ensure the script is run on the 'main' branch
current_branch=$(git rev-parse --abbrev-ref HEAD)
if [ "$current_branch" != "main" ]; then
  echo "Error: Tags should only be created on the 'main' branch."
  exit 1
fi

# Fetch the latest tags from the remote repository
git fetch --tags

# Get the latest tag
latest_tag=$(git describe --tags --abbrev=0 2>/dev/null)

# Strip the timestamp (if present) for validation
base_tag=${latest_tag%-*}

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
if [ -z "$base_tag" ]; then
  major=1
  minor=0
  patch=0
else
  # Split the base tag into major, minor, and patch components
  IFS='.' read -r major minor patch <<<"${base_tag#v}"

  # Validate that major, minor, and patch are numbers
  if [[ ! "$major" =~ ^[0-9]+$ || ! "$minor" =~ ^[0-9]+$ || ! "$patch" =~ ^[0-9]+$ ]]; then
    echo "Error: Invalid version format in the latest tag ($latest_tag). Expected format: v<major>.<minor>.<patch>"
    echo "Falling back to v1.0.0 as the base tag."
    major=1
    minor=0
    patch=0
  fi

  # Increment the patch version
  patch=$((patch + 1))
fi

# Create the new tag
new_tag="v${major}.${minor}.${patch}"

# Create and push the new tag
git tag -a "$new_tag" -m "Auto-generated tag: $new_tag"
git push origin "$new_tag"

echo "Created and pushed tag: $new_tag"