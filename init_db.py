from tools import db


def init_db():
    from .models.ui_tests import UIPerformanceTest
    from .models.ui_report import UIReport
    from .models.thresholds import UIThresholds
    from .models.ui_baseline import UIBaseline
    db.get_shared_metadata().create_all(bind=db.engine)

