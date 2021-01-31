(
    export MSYS_NO_PATHCONV=1
    ./dockerw.sh run --rm --volume "$PWD":/output whose_module:latest "$@" --output=/output --logs
)
