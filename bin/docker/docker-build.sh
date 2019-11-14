s=$BASH_SOURCE ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; SCRIPT_HOME="$s"  # get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
APP_HOME="$SCRIPT_HOME/../.."

cd $APP_HOME
  # delete docker
  docker image rm -f hungphat/falcon_intern

  # Build docker
  docker build -t hungphat/falcon_intern .
cd - 1>/dev/null
