from sqlalchemy.sql import expression
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.types import DateTime

class utcnow(expression.FunctionElement):
    type = DateTime()
    inherit_cache = True

@compiles(utcnow, 'oracle')
def oracle_utcnow(element, compiler, **kw):
    return "SYS_EXTRACT_UTC(SYSTIMESTAMP)"  
