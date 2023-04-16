from os import PathLike, makedirs
import os.path
import toml
from typing import Any, List

"""
    Dont ask why this is the only file with actual comments in it
    I was writing this code at a gym and decided that I'd be rather
    studious with how I approached this code, as chances are this is
    the only code that I will not be able to understand at a later date.

    I am really bad with file handling and the concept of config loading
    from the appdata folder is new to me, so hopefully this will help not
    only me to understand it, but others who may come across this code as well.
"""

class ApplicationConfig(object):

    application_path : PathLike
    DEFAULT_CONFIG_PATH : PathLike = "./assets/default_configs/config.default.toml"

    raw_config_data : dict

    std_app_dirs = ("playlists",)

    def __init__(self, application_path : PathLike) -> None:
        self.application_path = application_path

        if not os.path.exists(self.application_path):
            self.build_std_app_dirs()

        # Loads the config.toml from %appdata% or creates
        # a new config.toml and returns the default information.
        self.raw_config_data = self.ensure_default_configuration()

        self.upsert_existing_config_file(version_check=True)

    def build_std_app_dirs(self) -> None:
        for d in self.std_app_dirs:
            makedirs(os.path.join(self.application_path, d))

    def ensure_default_configuration(self) -> dict:

        # The value this function will return
        # This should at some point become a dictionary.
        ret_val = None

        if not os.path.exists(
            os.path.join(self.application_path, "config.toml")
        ):
            # Reads the default config from the assets folder
            with open(self.DEFAULT_CONFIG_PATH, 'r') as def_conf:
                
                # Create/open a real config file 
                with open(os.path.join(self.application_path, 'config.toml'), 'w+') as real_conf:

                    # Write the default config information
                    real_conf.write(def_conf.read())

                # Load the default data from the def_conf as the current config
                ret_val = toml.load(def_conf)

            # Return the default config in lieu of an existing one
            return ret_val
        
        # Open the current existing config from the config dir
        with open(
            os.path.join(self.application_path, "config.toml")
        ) as conf_file:
            
            # Load the toml file
            ret_val = toml.load(conf_file)

        # Return the loaded toml data
        return ret_val
    
    def set_config_option(self, new_value : Any, *config_path, 
                          protected : bool = True,
                          skip_upsert : bool = False) -> None:
        """
            Sets a config option. The config path should be a arbitrary argument list that
            leads a linear path towards the value that should be updated.
        """

        config_path = list(config_path)

        if len(config_path) < 2:
            raise ValueError("config_path length must exceed a length of 2")

        # Popping the last item from the path as we don't want it
        end_key = config_path.pop(-1)

        # Setting the entry point for the traversal
        x = self.raw_config_data

        # Iterate over the keys
        for c in config_path:

            # Additional optional protection to ensure that no extra config keys are made
            if protected:

                if c not in x.keys():
                    raise ValueError("Specified config key does not align with existing config. Is it up to date?")
                
            # Actual simple traversal thingy
            x = x[c]

        # Updating the value within the raw data thingy
        x[end_key] = new_value

        # Upsert the config, which can optionally be disabled
        if not skip_upsert:
            self.upsert_existing_config_file()

    # This is the most disgusting function I think I've ever written.
    def config_update_function(self, p : dict, kv : dict) -> None:

        # kv is a dict of new values to check for in p
        for k, v in kv.items():

            # if the value of the key is a dictionary...
            if isinstance(v, dict):

                # Make sure there is a place for this dictionary
                # as it must contain some meaning.
                if k not in p.keys() and len(v) > 0:
                    p[k] = {}

                # Run this same function but on the inner dictionary
                self.config_update_function(p[k], v)

                # Skip the rest of the code, fuck you I don't want to use else statements
                # (I will pay for this further down the line)
                continue

            # If this function is not a dict, and doesn't exist in the current existing config...
            if k not in p.keys():

                # Set the new value
                p[k] = v

    def do_a_version_check(self) -> None:
        """
            This function will check and see if the current active config in memory
            is up to date with the default config file. It will fill in keys which
            do not exist in the toml file. 
        """

        # Open the default config and load it into memory
        with open("./assets/default_configs/config.default.toml", 'r') as def_conf:
            raw_default_config = toml.load(def_conf)

        # Check and see if the config version of the current in-use config is lower than the default
        if raw_default_config['application']['config_version'] <= self.get_config_version():
            return # Don't run the rest of the function if the config is up-to-date
        
        # Since we're updating the config at this point, we need to specify that
        # we're also updating this value. The function does not overwrite values
        # so this needs to be done manually unfortunately.
        self.raw_config_data['application']['config_version'] = raw_default_config['application']['config_version']

        # Update the config if the version is higher on the default configuration
        self.config_update_function(self.raw_config_data, raw_default_config)

    def upsert_existing_config_file(self, version_check : bool = False) -> None:
        """
            Pushes any changes made to the raw config into the config file.

            Passing 'version_check' as True will check the default config (in assets) and update
            the config if needed (adding the non-existent config keys where applicable). 
            
            Otherwise, the function will only check against the current raw_config_values in program 
            memory.
        """

        # Optional version check moment
        if version_check:
            self.do_a_version_check()

        # Dump the current config from ram into the file stored in %appdata%
        with open(os.path.join(self.application_path, "config.toml"), 'w') as config_file:
            toml.dump(self.raw_config_data, config_file)

    def get_playlists_directory(self, *, fail_safe : bool = True) -> PathLike:

        # The assumed playlist path
        pl_path = os.path.join(self.application_path, 'playlists/')

        # Check and see if it exists, with an additional fail-safe just in case 
        # the directories aren't instantiated for whatever reason.
        if not os.path.exists(pl_path) and fail_safe:

            # Create the default directories
            self.build_std_app_dirs()

            # Run the function again, without the fail-safe
            return self.get_playlists_directory(fail_safe = False)

        # If the function is ran and the default fail-safe value is False, and the
        # directory doesn't exist, then raise an error
        elif fail_safe == False:
            raise FileNotFoundError("Failed to provide the playlists directory. Idk why this happened")

        # Return the path to the playlist
        return pl_path


    def get_debug_mode(self) -> bool:
        return self.raw_config_data['application']['debug_mode']

    def get_config_version(self) -> int:
        return self.raw_config_data['application']['config_version']

    def get_theme(self) -> str:
        """Returns the current selected themes for the program"""
        return self.raw_config_data['application']['theme']
    
    def get_toast_status(self) -> bool:
        """Returns whether or not the user wants ot recieve toasts"""
        return self.raw_config_data['application']['show_toasts']