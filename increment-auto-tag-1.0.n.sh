#!/bin/bash
# INSTRUCTIONS:
# This script increments the patch version for the 1.0.n series.
# Run the script in Git Bash: ./increment-auto-tag-1.0.n.sh
# Before running the script, make sure it has executable permissions: 
# chmod +x increment-auto-tag-1.0.n.sh

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

# If no tags exist, start with v1.0.0
if [ -z "$latest_tag" ]; then
  major=1
  minor=0
  patch=0
else
  # Split the latest tag into major, minor, and patch components
  IFS='.' read -r major minor patch <<<"${latest_tag#v}"

  # Validate the version format
  if [[ ! "$major" =~ ^1$ || ! "$minor" =~ ^0$ || ! "$patch" =~ ^[0-9]+$ ]]; then
    echo "Error: This script only handles 1.0.n versions. Latest tag: $latest_tag"
    exit 1
  fi

  # Increment the patch version
  patch=$((patch + 1))
fi

# Create the new tag
new_tag="v${major}.${minor}.${patch}"

# Append the current date and time to the tag (format: YYYY_MM_DD/HH_MM_SS-AMPM)
timestamp=$(date +"%Y_%m_%d/%I_%M_%S-%p")
new_tag="${new_tag}-${timestamp}"

# Create and push the new tag
git tag -a "$new_tag" -m "Auto-generated tag: $new_tag"
git push origin "$new_tag"

echo "Created and pushed tag: $new_tag"