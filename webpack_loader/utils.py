from django.utils.module_loading import import_string

from .config import load_config


_loaders = {}


def get_loader(config_name):
    if config_name not in _loaders:
        loader_class = load_config(config_name)['LOADER_CLASS']
        if not callable(loader_class):
            loader_class = import_string(loader_class)
        _loaders[config_name] = loader_class(config_name)
    return _loaders[config_name]
