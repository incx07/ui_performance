from sqlalchemy import String, Column, Integer, Float, Text, Boolean, JSON
from tools import db_tools, db, rpc_tools, constants as c, secrets_tools


class UIReport(db_tools.AbstractBaseMixin, db.Base, rpc_tools.RpcMixin):
    __tablename__ = "ui_report"

    id = Column(Integer, primary_key=True)
    uid = Column(String(128), unique=True, nullable=False)
    name = Column(String(128), unique=False)
    project_id = Column(Integer, unique=False, nullable=False)
    test_status = Column(
        JSON,
        default={
            "status": "Pending...",
            "percentage": 0,
            "description": "Check if there are enough workers to perform the test"
        }
    )
    start_time = Column(String(128), unique=False)
    stop_time = Column(String(128), unique=False)
    duration = Column(Integer, unique=False, nullable=True)
    is_active = Column(Boolean, unique=False)
    browser = Column(String(128), unique=False)
    browser_version = Column(String(128), unique=False)
    environment = Column(String(128), unique=False, nullable=True)
    test_type = Column(String(128), unique=False, nullable=True)
    base_url = Column(String(128), unique=False, nullable=True)
    thresholds_total = Column(Integer, unique=False, nullable=True, default=0)
    thresholds_failed = Column(Integer, unique=False, nullable=True, default=0)
    exception = Column(String(1024), unique=False)
    passed = Column(Boolean, unique=False, default=True)
    loops = Column(Integer, unique=False, nullable=True)
    aggregation = Column(String(128), unique=False)