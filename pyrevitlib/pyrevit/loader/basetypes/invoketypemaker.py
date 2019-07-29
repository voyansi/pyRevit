"""Prepare and compile direct invoke script types."""
from pyrevit.coreutils import create_type, create_ext_command_attrs
from pyrevit.coreutils.logger import get_logger

from pyrevit.loader.basetypes import CMD_EXECUTOR_TYPE


#pylint: disable=W0703,C0302,C0103
mlogger = get_logger(__name__)


def create_executor_type(extension, module_builder, cmd_component): #pylint: disable=W0613
    mlogger.debug('Creating executor type for: %s', cmd_component)

    create_type(module_builder,
                CMD_EXECUTOR_TYPE,
                cmd_component.unique_name or '',
                create_ext_command_attrs(),
                cmd_component.get_full_script_address() or '',
                cmd_component.assembly or '',
                '',
                '',
                cmd_component.name or '',
                cmd_component.bundle_name or '',
                extension.name or '',
                cmd_component.unique_name or '',
                0,
                0)

    mlogger.debug('Successfully created executor type for: %s', cmd_component)
    cmd_component.class_name = cmd_component.unique_name
