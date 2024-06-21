# app/lib/read_env.py


from dotenv import load_dotenv
from os import environ, getcwd
from os.path import exists, join

from app.lib.exceptions import EnvFileUnavailableError
from app.lib.log_config import CustomLogger
from app.lib.secret_retrieval import Doppler

BASE_PROJECT_PATH: str = getcwd()
ENV_LOC_ROOT: str = join(BASE_PROJECT_PATH, "assets", ".env")
ENV_LOC_APP: str = join(BASE_PROJECT_PATH, "app", "assets", ".env")


def read_env_file(file_loc: str | None = None, strict: bool = True) -> None:
    # print("read_env_file")
    logs: CustomLogger = CustomLogger()
    plog = logs.logger
    plog.debug("local env")
    # checking .env location
    if file_loc is None:
        if exists(ENV_LOC_ROOT):
            env_loc = ENV_LOC_ROOT
            plog.debug(f"{ENV_LOC_ROOT = }")
        elif exists(ENV_LOC_APP):
            env_loc = ENV_LOC_APP
            plog.debug(f"{ENV_LOC_APP}")
        else:
            if strict:
                try:
                    env_var_test = environ.get("ENVIRON", None)
                    plog.debug(env_var_test)
                    if (env_var_test is None):
                        raise EnvFileUnavailableError
                    else:
                        plog.warning("Environment variables located. Proceeding...")
                        return None
                except AttributeError:
                    raise EnvFileUnavailableError
    else:
        env_loc = file_loc
    # checking if env file exists
    if exists(env_loc):
        load_dotenv(dotenv_path=env_loc)
    else:
        if strict:
            raise EnvFileUnavailableError
        else:
            plog.warning("No environment file located. Proceeding...")
            return None
    # checking if env vars are populated
    user_tmp = environ.get("ENVIRON", None)
    plog.debug(f"{user_tmp = }")
    if user_tmp is None:
        if strict:
            raise EnvFileUnavailableError
        else:
            plog.warning("No environment variables found. Proceeding...")
    plog.debug("local env read")
    return None


def read_env_remote(environment: str = "dev", project: str = "rutificador") -> None:
    logs: CustomLogger = CustomLogger()
    plog = logs.logger
    plog.debug("remote env")
    # print("read_env_remote")
    if exists(ENV_LOC_ROOT):
        env_loc = ENV_LOC_ROOT
    elif exists(ENV_LOC_APP):
        env_loc = ENV_LOC_APP
    else:
        test_var_1: str | None = environ.get(f"DOPPLER_ACCESS_TOKEN_{environment}", None)
        test_var_2: str | None = environ.get("DOPPLER_ACCESS_TOKEN", None)
        test_var_3: str | None = environ.get("ENVIRON", None)
        if test_var_1 is None and test_var_2 is None and test_var_3 is None:
            raise Exception("No env var file")
        else:
            env_loc = None
    APP_ENVIRON = environ.get("ENVIRON", None)
    plog.debug(f"{APP_ENVIRON = }")
    if APP_ENVIRON is None:
        env_var: str = environment
    else:
        env_var: str = APP_ENVIRON
    plog.debug(f"{environment = } , {env_var = }")
    secrets_app: Doppler = Doppler(env=env_var, prj=project, token=env_loc)
    required_secrets: list[str] = [
        "DO_SPACES_ACI",
        "DO_SPACES_AKS",
        "DO_SPACES_BASE_URL",
        "DO_SPACES_LOCATION",
        "DO_SPACES_NAMESPACE",
        "RDF_API_BASE_URL",
        "RDF_USER",
        "RDF_PASS",
        "REDIS_USER",
        "REDIS_PASSWORD",
        "REDIS_URL",
        "REDIS_PORT",
        "REDIS_HOST",
    ]
    for secret in required_secrets:
        tmp_secret: str = secrets_app.retrieve_secret(secret=secret)
        # plog.debug(f"{secret = }, {tmp_secret = }")
        tmp_new_key: dict[str, str] = {
            secret: tmp_secret,
        }
        # plog.debug(f"{tmp_new_key = }")
        environ.update(tmp_new_key)
        # plog.debug(f"{environ.get(secret, None) = }")
    plog.debug("remote env read")
    return None
