from typing import Any
from typing import Optional
from typing import Union

import sqlalchemy as sa


class Upsert(sa.sql.Insert):
    __visit_name__ = "upsert"
    _propagate_attrs = {"compile_state_plugin": "yql"}
    stringify_dialect = "yql"


@sa.sql.base.CompileState.plugin_for("yql", "upsert")
class UpsertDMLState(sa.sql.dml.InsertDMLState):
    pass
