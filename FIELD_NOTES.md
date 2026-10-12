fabro run \
~/Projects/factory-workflows/.fabro/workflows/implement-task/workflow.toml \
--goal "Add a health check endpoint that returns JSON with status ok" \
-I verify_command="npm test"

Worker image

ghcr.io/ruslanstarikov/factory-worker:0.1.0

