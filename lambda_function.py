import json
import logging

from app.controller.router import Router
from app.domain.repository.database import Database
from app.domain.repository.db_factory import DbFactory

logger = logging.getLogger(__name__)
router = None
db = None

def lambda_handler(event, context):
    logger.info("Trigger event: {0}\n".format(json.dumps(event)))
    global db
    global router
    try:
        if db is None:
            db = Database()
            DbFactory.set_db_instance(db)

        if router is None:
            router = Router()

        response = router.handle_request(event, context)
        return response
    except Exception as e:
        logger.exception(
            "Internal Server Error: %s" % (e)
        )
        response = {"status": 500, "message": "Internal Server Error"}
        return {"statusCode": 500, "body": json.dumps(response)}        